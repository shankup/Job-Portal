# Generated by Django 5.0 on 2024-02-16 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='image',
        ),
    ]
