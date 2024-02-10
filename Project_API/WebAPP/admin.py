from django.contrib import admin
from .models import Employee

# Define a custom admin class
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "ssc_score", "company", "experience")

# Register the Employee model with the custom admin class
admin.site.register(Employee, EmployeeAdmin)
