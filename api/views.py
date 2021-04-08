from time import time, timezone
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import json
import datetime
from datetime import date, timedelta
from datetimerange import DateTimeRange
# Create your views here.
def index(request,start_date,end_date):
    response=requests.get('https://gitlab.com/-/snippets/2094509/raw/master/sample_json_1.json')
    data=response.json()
    data_=json.dumps(data)
    
    time_range_2 = DateTimeRange(start_date, end_date)
    all_date=[]
    
    for value in time_range_2.range(datetime.timedelta(minutes=1)):
        (all_date.append(str(value.date())+' '+str(value.time())))
    # print(all_date)
    shiftA=[]
    shiftB=[]
    shiftC=[]
    shift1=DateTimeRange(start_date[:start_date.index('T')]+' '+'06:00', start_date[:start_date.index('T')]+' '+'14:00')
    for i in shift1.range(datetime.timedelta(minutes=1)):
        shiftA.append(str(i.date())+' '+str(i.time()))
   
    shift2=DateTimeRange(start_date[:start_date.index('T')]+' '+'14:00', start_date[:start_date.index('T')]+' '+'20:00')
    for i in shift2.range(datetime.timedelta(minutes=1)):
        shiftB.append(str(i.date())+' '+str(i.time()))
    shift3=DateTimeRange(start_date[:start_date.index('T')]+' '+'20:00', start_date[:start_date.index('T')]+' '+'23:59')
    # print(shift3)
    for i in shift3.range(datetime.timedelta(minutes=1)):
        shiftC.append(str(i.date())+' '+str(i.time()))
        
    shift3=DateTimeRange(end_date[:end_date.index('T')]+' '+'00:00', end_date[:end_date.index('T')]+' '+'06:00')
    # print(shift3)
    for i in shift3.range(datetime.timedelta(minutes=1)):
        shiftC.append(str(i.date())+' '+str(i.time()))
    # print(shiftC)
    res={}
    count_prodA=0
    count_prodB=0 
    for i in data:
        if i['time'] in all_date:
            if i['time'] in shiftA:
                if i['production_A']==True:
                    # print(i)
                    count_prodA+=1
    
    
      
    for i in data:
        if i['time'] in all_date:
            if i['time'] in shiftA:
                if i['production_B']==True:
                    # print(i)
                    count_prodB+=1
 
    res['shiftA']={'production_A_count':count_prodA,'production_B_count':count_prodB,}
    # print(res)
    count_prodA=0
    count_prodB=0 
    for i in data:
        if i['time'] in all_date:
            if i['time'] in shiftB:
                if i['production_A']==True:
                    # print(i)
                    count_prodA+=1
    # print(count)
      
    for i in data:
        if i['time'] in all_date:
            if i['time'] in shiftB:
                if i['production_B']==True:
                    # print(i)
                    count_prodB+=1
    # print(count)
    res['shiftB']={'production_A_count':count_prodA,'production_B_count':count_prodB,}
    
    # print(shiftC)
    count_prodA=0
    count_prodB=0 
    for i in data:
        if i['time'] in all_date:
            if i['time'] in shiftC:
                if i['production_A']==True:
                    # print(i)
                    
                    count_prodA+=1
    # print(count)
 
    # print(shiftC)
    print('==============') 
    for i in data:
        if i['time'] in all_date:
            if i['time'] in shiftC:
                
                if i['production_B']==True:
                    # print(i)
                    count_prodB+=1
    # print(count)
    res['shiftC']={'production_A_count':count_prodA,'production_B_count':count_prodB,}
    # print(res)
    return JsonResponse(res,safe=False)