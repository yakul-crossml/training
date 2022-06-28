from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    assigned_to=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=100)
    title = models.CharField(max_length=50, verbose_name='Title of Project')
    description = models.TextField(max_length=100, verbose_name='Description of Project')
    start_date = models.DateTimeField(verbose_name='Start Date of Project',null=True, blank=True)
    end_date = models.DateTimeField(verbose_name='End Date of Project',null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='Updated', auto_now=True,null=True)

    def __str__(self):
        return self.title

STATUS = (
('pending','Pending'),
('inprogess','Inprogess'),
('completed', 'completed'),
)
PRIORITY = (
('high','High'),
('low','low'),
)


class Issues(models.Model):
    assigned_to=models.ForeignKey(User, on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    status=models.CharField(max_length=100, choices=STATUS)
    title=models.CharField(max_length=100)
    description = models.TextField(max_length=100, verbose_name='Description of Task')
    priority = models.CharField(max_length=100, choices=PRIORITY)
    start_date = models.DateTimeField(verbose_name='Start Date of Task',null=True, blank=True)
    end_date = models.DateTimeField(verbose_name='End Date of Task',null=True, blank=True)    
    estimated_time =models.CharField(max_length=7, null=True, blank=True)
    file_upload = models.FileField(upload_to ='media', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='Updated', auto_now=True,null=True)

    def __str__(self):
        return self.title
