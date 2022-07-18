from django import forms
from ecommerce_app.models import *
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from ecommerce_app.models import User  


class CustomUserCreationForm(UserCreationForm): 
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username) 
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  






class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = ['product', 'user']
        # widgets = {
        #     'process_id': forms.Select(attrs={'class': 'form-control', 'id': 'process_id', 'name': 'process_id'}),
        #     'import_type': forms.Select(attrs={'class': 'form-control', 'id': 'import_type', 'name': 'import_type'}),
        #     'import_path': forms.TextInput(attrs={'class': 'form-control', 'id': 'import_path', 'name': 'import_path'}),
        #     'import_schedule_type': forms.Select(attrs={'class': 'form-control', 'id': 'import_schedule_type', 'name': 'import_schedule_type'}),
        #     'import_schedule': forms.TextInput(attrs={'class': 'form-control', 'id': 'import_schedule', 'name': 'import_schedule'}),
        #     'hostname': forms.TextInput(attrs={'class': 'form-control', 'id': 'hostname', 'name': 'hostname', 'autocomplete': 'off',}),
        #     'import_key_file': forms.FileInput(attrs={'class': 'form-control', 'id': 'import_key_file', 'name': 'key_file', 'onchange':'ValidateKeyFile(this);'}),
        #     'import_cert_file': forms.FileInput(attrs={'class': 'form-control', 'id': 'import_cert_file', 'name': 'cert_file', 'onchange':'ValidateKeyFile(this);'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'name': 'password','autocomplete': 'off',}),
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'name': 'username', 'autocomplete': 'off',}),
        # }
    
