# Generated by Django 4.1.2 on 2022-10-30 12:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=uuid.UUID('49b9f957-2a10-4a09-b35c-bdc92a33f77d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
