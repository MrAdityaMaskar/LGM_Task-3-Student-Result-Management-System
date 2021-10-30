from django.shortcuts import render
from .models import Student
from .models import StudentList


# Create your views here.


def student(request):
    if request.method == 'POST':
        cont = StudentList.objects.filter(email=request.POST['email'])
        print(cont)
        check = ['Aditya']
        extra_context = {'studentinfo': cont, 'check': check}
        return render(request, 'student_info.html', extra_context)
    return render(request, 'student_info.html')


def index(request):
    return render(request, 'home.html')


def sample(request):
    if request.method == 'POST':
        context = Student.objects.filter(student_id=request.POST['stud_id'])
        check = ['Aditya']
        extra_context = {'student': context, 'check': check}
        return render(request, 'result.html', extra_context)

    return render(request, 'result.html')
