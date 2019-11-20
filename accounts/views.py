from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model

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