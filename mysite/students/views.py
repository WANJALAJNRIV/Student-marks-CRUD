from django.shortcuts import render
from .models import Student
from .forms import NewStudentForm



def student_list(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'student_list.html', context)


def add_student(request):
    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = NewStudentForm()
    return render(request, 'add_student.html', {'form': form})
