# Generated by Django 4.1.2 on 2022-10-30 11:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_id'),
        ('application', '0001_create_job_and_application_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='job_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.job'),
        ),
        migrations.AlterField(
            model_name='application',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4d27ce39-8cff-4d7a-bf67-b94370e8590b'), primary_key=True, serialize=False),
        ),
    ]
