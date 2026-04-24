from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('job_list/',views.job_list,name="job_list"),
    path('add/', views.add_job, name='add_job'),
    path('signup/', views.signup, name='register'),
    path('edit/<int:id>/', views.edit_job, name='edit'),
    path('delete/<int:id>/', views.delete_job, name='delete'),
]