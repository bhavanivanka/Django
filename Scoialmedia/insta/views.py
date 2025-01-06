from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from insta.models import *

# Create your views here.
def home(request):
    objs=Feed.objects.all()
    return render(request,'index.html',{'posts':objs})


@login_required(login_url="/admin")
def create(request):
    if request.method=="POST":
        image=request.FILES.get('img')
        capt=request.POST.get('cap')
        obj=Feed(user=request.user,pic=image,caption=capt)
        obj.save()
    return render(request,'create.html')
