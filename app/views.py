from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def Insert_topic(request):
    tn=input('enter the topic name')
    TO=Topic.objects.create(topic_name=tn)
    TO.save()
    return HttpResponse('inserted data sucessfully')
def Insert_Webobj(request):
    tn=Topic.objects.get_or_create(topic_name='cricket')[0]
    pname=input('enter palyer name')
    purl=input('enter player url')
    WO=WebPage.objects.get_or_create(topic_name=tn,p_name=pname,p_url=purl)[0]
    WO.save()
    return HttpResponse('data inserted into webpage sucessfully')
def Insert_AccessRecord(request):
    # #tn=Topic.objects.get_or_create(topic_name='kabbadi')[0]
    # #pname=input('enter palyer name')
    # #purl=input('enter player url')
    # WO=WebPage.objects.get_or_create(p_name='shiva')[0]
    # pauther=input('enter auther')
    # pdate=input('enter the date')
    # AO=AccessRecord.objects.get_or_create(p_name=WO,auther=pauther,date=pdate)[0]
    # AO.save()
    TO=Topic.objects.get_or_create(topic_name='vollyball')[0]
    TO.save()
    pname=input('enter palyer name')
    purl=input('enter url')
    WO=WebPage.objects.get_or_create(p_name=pname,topic_name=TO,p_url=purl)[0]
    WO.save()
    WO1=WebPage.objects.get_or_create(p_name='arjun')[0]
    pauther=input('enter auther')
    pdate=input('enter date')
    AO=AccessRecord.objects.get_or_create(p_name=WO1,auther=pauther,date=pdate)[0]
    AO.save()

    return HttpResponse('inserted data sucesssfully in access recordram')

def display_topic(request):
    TO=Topic.objects.all()
    TO=Topic.objects.filter(topic_name='cricket')
    d={'topics':TO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    WO=WebPage.objects.all()
    TO=Topic.objects.filter(topic_name='cricket')
    WO=WebPage.objects.filter(topic_name=TO)
    d={'webtopics':WO}
    return render(request,'display_webtopics.html',d)
    