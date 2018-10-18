from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render

# Create your views here.
def hood(request):
    return render(request,'index.html')
