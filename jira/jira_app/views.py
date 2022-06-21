from django.shortcuts import render
from django.views import View
from jira_app.forms import IssuesForm, ProjectForm
from django.contrib.auth.models import User
from django_datatables_view.base_datatable_view import BaseDatatableView
from jira_app.models import *
from django.utils.html import escape
from django.http import JsonResponse

# Create your views here.
class Dashboard(View):
    template_name = 'dashboard.html'
    
    def get(self, request, *args, **kwargs):
        project_form=ProjectForm()
        return render(request,
                      self.template_name,
                      {
                'project_form': project_form, 
            }
                     )
    def post(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                     )



class Projects(View):
    template_name = 'projects.html'
    
    def get(self, request, *args, **kwargs):
        project_form=ProjectForm()
        users=User.objects.all()
        return render(request,
                      self.template_name,
                      {
                'project_form': project_form,
                'users':users 
            }
                     )
    def post(self, request, *args, **kwargs):
        project_form=ProjectForm(request.POST)
        project_form.save()

        return render(request,
                      self.template_name,
                      {
                      "project_form":project_form
                      }
                     )


                     
class Issues_fun(View):
    template_name = 'issues.html'
    
    def get(self, request, *args, **kwargs):
        Issues_form=IssuesForm()
        if request.GET.get('project_id'):
            return render(request,
                      self.template_name,
                      {
                'issues_form': Issues_form, 
                'abc':"abc"
            }
            )
        return render(request,
                      self.template_name,
                      {
                'issues_form': Issues_form, 
            }
                     )
    def post(self, request, *args, **kwargs):
        issues_form=IssuesForm(request.POST)
        issues_form.save()
        return render(request,
                      self.template_name,
                     )


class ProjectsListJson(BaseDatatableView):
    model = Project
    columns =['title', 'description', 'status', 'assigned_to', 'start_date', 'end_date','issues']
    order_columns =['title', 'description', 'status', 'assigned_to', 'start_date', 'end_date', 'issues']
   
    max_display_length = 10
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
    
        if search:        
            qs = qs.filter(company_name__istartswith=search) or qs.filter(title__istartswith=search) or qs.filter(description__istartswith=search)
        return qs

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'issues':
            # escape HTML for security reasons
            return ('<form action="/issues" id=iissue> <button type="submit" name="project_id" value="{0}" class="btn btn-primary">Add Issues</button> </form>').format(row.id)
        else:
            return super(ProjectsListJson, self).render_column(row, column)
    
    def get_initial_queryset(self):        
        return Project.objects.all()



class IssuesListJson(BaseDatatableView):
    model = Issues
    columns =['project.title', 'description', 'status', 'assigned_to', 'title','priority','estimated_time' ,'start_date', 'end_date']
    order_columns =['project.title', 'description', 'status', 'assigned_to', 'title','priority','estimated_time' ,'start_date', 'end_date']
   
    max_display_length = 10
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
    
        if search:
            qs = qs.filter(project__title__istartswith=search) or qs.filter(title__istartswith=search) or qs.filter(description__istartswith=search)
        return qs
    
    def get_initial_queryset(self):
        return Issues.objects.all()


class IssuesListJsonlast(BaseDatatableView):
    model = Issues
    columns =['project.title', 'description', 'status', 'assigned_to', 'title','priority','estimated_time' ,'start_date', 'end_date']
    order_columns =['project.title', 'description', 'status', 'assigned_to', 'title','priority','estimated_time' ,'start_date', 'end_date']
   
    max_display_length = 10
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
    
        if search:        
            qs = qs.filter(project__title__istartswith=search) or qs.filter(title__istartswith=search) or qs.filter(description__istartswith=search)
        return qs
    
    def get_initial_queryset(self):
        return Issues.objects.all()