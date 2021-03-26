from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    #path('index1/', views.index1, name='index1'),
    path('register/', views.register, name='register'),
    path('login/', views.SignIn, name='signIn'),
    path('details/', views.details, name='details'),
    path('edit_details/', views.edit_details, name='edit_details'),
    path('education/', views.education, name='education'),
    path('edit_education/<int:pk>/', views.edit_education, name='edit_education'),
    path('project/', views.project, name='project'),
    path('edit_project/<int:pk>/', views.edit_project, name='edit_project'),
    path('personaldetails/', views.personaldetails, name='personaldetails'),
    path('edit_personaldetails/<int:pk>/', views.edit_personaldetails, name='edit_personaldetails'),
    path('logout/', views.signout, name='logout'),
    path('resume/', views.resume, name='resume'),



]