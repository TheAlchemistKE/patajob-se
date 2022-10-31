import uuid

from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    name = models.CharField(max_length=150)
    description = models.TextField()
    established_date = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    logo = models.FileField(upload_to='logos/', null=True)
    corporation_type = models.CharField(max_length=150)
    company_size = models.IntegerField()
    website = models.URLField(max_length=200, default="https://example.com/")
    reddit = models.URLField(max_length=200, default="https://reddit.com/r/")
    twitter = models.URLField(max_length=200, default="https://twitter.com/")
    facebook = models.URLField(max_length=200, default="https://facebook.com/")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'companies'
        verbose_name_plural = 'companies'
