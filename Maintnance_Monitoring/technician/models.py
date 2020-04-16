from django.db import models

# Create your models here.
class TechnicianModel(models.Model):
    tid = models.CharField(primary_key=True,max_length=20)
    tname = models.CharField(max_length=80)
    tdept = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    contact = models.IntegerField()