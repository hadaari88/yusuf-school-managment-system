from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout, login, authenticate
from subjects.models import Subject
from sports.models import Sport
from transport.models import Transport
from teachers.models import Teacher
from exam.models import Exam
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    """
    Main landing page that aggregates data from various apps.
    """
    context = {
        'subjects': Subject.objects.all(),
        'teachers': Teacher.objects.all(),
        'exams': Exam.objects.all(),
        'sports': Sport.objects.all(),
        'transports': Transport.objects.all(),
    }
    return render(request, 'home/index.html', context)

def login_view(request):
    """
    Handles user login.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'home/login.html', {'form': form})

def mark_notification_as_read(request):
    """
    Marks a notification as read.
    """
    return JsonResponse({"message": "Notification marked as read."})

def clear_all_notification(request):
    """
    Clears all notifications.
    """
    return JsonResponse({"message": "All notifications cleared."})

def inbox(request):
    """
    Renders the inbox page.
    """
    return render(request, 'home/inbox.html')

def home(request):
    """
    Alternative landing page.
    """
    context = {
        'subjects': Subject.objects.all(),
        'teachers': Teacher.objects.all(),
        'exams': Exam.objects.all(),
    }
    return render(request, 'home/index.html', context)

@login_required
def dashboard(request):
    """
    Dashboard view that gathers data from all apps.
    """
    if request.user.is_superuser:
        return redirect('department_dashboard')
    elif hasattr(request.user, 'teacher'):
        return redirect('teacher_dashboard')
    elif hasattr(request.user, 'student'):
        return redirect('student_dashboard')

    context = {
        'subjects': Subject.objects.all(),
        'teachers': Teacher.objects.all(),
        'exams': Exam.objects.all(),
        'sports': Sport.objects.all(),
        'transports': Transport.objects.all(),
    }
    return render(request, 'home/dashboard.html', context)

def custom_logout(request):
    """
    Logs out the user and redirects them to the login page.
    """
    logout(request)
    return redirect('login')

@login_required
def department_dashboard(request):
    """
    Admin dashboard view.
    """
    context = {
        'total_students': 2500,
        'total_teachers': 150,
        'total_employees': 600,
        'total_earnings': "10,000",
    }
    return render(request, 'home/admin_dashboard.html', context)

@login_required
def teacher_dashboard(request):
    """
    Teacher dashboard view.
    """
    context = {
        'assigned_subjects': Subject.objects.filter(teacher=request.user),
        'exams': Exam.objects.all(),
    }
    return render(request, 'home/teacher_dashboard.html', context)

@login_required
def student_dashboard(request):
    """
    Student dashboard view.
    """
    context = {
        'enrolled_subjects': Subject.objects.all(),
        'sports': Sport.objects.all(),
        'transports': Transport.objects.all(),
    }
    return render(request, 'home/student_dashboard.html', context)
