from django.shortcuts import render
from django.http import HttpResponse
from .models import Travel
#from .models import Candidate
# Create your views here.
def index(request):
    travels=Travel.objects.all()
    return render(request,'traveler/index.html',{'travels':travels})
def dangjinindex(request):
    travels=Travel.objects.filter(local='당진')
    return render(request,'traveler/index.html',{'travels':travels})
def incheonindex(request):
    travels=Travel.objects.filter(local='인천')
    return render(request,'traveler/index.html',{'travels':travels})
def pajuindex(request):
    travels=Travel.objects.filter(local='파주')
    return render(request,'traveler/index.html',{'travels':travels})
def yangpyeongindex(request):
    travels=Travel.objects.filter(local='양평')
    return render(request,'traveler/index.html',{'travels':travels})
def asanindex(request):
    travels=Travel.objects.filter(local='아산')
    return render(request,'traveler/index.html',{'travels':travels})
def andongindex(request):
    travels=Travel.objects.filter(local='안동')
    return render(request,'traveler/index.html',{'travels':travels})
def findlocalindex(request):
    return render(request,'traveler/findlocalss.html',{})
#def placelist(request):
#    return render(request,'')
