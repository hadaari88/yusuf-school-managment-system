from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Department
from .forms import DepartmentForm
from django.utils.timezone import now

def department_list(request):
    """Display a list of all departments."""
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})

def department_detail(request, pk):
    """Show details of a specific department."""
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'department/department_detail.html', {'department': department})

def department_create(request):
    """Create a new department."""
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('department_list'))  # Fixed redirect
    else:
        form = DepartmentForm()
    return render(request, 'department/department_form.html', {'form': form})

def department_edit(request, pk):
    """Edit an existing department."""
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('department_list'))  # Fixed redirect
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department/department_form.html', {'form': form})

def department_delete(request, pk):
    """Delete a department."""
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect(reverse_lazy('department_list'))  # Fixed redirect
    return render(request, 'department/department_confirm_delete.html', {'department': department})

def department_dashboard(request):
    """Department dashboard view with statistics."""
    departments = Department.objects.all()
    
    # Handle 'created_at' safely
    if hasattr(Department, 'created_at'):
        new_departments = Department.objects.filter(created_at__gte=now().replace(month=1, day=1)).count()
    else:
        new_departments = 0  # Default value if 'created_at' doesn't exist
    
    context = {
        'departments': departments,
        'new_departments': new_departments,
    }
    return render(request, 'department/department_dashboard.html', context)

def department_by_code(request, code):
    """Find a department by its code."""
    department = get_object_or_404(Department, code=code)
    return render(request, 'department/department_detail.html', {'department': department})

def department_by_category(request, category):
    """Filter departments by category."""
    departments = Department.objects.filter(category=category)
    return render(request, 'department/department_list.html', {
        'departments': departments,
        'selected_category': category
    })
