from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name', 'subject', 'exam_type', 'date', 'description']
