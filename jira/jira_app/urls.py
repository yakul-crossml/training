from django.contrib import admin
from django.urls import path, include
from jira_app.views import *

urlpatterns = [
    path('', Dashboard.as_view(), name="dasboard"),
    path('projects/', Projects.as_view(), name="projects"),
    path('issues/', Issues_fun.as_view(), name="issues"),
    path('projectjson', ProjectsListJson.as_view(), name="projects_list"),
    path('issuesjson', IssuesListJson.as_view(), name="issues_list"),
    path('issuesjsonlast', IssuesListJsonlast.as_view(), name="issues_list_last"),
]
