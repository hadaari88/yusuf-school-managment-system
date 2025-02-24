from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Parent
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notifications.utils import create_notification  # Adjust path as needed

# ---------------------------
# ADD STUDENT
# ---------------------------
@login_required
def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')

        # Retrieve parent data from the form
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        # Save parent information
        parent = Parent.objects.create(
            father_name=father_name,
            father_occupation=father_occupation,
            father_mobile=father_mobile,
            father_email=father_email,
            mother_name=mother_name,
            mother_occupation=mother_occupation,
            mother_mobile=mother_mobile,
            mother_email=mother_email,
            present_address=present_address,
            permanent_address=permanent_address
        )

        # Save student information
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            gender=gender,
            date_of_birth=date_of_birth,
            student_class=student_class,
            religion=religion,
            joining_date=joining_date,
            mobile_number=mobile_number,
            admission_number=admission_number,
            section=section,
            student_image=student_image,
            parent=parent
        )
        create_notification(request.user, f"Added Student: {student.first_name} {student.last_name}")  # type: ignore
        messages.success(request, "Student added Successfully")
        return redirect("student_list")
  
    return render(request, "students/add-student.html")


# ---------------------------
# STUDENT LIST VIEW
# ---------------------------
@login_required
def student_list(request):
    students = Student.objects.select_related('parent').all()
    
    unread_notification = []
    if request.user.is_authenticated:
        unread_notification = request.user.notification_set.filter(is_read=False)

    context = {
        'student_list': students,
        'unread_notification': unread_notification
    }
    return render(request, "students/student_list.html", context)


# ---------------------------
# STUDENT DASHBOARD VIEW (for an individual student)
# ---------------------------
@login_required
def student_dashboard(request, slug):
    student = get_object_or_404(Student, slug=slug)
    return render(request, "students/student_dashboard.html", {"student": student})


# ---------------------------
# EDIT STUDENT
# ---------------------------
@login_required
def edit_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    parent = student.parent  # Assume each student has a parent
    if request.method == "POST":
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.student_id = request.POST.get('student_id')
        student.gender = request.POST.get('gender')
        student.date_of_birth = request.POST.get('date_of_birth')
        student.student_class = request.POST.get('student_class')
        student.religion = request.POST.get('religion')
        student.joining_date = request.POST.get('joining_date')
        student.mobile_number = request.POST.get('mobile_number')
        student.admission_number = request.POST.get('admission_number')
        student.section = request.POST.get('section')
        if request.FILES.get('student_image'):
            student.student_image = request.FILES.get('student_image')
        
        # Update parent information
        parent.father_name = request.POST.get('father_name')
        parent.father_occupation = request.POST.get('father_occupation')
        parent.father_mobile = request.POST.get('father_mobile')
        parent.father_email = request.POST.get('father_email')
        parent.mother_name = request.POST.get('mother_name')
        parent.mother_occupation = request.POST.get('mother_occupation')
        parent.mother_mobile = request.POST.get('mother_mobile')
        parent.mother_email = request.POST.get('mother_email')
        parent.present_address = request.POST.get('present_address')
        parent.permanent_address = request.POST.get('permanent_address')
        parent.save()
        student.save()
        create_notification(request.user, f"Updated Student: {student.first_name} {student.last_name}")  # type: ignore
        
        return redirect("student_list")
    return render(request, "students/edit-student.html", {'student': student, 'parent': parent})


# ---------------------------
# VIEW STUDENT
# ---------------------------
@login_required
def view_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    return render(request, "students/student-details.html", {"student": student})


# ---------------------------
# DELETE STUDENT
# ---------------------------
@login_required
def delete_student(request, slug):
    if request.method == "POST":
        student = get_object_or_404(Student, slug=slug)
        student_name = f"{student.first_name} {student.last_name}"
        student.delete()
        create_notification(request.user, f"Deleted student: {student_name}")  # type: ignore
        return redirect("student_list")
    return HttpResponseForbidden()


# ---------------------------
# Notification Placeholder (if needed)
# ---------------------------
def create_notification(user, message):
    # Placeholder for notification creation logic.
    print(f"Notification for {user}: {message}")




