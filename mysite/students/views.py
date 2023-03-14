from django.shortcuts import render, redirect
from .models import Student
from .forms import NewStudentForm, EditStudentForm
from django.shortcuts import redirect, get_list_or_404, get_object_or_404
from django.contrib import messages



def list_students(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'list_students.html', context)


def add_student(request):
    context = {}
    form = NewStudentForm()
    context = {'form': form}
    if request.method == 'POST':
        form  = NewStudentForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('list_students')
    return render(request, 'add_student.html', context)


def edit_student(request, id):
    student = get_object_or_404(Student, id=id) 
    
    if request.method == 'POST':
        form  = EditStudentForm(request.POST, instance=student)
        if form.is_valid():
                form.save()
                return redirect('list_students')
    else:
        form = EditStudentForm(instance=student)
        context={"form":form }
        return render(request, 'update_student.html', context)

     
    return redirect('list_students')

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list_students')



