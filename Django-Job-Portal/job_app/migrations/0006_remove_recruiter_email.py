# Generated by Django 5.0 on 2024-02-20 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0005_recruiter_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiter',
            name='email',
        ),
    ]
