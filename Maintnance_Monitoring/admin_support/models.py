from django.db import models

class DepartmentModel(models.Model):
    d_id = models.IntegerField(primary_key=True,unique=True)
    d_name = models.CharField(max_length=50)

class LabModel(models.Model):
    l_id = models.AutoField(primary_key=True)
    l_name = models.CharField(max_length=30)
    lab_dept = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)

class SystemModel(models.Model):
    system_no = models.IntegerField(primary_key=True)
    lab_id = models.ManyToManyField(LabModel)
