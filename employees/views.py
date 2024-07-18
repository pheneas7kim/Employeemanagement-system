# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm, SearchForm

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'password':
            request.session['is_authenticated'] = True
            return redirect('employee_management')  
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')

def logout(request):
    if request.session.get('is_authenticated', False):
        del request.session['is_authenticated']
    return redirect('login')

def employee_management(request):
    if not request.session.get('is_authenticated', False):
        return redirect('login')  
    
    form = EmployeeForm()
    search_form = SearchForm()
    employees = Employee.objects.all()

    if request.method == 'POST':
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'Save':
                form = EmployeeForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Employee added successfully.')
                    return redirect('employee_management')
            elif action == 'Clear':
                form = EmployeeForm()
        elif 'search' in request.POST:
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                employee_id = search_form.cleaned_data['employee_id']
                employees = Employee.objects.filter(employee_id=employee_id)
                if not employees:
                    messages.error(request, f'Employee with ID {employee_id} does not exist.')
               
                return render(request, 'index.html', {'form': form, 'search_form': search_form, 'employees': employees})
        elif 'delete' in request.POST:
            employee_id = request.POST.get('delete')
            employee = get_object_or_404(Employee, pk=employee_id)
            employee.delete()
            messages.success(request, f'Employee with ID {employee_id} deleted successfully.')
            return redirect('employee_management')
        elif 'update' in request.POST:
            employee_id = request.POST.get('update')
            employee = get_object_or_404(Employee, pk=employee_id)
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                messages.success(request, f'Employee with ID {employee_id} updated successfully.')
                return redirect('employee_management')

    return render(request, 'index.html', {'form': form, 'search_form': search_form, 'employees': employees})
