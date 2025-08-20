from django.shortcuts import render,redirect,get_object_or_404
from company_app.forms import *
from company_app.models import *

# Create your views here.
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'create_company.html',{'form':form})

def company_list(request):
    company_data = CompanyModel.objects.all()
    return render(request, 'company_list.html', {'company_data':company_data})

def edit_company(request, id):
    data = get_object_or_404(CompanyModel, id=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=data)
    return render(request, 'edit_company.html', {'form':form})

def delete_company(request, id):
    get_object_or_404(CompanyModel, id=id).delete()
    return redirect('company_list')




def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html',{'form':form})

def employee_list(request):
    employee_data = EmployeeModel.objects.all()
    return render(request, 'employee_list.html', {'employee_data':employee_data})

def edit_employee(request, id):
    data = get_object_or_404(EmployeeModel, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=data)
    return render(request, 'edit_employee.html', {'form':form})

def delete_employee(request, id):
    get_object_or_404(EmployeeModel, id=id).delete()
    return redirect('employee_list')