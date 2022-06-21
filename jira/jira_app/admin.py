from django.contrib import admin
from jira_app.models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(Issues)
