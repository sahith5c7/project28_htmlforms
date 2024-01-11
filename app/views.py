from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def htmlforms(request):
    if request.method=='POST':
        username=request.POST['un']
        return HttpResponse(username)
    return render(request,'htmlforms.html')

def createschool(request):
    if request.method=='POST':
        sn=request.POST['sn']
        sl=request.POST.get('sl')
        sp=request.POST.get('sp')

        SO = School.objects.get_or_create(Sname=sn,Slocation=sl,Sprincipal=sp)[0]
        SO.save()
        
        return HttpResponse('School data inserted Successfully')
    return render(request,'createschool.html')


