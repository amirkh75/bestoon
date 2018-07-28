# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from web.models import User , Token , Expensee , income

@csrf_exempt
def submit_expense(request):
    """user submits and expense"""
#TODO:
    now = datetime.now( )
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    Expensee.objects.create(user = this_user,amount=request.POST['amount'],
    title = request.POST['title'], date=now)
    print request.POST
    return JsonResponse({
        'status' : 'ok'
        }, encoder=JSONEncoder)
