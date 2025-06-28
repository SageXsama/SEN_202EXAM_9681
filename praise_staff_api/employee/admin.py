from django.contrib import admin
from .models import Employee, EmployeeProfile
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
# Register your models here.
