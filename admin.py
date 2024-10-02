
from django.contrib import admin
from .models import (Employee, Attendence)
# Register your models here.


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display  = ['id','name','designation','department','joining_date','email','address']


@admin.register(Attendence)
class AttendenceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'department', 'employee_name', 'attendence', 'time_in', 'time_out']
    list_filter = ['date', 'department', 'attendence']
    search_fields = ['employee__name']

    def employee_name(self, obj):
        return obj.employee.name

    employee_name.short_description = 'Employee Name'