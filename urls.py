from django.urls import path
from hrmsapp import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('newemployee/', views.addemployee, name = 'addemployee'),
    path('attendence/', views.attendence, name = 'attendence'),
    path('report/', views.report, name = 'report'),
]