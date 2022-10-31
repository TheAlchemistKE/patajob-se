from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_listing'),
    path('<str:pk>/details/', views.JobDetailView.as_view(), name='job_detail'),
    path('<str:job_id>/apply/', views.apply_to_job, name='apply_to_job'),
    path('<str:job_id>/match/', views.match_insight, name='match_insight')
]
