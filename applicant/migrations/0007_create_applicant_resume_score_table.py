# Generated by Django 4.1.2 on 2022-10-30 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0006_make_about_field_nullable'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantResumeScore',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('1d7b7bf2-011f-4cb7-a74b-8c2609595831'), editable=False, primary_key=True, serialize=False)),
                ('backend_engineer', models.IntegerField()),
                ('software_engineer', models.IntegerField()),
                ('devops_engineer', models.IntegerField()),
                ('data_analyst', models.IntegerField()),
                ('frontend_engineer', models.IntegerField()),
                ('fullstack_engineer', models.IntegerField()),
                ('ui_ux_engineer', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'ApplicantResumeScores',
            },
        ),
        migrations.AlterField(
            model_name='applicant',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ce9ad6c6-21d0-4f91-b9c5-4a9298df97bd'), editable=False, primary_key=True, serialize=False),
        ),
    ]