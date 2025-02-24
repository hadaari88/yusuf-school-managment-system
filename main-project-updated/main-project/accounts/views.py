from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import FeePayment, SalaryPayment, Expense  # Ensure these models exist
from .forms import FeePaymentForm, SalaryPaymentForm, ExpenseForm  # Create forms accordingly

# Authentication views (already existing)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('department_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('department_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Fee Payment CRUD views

def fee_list(request):
    fees = FeePayment.objects.all()
    return render(request, 'accounts/fee_list.html', {'fees': fees})

def fee_detail(request, pk):
    fee = get_object_or_404(FeePayment, pk=pk)
    return render(request, 'accounts/fee_detail.html', {'fee': fee})

def add_fee_payment(request):
    if request.method == 'POST':
        form = FeePaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee_list')
    else:
        form = FeePaymentForm()
    return render(request, 'accounts/add_fee_payment.html', {'form': form})

def edit_fee_payment(request, pk):
    fee = get_object_or_404(FeePayment, pk=pk)
    if request.method == 'POST':
        form = FeePaymentForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fee_list')
    else:
        form = FeePaymentForm(instance=fee)
    return render(request, 'accounts/edit_fee_payment.html', {'form': form})

def delete_fee_payment(request, pk):
    fee = get_object_or_404(FeePayment, pk=pk)
    if request.method == 'POST':
        fee.delete()
        return redirect('fee_list')
    return render(request, 'accounts/delete_fee_payment.html', {'fee': fee})

# Similar CRUD views for Salary Payment

def salary_list(request):
    salaries = SalaryPayment.objects.all()
    return render(request, 'accounts/salary_list.html', {'salaries': salaries})

def salary_detail(request, pk):
    salary = get_object_or_404(SalaryPayment, pk=pk)
    return render(request, 'accounts/salary_detail.html', {'salary': salary})

def add_salary_payment(request):
    if request.method == 'POST':
        form = SalaryPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryPaymentForm()
    return render(request, 'accounts/add_salary_payment.html', {'form': form})

def edit_salary_payment(request, pk):
    salary = get_object_or_404(SalaryPayment, pk=pk)
    if request.method == 'POST':
        form = SalaryPaymentForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryPaymentForm(instance=salary)
    return render(request, 'accounts/edit_salary_payment.html', {'form': form})

def delete_salary_payment(request, pk):
    salary = get_object_or_404(SalaryPayment, pk=pk)
    if request.method == 'POST':
        salary.delete()
        return redirect('salary_list')
    return render(request, 'accounts/delete_salary_payment.html', {'salary': salary})

# Similar CRUD views for Expenses

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'accounts/expense_list.html', {'expenses': expenses})

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'accounts/expense_detail.html', {'expense': expense})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'accounts/add_expense.html', {'form': form})

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'accounts/edit_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'accounts/delete_expense.html', {'expense': expense})

# Example fees collection view (if needed)
def fees_collection(request):
    fees = FeePayment.objects.all()  # Or aggregate collection details
    return render(request, 'accounts/fees_collection.html', {'fees': fees})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import FeePayment, SalaryPayment, Expense
from .forms import FeePaymentForm, SalaryPaymentForm, ExpenseForm

# Existing authentication views here...

def expenses(request):
    """
    View to display a summary of expenses.
    """
    expense_list = Expense.objects.all()
    return render(request, 'accounts/expenses.html', {'expenses': expense_list})
def salary(request):
    # This view can serve as a summary page for salary payments
    salaries = SalaryPayment.objects.all()
    return render(request, 'accounts/salary.html', {'salaries': salaries})

