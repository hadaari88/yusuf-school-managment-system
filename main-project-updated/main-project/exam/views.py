from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Exam
from .forms import ExamForm

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, "exam/exam_list.html", {"exams": exams})

def exam_detail(request, slug):
    exam = get_object_or_404(Exam, slug=slug)
    return render(request, "exam/exam_detail.html", {"exam": exam})

def add_exam(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(request, "Exam added successfully!")
            return redirect("exam_detail", slug=exam.slug)
    else:
        form = ExamForm()
    return render(request, "exam/exam_form.html", {"form": form})

def edit_exam(request, slug):
    exam = get_object_or_404(Exam, slug=slug)
    if request.method == "POST":
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            exam = form.save()
            messages.success(request, "Exam updated successfully!")
            return redirect("exam_detail", slug=exam.slug)
    else:
        form = ExamForm(instance=exam)
    return render(request, "exam/exam_form.html", {"form": form, "exam": exam})

def delete_exam(request, slug):
    exam = get_object_or_404(Exam, slug=slug)
    if request.method == "POST":
        exam.delete()
        messages.success(request, "Exam deleted successfully!")
        return redirect("exam_list")
    return render(request, "exam/exam_confirm_delete.html", {"exam": exam})
