# employeemanagement/urls.py
from django.contrib import admin
from django.urls import path
from employees.views import employee_management
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('employee_management/', views.employee_management, name='employee_management'),
]
