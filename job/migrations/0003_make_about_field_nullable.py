# Generated by Django 4.1.2 on 2022-10-30 12:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3f49336b-a331-4955-b254-903312c6a802'), editable=False, primary_key=True, serialize=False),
        ),
    ]
