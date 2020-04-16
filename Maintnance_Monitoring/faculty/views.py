from django.shortcuts import render,redirect
from django.views.generic import View

from admin_support.models import DepartmentModel,LabModel,SystemModel
from technician.models import TechnicianModel
from .models import EmployeeReg_Model, Compliant_Model


# Create your views here.
from .sendsms import sendSMS


class Save_Register(View):
    def post(self,request):
        eid = request.POST['eid']
        fname = request.POST['fname']
        email = request.POST['email']
        password = request.POST['upass']
        edept = request.POST['edept']
        desig = request.POST['desig']
        mobile = request.POST['mob']
        EmployeeReg_Model(eid=eid,ename=fname,email=email,epass=password,edept=edept,edesig=desig,mobile=mobile).save()
        return render(request,'faculty_template/register_fac.html',{"msg":"Your Registration is success"})



def Login_Check(request):
    if request.method == "POST" :
        try:
            uname = request.POST['email']
            upass = request.POST['password']
            user = EmployeeReg_Model.objects.get(email=uname,epass=upass)
            if user:
                request.session['user'] = user.ename
                return render(request,"faculty_template/employee_home.html")

        except EmployeeReg_Model.DoesNotExist:
            return render(request, 'faculty_template/login_page.html', {"msg": "Invalid Credentials"})
    return render(request,'faculty_template/login_page.html')


def Logout(request):
    del request.session
    return render(request,'faculty_template/login_page.html')


class Add_Get_Complaint(View):
    def post(self,request):
        sys_no = request.POST['sys_num']
        lab_name = request.POST['lab_name']
        d_name = request.POST['d_name']
        issue = request.POST['issue']
        tech = TechnicianModel.objects.filter(tdept=d_name)
        status = "Pending"
        name = []
        cno = []
        print(cno)
        for x in tech:
            cno.append(x.contact)
            name.append(x.tname)
        Compliant_Model(sys_no=sys_no,lab_name=lab_name,d_name=d_name,issue=issue,status=status).save()
        mess = "Hello Mr/Miss : " + str(name) + ". This is massege for maintanance of Library form "+d_name+" department system number is "+sys_no+ " and LAB Name is "+lab_name+" Please Resolve the problem as soon as possible"
        a = sendSMS(str(cno),mess)
        print(a)
        return Add_Complaint(request)


def Add_Complaint(request):
    dept = DepartmentModel.objects.all()
    lab = LabModel.objects.all()
    system = SystemModel.objects.all()
    return render(request,"faculty_template/add_complaint.html",{"dept":dept,"lab":lab,"system":system})



def All_Complaint(request):
    all_data = Compliant_Model.objects.all()
    return render(request,"faculty_template/all_complaint.html",{"data":all_data})


def Solved_Complaint(request):
    solve_data = Compliant_Model.objects.filter(status="solved")
    print(solve_data)
    return render(request,"faculty_template/solved_complaint.html",{"data":solve_data})