from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View

from faculty.models import Compliant_Model
from .models import  TechnicianModel
# Create your views here.
class Register_Tech(View):
    def get(self,request):
        return render(request,"technician_template/technician_register.html")
    def post(self,request):
        initial = 'TID-'
        tid =initial + str(TechnicianModel.objects.count() + 1)
        print(tid)
        tech_id = tid
        name = request.POST['name']
        dept = request.POST['dept_name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['contact']
        user = TechnicianModel.objects.filter(tid=tech_id,email=email)
        if user:
            msg = "Email Already Exist Please use another email"
            return render(request,"technician_template/technician_register.html",{"msg":msg})
        else:
            TechnicianModel(tid=tech_id,tname=name,tdept=dept,email=email,password=password,contact=mobile).save()
            msg = "Technician Register Successfully"
            return render(request,"technician_template/technician_register.html",{"msg":msg})


class Login_Check(View):
    def get(self,request):
        return render(request,"technician_template/technician_login.html")
    def post(self,request):
        try:
            uname = request.POST['email']
            password = request.POST['password']
            user = TechnicianModel.objects.get(email=uname,password=password)

            if user:
                request.session['user_name'] = user.tname
                request.session['user'] = user.tdept
                return render(request, "technician_template/tech_welcome.html")
        except TechnicianModel.DoesNotExist:
            msg = "please provide valid credentials"
            return render(request,"technician_template/technician_login.html",{"msg":msg})

def Logout_user(request):
    del request.session['user_name']
    return render(request,"technician_template/technician_login.html")


def Complaint_all(request):
    data = Compliant_Model.objects.filter(Q(d_name=request.session['user'])&Q(status="pending"))
    return render(request, "technician_template/tech_welcome.html",{"data":data})


def Solved_complaint(request):
    solved_data = Compliant_Model.objects.filter(Q(d_name=request.session['user']) & Q(status="solved"))
    return render(request, "technician_template/tech_welcome.html", {"solved_data": solved_data})
