# Generated by Django 2.2 on 2020-02-20 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentmodel',
            name='d_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='departmentmodel',
            name='d_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='labmodel',
            name='l_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='labmodel',
            name='lab_dept',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admin_support.DepartmentModel'),
        ),
        migrations.RemoveField(
            model_name='systemmodel',
            name='lab_id',
        ),
        migrations.AddField(
            model_name='systemmodel',
            name='lab_id',
            field=models.ManyToManyField(to='admin_support.LabModel'),
        ),
    ]
