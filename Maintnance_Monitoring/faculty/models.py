from django.db import models

# Create your models here.
from admin_support.models import SystemModel


class EmployeeReg_Model(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=80)
    email = models.EmailField()
    epass = models.CharField(max_length=12)
    edept = models.CharField(max_length=50)
    edesig = models.CharField(max_length=50)
    mobile = models.IntegerField()


class Compliant_Model(models.Model):
    sys_no = models.CharField(max_length=20)
    lab_name = models.CharField(max_length=20)
    d_name= models.CharField(max_length=20)
    issue = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    system_data=models.ManyToManyField(SystemModel,on_delete=models.CASCADE)