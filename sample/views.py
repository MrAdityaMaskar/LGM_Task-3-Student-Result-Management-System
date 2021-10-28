from django.shortcuts import render
from .models import Student


# Create your views here.


def sample(request):
    if request.method == 'POST':
        context = Student.objects.filter(student_id=request.POST['stud_id'])
        extra_context = {'student': context}
        return render(request, 'home.html', extra_context)

    return render(request, 'home.html')
