from django.db import models

class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.code
