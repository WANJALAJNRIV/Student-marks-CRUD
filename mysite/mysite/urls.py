#Wanjala Stephen David
# IN16/00055/20

from django.contrib import admin
from django.urls import path
from students.views import add_student, list_students, delete_student, edit_student, add_marks, add_one_student_to_class, all_available_classes, add_one_student_to_class, enrolled_classes, index, generate_mark_sheet
from unit.views import add_unit, list_units, delete_unit, edit_unit
from Class.views import add_class, list_classes, delete_class, edit_class, all_available_courses,add_students_to_class


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('student/add/', add_student, name='add_student'),
    path('student/list', list_students, name='list_students'),
    path('student/delete/<int:id>/', delete_student, name='delete_student'),
    path('student/edit/<int:id>', edit_student, name='edit_student'),
    path('student/availableclasses/<int:id>', all_available_classes, name='all_available_classes'),
    path('student/addtoclass/<int:class_id>/<int:student_id>/', add_one_student_to_class, name='add_one_student_to_class'),
    path('student/addmarks/<int:id>', add_marks, name='add_marks'),
    path('student/enrolledclasses/<int:student_id>', enrolled_classes, name='enrolled_classes'),
    path("student/marksheet/<int:student_id>/<int:class_id>", generate_mark_sheet, name="generate_mark_sheet"), 

    path('unit/add/', add_unit, name='add_unit'),
    path('unit/list', list_units, name='list_units'),
    path('unit/delete/<int:id>/', delete_unit, name='delete_unit'),
    path('unit/edit/<int:id>', edit_unit, name='edit_unit'),

    path('class/add/', add_class, name='add_class'),
    path('class/list', list_classes, name='list_classes'),
    path('class/delete/<int:id>/', delete_class, name='delete_class'),
    path('class/edit/<int:id>', edit_class, name='edit_class'),
    path('class/availablecourses/<int:id>', all_available_courses, name='all_available_courses'),
    path('class/addStudents/<str:course_name>/<str:registration_number>/', add_students_to_class, name='add_students_to_class'),









]
