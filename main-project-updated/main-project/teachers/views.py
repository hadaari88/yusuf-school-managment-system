from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Teacher
from .forms import TeacherForm

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/teacher.html", {"teachers": teachers})

def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher added successfully!")
            return redirect("teacher_list")
    else:
        form = TeacherForm()
    return render(request, "teachers/add-teacher.html", {"form": form})

def view_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(request, "teachers/teacher-details.html", {"teacher": teacher})

def edit_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher updated successfully!")
            return redirect("teacher_list")
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "teachers/edit-teacher.html", {"form": form, "teacher": teacher})

def delete_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    if request.method == "POST":
        teacher.delete()
        messages.success(request, "Teacher deleted successfully!")
        return redirect("teacher_list")
    return render(request, "teachers/delete-confirmation.html", {"teacher": teacher})

def teacher_dashboard(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    context = {
        "teacher": teacher,
        "total_students": 0,       # Replace with your logic
        "total_classes": 0,        # Replace with your logic
        "upcoming_exams": 0,       # Replace with your logic
        "unread_notifications": 0, # Replace with your logic
        "upcoming_classes": [],    # Replace with your logic
        "recent_announcements": [] # Replace with your logic
    }
    return render(request, "teachers/teacher-dashboard.html", context)

from django.shortcuts import render, get_object_or_404
from .models import Teacher





