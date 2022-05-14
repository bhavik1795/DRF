from django.contrib import admin
from .models import ConcreteStudent

# Register your models here.

@admin.register(ConcreteStudent)
class ConcreteStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']