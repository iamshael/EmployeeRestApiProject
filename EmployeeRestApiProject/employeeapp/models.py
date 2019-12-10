from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=45)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=100)

    def __str__(self):
        return self.ename
