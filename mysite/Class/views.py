from django.shortcuts import render, redirect
from .models import Class, ClassEnrollment
from .forms import NewClassForm, EditClassForm
from django.shortcuts import redirect, get_list_or_404, get_object_or_404
from students.models import Student
from django.db.models import Count

unit_in_place = None

def list_classes(request):
    classes = Class.objects.all()
    context = {'classes': classes}
    return render(request, 'list_classes.html', context)


def add_class(request):
    context = {}
    form = NewClassForm()
    context = {'form': form}
    if request.method == 'POST':
        form  = NewClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_classes')
    return render(request, 'add_class.html', context)


def edit_class(request, id):
    _class = get_object_or_404(Class, id=id) 
    
    if request.method == 'POST':
        form  = EditClassForm(request.POST, instance=_class)
        if form.is_valid():
                form.save()
                return redirect('list_classes')
    else:
        form = EditClassForm(instance=_class)
        context={"form":form }
        return render(request, 'update_classes.html', context)
    return redirect('list_classes')

def delete_class(request, id):
    _class = get_object_or_404(Class, id=id)
    _class.delete()
    return redirect('list_classes')
    
#############################################################


def all_available_courses(request, id):
    courses = Student.objects.values('major_course_of_study').annotate(count=Count('id'))
    context = {'courses ': courses }
    unit_in_place = get_object_or_404(Class, id)
    return render(request, 'add_courses_class.html', context)


def add_students_to_class(request, course_name ):

    all_students  = Student.objects.filter(major_course_of_study=course_name)
    for student in all_students:
        new_enrollment = ClassEnrollment( student_reg_no=student.registeration_number, class_name=class_name, cat1=0, cat2=0, cat3 =0, final_exam=0)
    new_enrollment.save()
    return redirect('all_available_classes')





