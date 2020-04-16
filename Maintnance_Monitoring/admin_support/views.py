from django.shortcuts import render,redirect

# Create your views here.
from admin_support.models import DepartmentModel, LabModel, SystemModel


def ad_support_login(request):
   uname = request.POST['t1']
   upass = request.POST['t2']
   if uname=="admin_support":
       if upass == 'support':
           return render(request, "admin_support/admin_support.html")
       else:
           message = {'msg': 'Invalid Password'}
           return render(request, "admin_support/admin_support_login.html", {'message': message})

   else:
       message = {'msg':'Invalid Username'}
       return render(request, "admin_support/admin_support_login.html", {'message':message})


def saveDepartment(request):
    dept_id = request.POST['d1']
    dept_name = request.POST['d2'].upper()
    deptid = DepartmentModel.objects.filter(d_id=dept_id)
    deptname = DepartmentModel.objects.filter(d_name=dept_name)
    if int(dept_id) >= 101 and int(dept_id) <= 120:
        if deptid:
            qs = DepartmentModel.objects.all()
            message = 'Idno Already Available'
            return render(request, "admin_support/add_dept.html", {'msg': message,"data":qs})


        else:
            if deptname:
                qs = DepartmentModel.objects.all()
                message = 'Department Already Available'
                return render(request, "admin_support/add_dept.html", {'msg': message, "data": qs})
            else:
                DepartmentModel(d_id=dept_id, d_name=dept_name).save()
                return redirect('add_dept')
    else:
        qs = DepartmentModel.objects.all()
        message = 'Department Id Must be in range 101 to 120'
        return render(request, "admin_support/add_dept.html", {'msg': message, "data": qs})


def addDepartment(request):
    qs = DepartmentModel.objects.all()
    return render(request,"admin_support/add_dept.html",{'data':qs})


def addLab(request):
    qs = DepartmentModel.objects.all()
    return render(request,"admin_support/add_lab.html",{'data':qs})


def saveLab(request):
    lab_dept = request.POST.get("l1")
    lab_name = request.POST['l3']
    lab = LabModel.objects.filter(l_name=lab_name)
    if lab:
        message = 'Lab Name Already Available'
        qs = DepartmentModel.objects.all()

        return render(request, "admin_support/add_lab.html", {'msg': message,"data":qs})
    else:
        LabModel(l_name=lab_name,lab_dept_id=lab_dept).save()
        qs = DepartmentModel.objects.all()
        return render(request, "admin_support/add_lab.html", {'data': qs})


def addSystem(request):
    dqs = DepartmentModel.objects.all()
    lqs = LabModel.objects.all()
    return render(request, "admin_support/add_system.html", {'data1': dqs,"data2":lqs})


def saveLab(request):
    lab_id = request.POST.get("l2")
    sys_no = request.POST['l3']
    lab = SystemModel.objects.filter(system_no=sys_no)
    if lab:
        message = 'System Number Already Available'
        qs = DepartmentModel.objects.all()

        return render(request, "admin_support/add_system.html", {'msg': message,"data":qs})
    else:
        SystemModel(lab_id_id=lab_id,system_no=sys_no).save()
        return addSystem(request)