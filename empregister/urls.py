from django.urls import path,include
from . import views

urlpatterns = [

    path('list/',views.employee_list),
    path('employee/',views.employee_form)
]
