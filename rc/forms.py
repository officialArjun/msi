from django import forms
from . models import user_register_model
#register form
class user_register_form(forms.Form):
    form_username=forms.CharField(widget=forms.TextInput(),max_length=30)
    form_firstname=forms.CharField(widget=forms.TextInput(),max_length=30)
    form_lastname=forms.CharField(widget=forms.TextInput(),max_length=30)
    form_email=forms.EmailField(widget=forms.EmailInput())
    form_phone=forms.CharField(widget=forms.TextInput())
    form_pass1=forms.CharField(widget=forms.PasswordInput())
    form_pass2=forms.CharField(widget=forms.PasswordInput())
    
    
    #username Validation
    def clean_form_username(self):
        username=self.cleaned_data['form_username']
        if user_register_model.objects.filter(model_username=username):
            raise forms.ValidationError('username already exists')
    
    #email validation
    def clean_form_email(self):
        email=self.cleaned_data['form_email']
        if user_register_model.objects.filter(model_email=email):
            raise forms.ValidationError('Email Already Taken')

    
    #password validation
    def clean_form_pass2(self):
        pass1=self.cleaned_data['form_pass1']
        pass2=self.cleaned_data['form_pass2']
        if pass1==pass2:
            if len(pass2)<8:
                raise forms.ValidationError('Password must be of 8 Characters')
            if pass2.isdigit():
                raise forms.ValidationError('Password can\'t of numbers only')
            if pass2.isalpha():
                raise forms.ValidationError('Password Must be Alpha numeric!')
        else:
            raise forms.ValidationError('Password Doesn\'t match')
        
    #phone validaton
    def clean_form_phone(self):
        phone=self.cleaned_data['form_phone']
        if phone.isdigit():

            if len(phone)<10:
                raise forms.ValidationError('Mobile number must be of 10 digits')
            if len(phone)>10:
                raise forms.ValidationError('Mobile number must be of 10 digits')    
        else:
            raise forms.ValidationError('Enter valid mobile number')
        if user_register_model.objects.filter(model_phone=phone):
            raise forms.ValidationError('Phone number Already used')
#login form

class user_login_form(forms.Form):
    form_login_email=forms.EmailField(widget=forms.EmailInput())
    form_login_password=forms.CharField(widget=forms.PasswordInput())
    


#search user using email

class search_user(forms.Form):
    search_email=forms.EmailField(widget=forms.EmailInput())
