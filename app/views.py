from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def topic_model(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'topic_model.html',d)

def webpage(request):
    WTO=Webpage.objects.all()
    WTO=Webpage.objects.filter(topic_name='Cricket')
    WTO=Webpage.objects.exclude(topic_name='Cricket')
    WTO=Webpage.objects.all()[1:3:]
    WTO=Webpage.objects.all().order_by('name')
    WTO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    WTO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    WTO=Webpage.objects.all().order_by(Length('name'))
    WTO=Webpage.objects.all().order_by(Length('name').desc())
    d={'WTO':WTO}
    return render(request,'webpage.html',d)

def accessRecords(request):
    ATO=AccessRecords.objects.all()
    d={'ATO':ATO}
    return render(request,'accessRecords.html',d)
