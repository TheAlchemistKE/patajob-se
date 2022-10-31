from django.urls import path
from . import views

urlpatterns = [
    path('', views.details, name='company_profile'),
    path('job-openings/', views.index, name='company_job_openings'),
]