from django.contrib import admin
from .models import NewsetStudent

# Register your models here.

@admin.register(NewsetStudent)
class NewsetStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']