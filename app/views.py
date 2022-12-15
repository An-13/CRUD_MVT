from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

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
    WTO=Webpage.objects.filter(name__startswith='m')
    WTO=Webpage.objects.filter(name__endswith='d')
    WTO=Webpage.objects.filter(name__contains='s')
    WTO=Webpage.objects.filter(name__in=('Kholhi','MSD'))
    WTO=Webpage.objects.filter(name__regex='^M\w{2}')
    WTO=Webpage.objects.all()
    WTO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name__startswith='k'))
    WTO=Webpage.objects.all()
    WTO=Webpage.objects.filter(Q(topic_name='Football') | Q(url__endswith='com'))
    WTO=Webpage.objects.all()
    d={'WTO':WTO}
    return render(request,'webpage.html',d)

def accessRecords(request):
    ATO=AccessRecords.objects.all()
    ATO=AccessRecords.objects.filter(date='1998-04-13')
    ATO=AccessRecords.objects.filter(date__year='2022')
    ATO=AccessRecords.objects.filter(date__month='1')
    ATO=AccessRecords.objects.filter(date__day='15')
    ATO=AccessRecords.objects.filter(date__gte='1989-11-01')
    ATO=AccessRecords.objects.filter(date__lte='1993-11-01')
    ATO=AccessRecords.objects.filter(date__year__gte='1998')
    d={'ATO':ATO}
    return render(request,'accessRecords.html',d)
