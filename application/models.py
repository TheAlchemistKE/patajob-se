import uuid
from django.db import models
from django.contrib.auth.models import User

from job.models import Job

# from job.models import Job

# Create your models here.

APPLICATION_STATUS = (
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Rejected'),

)


class Application(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4())
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    applicant_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=False)
    applied_date = models.DateTimeField(auto_now_add=True)
    applicant_match_score = models.IntegerField(default=0)
    decision_status = models.IntegerField(choices=APPLICATION_STATUS, default=0)
    decision_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.applicant_id.email
