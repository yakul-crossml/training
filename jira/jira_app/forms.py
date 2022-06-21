from .models import Project, Issues
from django import forms




class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('assigned_to','company_name', 'title',  'description', 'start_date', 'end_date')

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date:
            if not start_date:
                raise forms.ValidationError("Start date not entered.")
        
        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date should be greater than start date.")



class IssuesForm(forms.ModelForm):

    class Meta:
        model = Issues
        fields = ('assigned_to','project', 'title', 'description', 'status', 'priority','start_date', 'end_date', 'estimated_time')
 
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

 
        if end_date:
            if not start_date:
                raise forms.ValidationError("Start date not entered.")
        
        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date should be greater than start date.")
     




