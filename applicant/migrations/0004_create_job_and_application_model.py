# Generated by Django 4.1.2 on 2022-10-30 10:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0003_Create_company_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bd1dadb1-3e08-4f0a-8666-4409583cee9b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
