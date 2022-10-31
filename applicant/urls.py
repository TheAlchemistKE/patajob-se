from django.urls import path
from . import views

urlpatterns = [
    path('', views.details, name='applicant_profile'),
    path('applications/', views.index, name='applicant_job_applications')
]