# Generated by Django 2.2 on 2020-01-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeReg_Model',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('epass', models.CharField(max_length=12)),
                ('edept', models.CharField(max_length=50)),
                ('edesig', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]
