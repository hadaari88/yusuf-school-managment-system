from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject
from .forms import SubjectForm

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subject_list.html', {'subjects': subjects})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subjects/subject_form.html', {'form': form})

def view_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'subjects/subject_detail.html', {'subject': subject})

def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subjects/subject_form.html', {'form': form})

def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subjects/subject_confirm_delete.html', {'subject': subject})

def subject_dashboard(request):
    subjects = Subject.objects.all()
    total_subjects = subjects.count()
    return render(request, 'subjects/subject_dashboard.html', {'subjects': subjects, 'total_subjects': total_subjects})
