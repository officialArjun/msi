from django.shortcuts import render,redirect
from .forms import *
from .models import user_register_model
from django.contrib.auth import login,logout,user_logged_in,user_logged_out,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session,SessionManager

#index
def index(request):
    return render(request,'rc/index.html')

#register
def register(request):
    if request.method=='POST':
        form_ob=user_register_form(request.POST)
        if form_ob.is_valid():
            newuser=user_register_model(model_username=request.POST['form_username'],model_firstname=request.POST['form_firstname'],model_lastname=request.POST['form_lastname'],model_email=request.POST['form_email'],model_password=request.POST['form_pass2'],model_phone=request.POST['form_phone'])
            newuser.save()
            return redirect('login')
    else:

        form_ob=user_register_form()
    context={'form_ob':form_ob}
    return render(request,'rc/register.html',context)

#login

def user_login(request):
    if request.method=='POST':
        form_ob=user_login_form(request.POST)
        if form_ob.is_valid():
            login_pass=request.POST['form_login_password']
            if user_register_model.objects.filter(model_email=request.POST['form_login_email']):
                db=user_register_model.objects.get(model_email=request.POST['form_login_email'])
                if login_pass == db.model_password:
                    user=request.POST['form_login_email']
                    login(request,user)
                    
                    
                    return redirect('p1')

                    
                
                else:
                    raise forms.ValidationError('Your entered wrong password')    
            else:
                raise forms.ValidationError('Account is not exists')    
    else:
        form_ob=user_login_form()
    context={"form_ob":form_ob}
    return render(request,'rc/login.html',context)

#p1
@login_required
def p1(request):
    if request.method=='POST':
        form_ob=search_user(request.POST)
        if form_ob.is_valid():
            model_ob=user_register_model.objects.get(model_email=request.POST['search_email'])
    else:

        form_ob=search_user()
        model_ob=user_register_model()
    
    
    context={'form_ob':form_ob,'model_ob':model_ob}

    return render(request,'rc/p1.html',context)

#logout
def user_logout(request):
    if request.method=='POST':
        logout(request)
    
    return render(request,'rc/p1.html')