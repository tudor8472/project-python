from django.shortcuts import render, redirect,HttpResponse
from .forms import RegisterForm
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        else:
            return render(response, "register/register_not.html")
        return redirect("/login")
    else:
        form = RegisterForm()
    
    return render(response, "register/register.html", {"form" : form })

def logout(response):
    return render(response,"registration/logout.html")