from django.shortcuts import render
from django.http import HttpResponse
#from .models import Candidate
# Create your views here.
def index(request):
    #candidates = Candidate.objects.all()
    return render(request,'mainpg1/index.html')
#def placelist(request):
#    return render(request,'')
