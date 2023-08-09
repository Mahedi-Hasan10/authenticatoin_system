from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib import messages
from firstapp.forms import RegisterForm,ChangeData


# Create your views here.
def home(request):
    return render(request,'home.html') 

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Successfully registered")
                return redirect('homepage')
        else:
            form = RegisterForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('profile')
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password'] 
                user = authenticate(username = name, password = userpass)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeData(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,"Account updated succesfully")
                return redirect('homepage')
        else:
            form = ChangeData(instance=request.user)
        return render(request,'profile.html',{'form':form})
    else:
        return redirect('login')
    
def userlogout(request):
    logout(request)
    return redirect('login')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Successfully password changed")
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')
    

def change_pass2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Successfully password changed")
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request,'passchange2.html',{'form':form})
    else:
        return redirect('login')