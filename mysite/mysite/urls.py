"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import add_student, list_students, delete_student, edit_student
from unit.views import add_unit, list_units, delete_unit, edit_unit
from Class.views import add_class, list_classes, delete_class, edit_class
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/add/', add_student, name='add_student'),
    path('student/list', list_students, name='list_students'),
    path('student/delete/<int:id>/', delete_student, name='delete_student'),
    path('student/edit/<int:id>', edit_student, name='edit_student'),

    path('unit/add/', add_unit, name='add_unit'),
    path('unit/list', list_units, name='list_units'),
    path('unit/delete/<int:id>/', delete_unit, name='delete_unit'),
    path('unit/edit/<int:id>', edit_unit, name='edit_unit'),

     path('class/add/', add_class, name='add_class'),
    path('class/list', list_classes, name='list_classes'),
    path('class/delete/<int:id>/', delete_class, name='delete_class'),
    path('class/edit/<int:id>', edit_class, name='edit_class')
]
