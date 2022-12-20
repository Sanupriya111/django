from django.shortcuts import render

from .forms import EmployeForm
# Create your views here.
def employee_list(request):
    return render(request,'empregister/employee_list.html')
def employee_form(request):
    form=EmployeForm()
    return render(request,'empregister/employee_form.html',{'form':form})
    
def employee_delete(request):
    return
