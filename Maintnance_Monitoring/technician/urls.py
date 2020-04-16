from django.urls import path
from django.views.generic import TemplateView

from technician import views

urlpatterns = [
    path("",TemplateView.as_view(template_name="technician_template/technician_home.html"),name="technician/main"),
    path('register/',views.Register_Tech.as_view(),name="technician/register"),
    path("login/",views.Login_Check.as_view(),name="technician/login"),
    path('logout/',views.Logout_user,name="technician/logout"),
    path("complaint_all/",views.Complaint_all,name="technician/complaint_all"),
    path("solved_complaint/",views.Solved_complaint,name = "technician/solved_complaint")
]