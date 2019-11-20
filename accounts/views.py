from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users':users
    }
    return render(request,'accounts/index.html',context)

def detail(request,user_pk):
    user = get_object_or_404(get_user_model(),id=user_pk)

    return  render(request,'accounts/detail.html',{'user':user})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    
    return render(request,'accounts/form.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)

        if form.is_valid():
            auth_login(request,form.get_user())

            return redirect('/accounts')
    else:
        form = AuthenticationForm()
    
    return render(request,'accounts/form.html',{'form':form})
