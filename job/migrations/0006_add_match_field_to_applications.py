# Generated by Django 4.1.2 on 2022-10-31 08:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.UUIDField(default=uuid.UUID('90811502-1e3b-41a8-8930-c409d944c043'), editable=False, primary_key=True, serialize=False),
        ),
    ]
