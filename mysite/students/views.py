from django.shortcuts import render, redirect
from .models import Student
from .forms import NewStudentForm, EditStudentForm, StudentMarks
from django.shortcuts import redirect, get_list_or_404, get_object_or_404
from Class.models import Class, ClassEnrollment


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


def all_available_classes(request, id):
    classes = Class.objects.all()
    context = {'classes': classes}
    student_in_place = get_object_or_404(Student, id=id)
    context['id_number'] = student_in_place.id
    return render(request, 'add_student_to_class.html', context)


def add_one_student_to_class(request, class_id, student_id):
    new_class = get_object_or_404(Class, id=class_id)
    current_student = get_object_or_404(Student, id=student_id)
    new_enrollment = ClassEnrollment( student_reg_no=current_student.registeration_number, class_name=new_class.class_name, cat1=0, cat2=0, cat3 =0, final_exam=0)
    new_enrollment.save()
    return redirect('list_units')


def add_marks(request, id ):

    enrollment = get_object_or_404(ClassEnrollment, id=id)
    if request.method == 'POST':
        form  = StudentMarks(request.POST)
        if form.is_valid():
            enrollment.cat1 = form.cleaned_data['cat_1']
            enrollment.cat2 = form.cleaned_data['cat_2']
            enrollment.cat3 = form.cleaned_data['cat_3']
            enrollment.save()
            return redirect('list_students')
    else:
        form = StudentMarks()
        form.cat_1 = enrollment.cat1
        form.cat_2 = enrollment.cat2
        form.cat_3 = enrollment.cat3
        form.final_exam = enrollment.final_exam
        context={'form': form}
        return render(request, 'add_marks.html', context)
    

def enrolled_classes(request, student_id):
     current_student = get_object_or_404(Student, id=student_id)
     all_enrolled_classes = get_list_or_404(ClassEnrollment, student_reg_no=current_student.registeration_number)
     context = {'classes' : all_enrolled_classes, 'student':current_student}
     return render(request, 'enrolled_classes.html', context)




    
    

