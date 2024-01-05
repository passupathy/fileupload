from django.shortcuts import render,redirect
from .forms import good
from.models import honda
from django.contrib import messages
from django.urls import path
import os

# Create your views here.

def home(request):

    mydata=honda.objects.all()

    bad=good()

    if mydata!="":
         context={'ok':bad,'mydata':mydata}
         return render(request,"index.html",context)
         
    else:
         context={'ok':bad}
         return render(request,'index.html',context)

def iload(request):

    if request.method=="POST":
        bad=good(request.POST,request.FILES)

        if bad.is_valid():
            lorry=request.POST.get('car')
            jcb=request.FILES.get('bus')

            exists= honda.objects.filter(shine=jcb).exists()

            if exists:
                messages.error(request," no no")

            else:
                honda.objects.create(uni=lorry,shine=jcb).save()
                messages.success(request," ok uploaded")

        return redirect('home')
    

def delete(request,id):
    
    mydata=honda.objects.get(id=id)
    mydata.delete()
    os.remove(mydata.shine.path)
    messages.success(request," ok dleted")
    return redirect('home')
        

