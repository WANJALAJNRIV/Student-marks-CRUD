from django.db import models
from unit.models import Unit
   

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100)
    unit_code = models.ForeignKey(Unit, on_delete=models.CASCADE)
    

class ClassEnrollment(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100)
    student_reg_no = models.IntegerField()
    cat1 = models.DecimalField(max_digits=5, decimal_places=2)
    cat2 = models.DecimalField(max_digits=5, decimal_places=2)
    cat3 = models.DecimalField(max_digits=5, decimal_places=2)
    final_exam = models.DecimalField(max_digits=5, decimal_places=2)
    