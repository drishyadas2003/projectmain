from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def home(request):
    
    
    return render(request,'home.html',)  


def blog(request):
    
    return render(request,'blog.html',)



def softwareblog(request):
    
    return render(request,'softwareblog.html',)


def cloudblog(request):
    
    return render(request,'cloudblog.html',)



def digitalmarketing(request):
    
    return render(request,'digitalmarketing.html',)



def carrers(request):
    
    return render(request,'carrers.html',)


def webdesigner(request):
    
    return render(request,'webdesigner.html',)

def seniordeveloper(request):
    
    return render(request,'seniordeveloper.html',)



def courses(request):
    cou=Course.objects.all()
    
    context={'cou':cou}
    return render(request,'courses.html',context)




def aboutus(request):
    
    return render(request,'aboutus.html',)


def placements(request):
    place=Placement.objects.all()
    
    
    context={'place':place}
    return render(request,'placements.html',context)



def contactus(request):
    
    return render(request,'contactus.html',)




def success(request):
    suc=Success.objects.all()
    
    context={'suc':suc}
    return render(request,'success.html',context)




def coursedigital(request):
    cou=Course.objects.all()
    
    context={'cou':cou}
    return render(request,'coursedigital.html',context)


def vmsphere(request):
    
    return render(request,'vmsphere.html',)


def wsa(request):
    
    return render(request,'wsa.html',)

def ciso(request):
    
    return render(request,'ciso.html',)

def az(request):
    
    return render(request,'az.html',)

def compa(request):
    
    return render(request,'compa.html',)

def compnet(request):
    
    return render(request,'compnet.html',)

def phpfullstack(request):
    
    return render(request,'phpfullstack.html',)

def pythonfullstack(request):
    
    return render(request,'pythonfullstack.html',)

def redhat(request):
    
    return render(request,'redhat.html',)


def aws(request):
     
     return render(request,'aws.html',)