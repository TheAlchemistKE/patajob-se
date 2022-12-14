# Generated by Django 4.1.2 on 2022-10-30 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('7c6e1d7c-1034-4894-83bc-d42cb91fa989'), primary_key=True, serialize=False)),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('decision_status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Rejected')], default=0)),
                ('decision_date', models.DateTimeField(blank=True, null=True)),
                ('applicant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
