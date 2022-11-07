from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Placeone


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    objone=Placeone.objects.all()
    return render(request,"index.html",{'result':obj,'resultone':objone})

# def about(request):
#      return render(request,"about.html")