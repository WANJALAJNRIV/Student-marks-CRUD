from django.shortcuts import render, redirect
from .models import Student
from .forms import NewStudentForm, EditStudentForm, StudentMarks
from django.shortcuts import redirect, get_list_or_404, get_object_or_404
from Class.models import Class, ClassEnrollment

student_in_place = None


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
    return render(request, 'add_student_to_class.html', context)

def add_to_class(request, class_name ):
    new_enrollment = ClassEnrollment( student_reg_no=student_in_place.registeration_number, class_name=class_name, cat1=0, cat2=0, cat3 =0, final_exam=0)
    new_enrollment.save()
    return redirect('all_available_classes')


def add_marks(request, id ):
    
    if request.method == 'POST':
        enrollment = get_object_or_404(ClassEnrollment, id=id)

        form  = NewStudentForm(request.POST)

        if form.is_valid():
            enrollment.cat1 = form.cleaned_data['cat_1']
            enrollment.cat2 = form.cleaned_data['cat_2']
            enrollment.cat3 = form.cleaned_data['cat_3']
            enrollment.save()
            return redirect('list_students')
    else:
        form = NewStudentForm()
        context={'form': form}
        return render(request, 'add_marks.html', context)

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import io

def generate_marks_pdf(request, student_name, cat1, cat2, cat3):
    # Create a new buffer for the PDF file
    buffer = io.BytesIO()

    # Create a new PDF file
    pdf_file = canvas.Canvas(buffer, pagesize=letter)

    # Add content to the PDF file
    pdf_file.drawString(1*inch, 10*inch, 'Name: {}'.format(student_name))
    pdf_file.drawString(1*inch, 9*inch, 'Cat 1: {}'.format(cat1))
    pdf_file.drawString(1*inch, 8*inch, 'Cat 2: {}'.format(cat2))
    pdf_file.drawString(1*inch, 7*inch, 'Cat 3: {}'.format(cat3))

    # Save the PDF file
    pdf_file.save()

    # Set the buffer's file pointer at the beginning
    buffer.seek(0)

    # Create a new HTTP response with the PDF file as an attachment
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="marks.pdf"'

    return response







    
    

