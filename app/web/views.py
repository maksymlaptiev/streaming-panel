from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from app import settings
from datetime import *
from models.models import *
import requests
# Create your views here.
data={"sitename":"CDN","date":"2020","rooturl":settings.ROOT_URL}


def index(request):
    #streams=Stream.objects.count()
    #channels=Channel.objects.count()
    #data['streams']=streams
    #data['channels']=channels
    streamdata={}
    streams= Stream.objects.all()
    streamdata['streams']=streams
    print(streamdata)
    return render(request, 'web/index.html', streamdata)

@csrf_exempt
def on_publish(request):
    print(request.POST)
    name=request.POST['name']
    type=request.POST['type']
    addr=request.POST['addr']
    status=1
    streamavailable = None
    try:
        streamavailable=Stream.objects.get(name=name)
    except Exception as ex:
        print(ex)
    if streamavailable !=None:
        streamavailable.lastpubdate=datetime.now()
        streamavailable.status=status
        streamavailable.save()
    else:
        streams=Stream.objects.create(name=name,type=type,address=addr,status=status,lastpubdate=datetime.now(),createdate=datetime.now())
    try:
        url="http://www.masjidnalive.com/MosqueAppStaging/api/Broadcast/StreamingStarted"
        data={"name":name,"type":type,"address":addr,"status":1,"message":"stream started"}
        headers={"Content-Type":"application/json"}
        res = requests.post(url,json=data,headers=headers)
        print(res.content)
        print("sent started")
    except Exception as ex:
        print(ex)
    return HttpResponse("OK")

@csrf_exempt
def on_publish_done(request):
    print(request.POST)
    name=request.POST['name']
    addr=request.POST['addr']
    status=0
    streamavailable = None
    try:
        streamavailable=Stream.objects.get(name=name)
    except Exception as ex:
        print(ex)
    if streamavailable !=None:
        streamavailable.status=status
        streamavailable.save()
    try:
        url="http://www.masjidnalive.com/MosqueAppStaging/api/Broadcast/StreamingStopped"
        data={"name":name,"address":addr,"status":0,"message":"stream stopped"}
        headers={"Content-Type":"application/json"}
        res = requests.post(url,json=data,headers=headers)
        print(res.content)
    except Exception as ex:
        print(ex)
    return HttpResponse("OK")

@csrf_exempt
def record_done(request):
    print(request.POST)
    return HttpResponse("OK")
