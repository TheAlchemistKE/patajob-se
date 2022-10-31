import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

from company.models import Company


class Job(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    title = models.CharField(max_length=200)
    description = models.TextField()
    role = models.TextField()
    role_entails = models.TextField()
    minimum_salary = models.IntegerField()
    maximum_salary = models.IntegerField()
    work_type = models.CharField(max_length=150)
    career_level = models.CharField(max_length=150)
    technical_skills = ArrayField(models.CharField(max_length=200), default=list)
    soft_skills = ArrayField(models.CharField(max_length=200), default=list)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    belongs_to = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
