# Generated by Django 4.1.2 on 2022-10-30 10:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_Create_company_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a5781ccb-b748-46ac-87d9-534d5265ac29'), editable=False, primary_key=True, serialize=False),
        ),
    ]
