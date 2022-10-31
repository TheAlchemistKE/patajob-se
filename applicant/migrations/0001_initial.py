# Generated by Django 4.1.2 on 2022-10-30 10:09

from django.conf import settings
import django.contrib.postgres.fields
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
            name='Applicant',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('c40c0121-5be3-43a6-9461-ab479176fb75'), editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=200)),
                ('headshot', models.FileField(null=True, upload_to='headshots/')),
                ('resume', models.FileField(null=True, upload_to='resumes/')),
                ('job_title', models.CharField(max_length=200)),
                ('social_media', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('portfolio', models.URLField()),
                ('about', models.TextField()),
                ('technical_skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('soft_skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('joined_date', models.DateTimeField(auto_now=True, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Applicants',
            },
        ),
    ]