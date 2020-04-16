from django.urls import path, include
from django.views.generic import TemplateView

from faculty import views

urlpatterns = [
    path('home', TemplateView.as_view(template_name="faculty_template/faculty_home.html"), name="faculty/faculty_home"),
    path('register_emp/',TemplateView.as_view(template_name="faculty_template/register_fac.html"),name="faculty/register_emp"),
    path('save_reg/',views.Save_Register.as_view(),name="faculty/save_reg"),
    path('login_page/',TemplateView.as_view(template_name='faculty_template/login_page.html'),name="faculty/login_page"),
    path('login_check/',views.Login_Check,name="faculty/login_check"),
    path('logout/',views.Logout,name="logout"),
    path('complaint/',views.Add_Get_Complaint.as_view(),name="complaint"),
    path('add_complaint/',views.Add_Complaint,name="add_complaint"),
    path('all_complaint/',views.All_Complaint,name="all_complaint"),
    path("solved_complaint/",views.Solved_Complaint,name="solved_complaint")


]
