from django.contrib import admin
from .models import Department, Employee
class EmpAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}  # new
admin.site.register(Employee)
admin.site.register(Department)
# Register your models here.
