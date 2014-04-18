#! /usr/bin/env python
#coding=utf-8
from django.http import Http404,HttpResponse
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response,render
import datetime
def hello(request):
    return HttpResponse('Hello Tongtong Liu!')
def current_time(request):
    now = datetime.datetime.now()
    return render_to_response('current_time.html',{'current_time':now})
def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In {0} hours, it will be {1}.</body></html>'.format(offset,dt)
    return HttpResponse(html)
def thanks(request):
    return render(request,'thanks.html')
    