from .models import Project, Issues
from django import forms




class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('assigned_to','company_name', 'title',  'description', 'start_date', 'end_date')
        widgets = {
            'assigned_to': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'title': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'description': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
        }

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
        widgets = {
            'assigned_to': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'project': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'title': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'description': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'status': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'priority': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
            'estimated_time': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),           
        }
 
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
     




