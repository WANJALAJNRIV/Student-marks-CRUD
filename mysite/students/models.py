from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    registeration_number = models.CharField(max_length=13)
    major_course_of_study =  models.CharField(max_length=100)

    def __str_(self):
        return self.registeration_number

    