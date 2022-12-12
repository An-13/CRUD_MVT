from django.shortcuts import render
from app.models import *

# Create your views here.
def topic_model(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'topic_model.html',d)

def webpage(request):
    WTO=Webpage.objects.all()
    d={'WTO':WTO}
    return render(request,'webpage.html',d)

def accessRecords(request):
    ATO=AccessRecords.objects.all()
    d={'ATO':ATO}
    return render(request,'accessRecords.html',d)
