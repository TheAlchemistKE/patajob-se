# Generated by Django 4.1.2 on 2022-10-30 12:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_application_job_id_alter_application_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ce7d0226-9304-42f5-b77f-71b138773293'), primary_key=True, serialize=False),
        ),
    ]
