from django.contrib import admin
from .models import StudentList
from .models import Student
# Register your models here.

admin.site.register(StudentList)
admin.site.register(Student)
