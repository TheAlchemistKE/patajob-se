# Generated by Django 4.1.2 on 2022-10-31 09:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_add_match_field_to_applications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6125ea41-0885-4824-af8d-402aae60f415'), primary_key=True, serialize=False),
        ),
    ]
