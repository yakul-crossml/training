# Generated by Django 4.0.4 on 2022-06-14 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50, verbose_name='Title of Project')),
                ('description', models.TextField(max_length=100, verbose_name='Description of Project')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Date of Project')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date of Project')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('inprogess', 'Inprogess'), ('completed', 'completed')], max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100, verbose_name='Description of Task')),
                ('priority', models.CharField(choices=[('high', 'High'), ('low', 'low')], max_length=100)),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Date of Task')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date of Task')),
                ('estimated_time', models.CharField(blank=True, max_length=7, null=True)),
                ('file_upload', models.FileField(blank=True, null=True, upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jira_app.project')),
            ],
        ),
    ]
