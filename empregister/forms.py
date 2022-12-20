
from cProfile import label
from django.forms import ModelForm
from .models import Employee

class EmployeForm(ModelForm):
    class Meta:
        model = Employee
        fields=('name','empcode','mobileno','position')
        labels={
            'name':'Full Name',
            'empcode':'Emp-Code',
            'mobileno':'MobileNo',
            'position':"Position"

        }
        def __init__(self,*arg,**kwarg):
            super(EmployeForm,self).__init__(*arg,**kwarg)
            self.fields['position'].empty_label="Select"