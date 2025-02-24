from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, PasswordResetRequest
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')  # Get role from the form (student, teacher, admin)
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('signup')  # Redirect back to signup page
        
        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        
        # Assign role properly
        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True
        else:
            messages.error(request, "Invalid role selection.")
            return redirect('signup')

        user.save()
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('index')
    
    return render(request, 'authentication/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful!')
            
            # Redirect based on user role
            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_student:
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid user role.')
                return redirect('index')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'authentication/login.html')


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()
        
        if user:
            token = get_random_string(32)
            reset_request = PasswordResetRequest.objects.create(user=user, email=email, token=token)
            reset_request.send_reset_email()
            messages.success(request, 'A reset link has been sent to your email.')
        else:
            messages.error(request, 'Email not found.')

    return render(request, 'authentication/forgot-password.html')


def reset_password_view(request, token):
    reset_request = get_object_or_404(PasswordResetRequest, token=token)
    
    # Check if token is expired
    if not reset_request.is_valid():
        messages.error(request, 'Reset link expired or invalid.')
        return redirect('login')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        reset_request.user.set_password(new_password)
        reset_request.user.save()
        reset_request.delete()  # Remove used reset request
        messages.success(request, 'Password reset successful. You can now log in.')
        return redirect('login')

    return render(request, 'authentication/reset_password.html', {'token': token})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')
