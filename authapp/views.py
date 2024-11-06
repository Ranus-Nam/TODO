from django.shortcuts import render,redirect, HttpResponse
from.models import *
from django.contrib.auth.forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirict('todoapp:todo_list')
    else:
        initial_data = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial = initial_data)
    return render (request, 'auth/register.html',{'form':form})

def login_view(request):    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('todoapp:todo_list')
    else:
        initial_data = {'username':'','password':''}
        form = AuthenticationForm(initial = initial_data)
    # return render (request, 'auth/register.html',{'form':form})
    return render(request, 'auth/login.html',{'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
    
@login_required
def dashboard_view(request):
    return redirect('todoapp:todo_list')
