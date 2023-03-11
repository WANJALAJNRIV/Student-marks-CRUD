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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/add/', add_student, name='add_student'),
    path('students/list', list_students, name='list_students'),
    path('student/delete/<str:registeration_number>/', delete_student, name='delete_student'),
    path('student/edit/<str:registeration_number>', edit_student, name='edit_student'),
]
