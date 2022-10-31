import uuid

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Applicant(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    fullname = models.CharField(max_length=200)
    headshot = models.FileField(upload_to='headshots/', null=True)
    resume = models.FileField(upload_to='resumes/', null=True)
    job_title = models.CharField(max_length=200)
    social_media = models.URLField(null=True)
    portfolio = models.URLField(null=True)
    about = models.TextField(null=True)
    technical_skills = ArrayField(models.CharField(max_length=200), default=list)
    soft_skills = ArrayField(models.CharField(max_length=200), default=list)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=False)
    joined_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Applicants'


class ApplicantResumeScore(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    backend_engineer = models.IntegerField()
    software_engineer = models.IntegerField()
    devops_engineer = models.IntegerField()
    data_analyst = models.IntegerField()
    frontend_engineer = models.IntegerField()
    fullstack_engineer = models.IntegerField()
    ui_ux_engineer = models.IntegerField()
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'ApplicantResumeScores'
