from django.shortcuts import render, redirect
from .models import Student
from .forms import Input
from django.shortcuts import redirect, get_list_or_404
from django.contrib import messages



def list_students(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'student_list.html', context)


def add_student(request):
    context = {}
    form = Input()
    context = {'form': form}
    if request.method == 'POST':
        form  = Input(request.POST)
        if form.is_valid():
                form.save()
                return redirect('list_students')
    return render(request, 'new_student.html', context)


def edit_student(request, registeration_number):
     
     return redirect('list_students')

def delete_student(request, registeration_number):
    student = get_list_or_404(Student, registeration_number)
    student.delete()
    return redirect('list_students')



