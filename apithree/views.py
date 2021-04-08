from django.shortcuts import render
from time import time, timezone
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import json
import datetime
from datetime import date, timedelta
from datetimerange import DateTimeRange
# Create your views here.
def apithree(request,start_date,end_date):
    response=requests.get('https://gitlab.com/-/snippets/2094509/raw/master/sample_json_3.json')
    data=response.json()
    data_=json.dumps(data)
    time_range_2 = DateTimeRange(start_date, end_date)
    all_date=[]
    
    for value in time_range_2.range(datetime.timedelta(minutes=1)):
        (all_date.append(str(value.date())+' '+str(value.time())))
    
    new_data=[]
    for d in data:
        if d['time'] in all_date:
            if d['state']==False:
                d['id']=int(d['id'][d['id'].index('0')+1:])
                d['belt2']=0
                new_data.append(d)
    
            if d['state']==True:
                d['belt1']=0
                d['id']=int(d['id'][d['id'].index('0')+1:])
                new_data.append(d)
                
                
    v={}
    for i in new_data:
        v[i['id']]=0

    for i in new_data:
        if i['id'] in v.keys():
            v[i['id']]+=i['belt1']
            v[i['id']]+=i['belt2']
    print(v)
    s={}
    for i in new_data:
        s[i['id']]=0
    for i in new_data:
        if i['id'] in s.keys():
            s[i['id']]+=1
            # v[i['id']]+=1
    print(s)
    
    for i in v:
        if i in s:
            v[i]=(v[i]//s[i])
    print(v)
    
    for i in new_data:
        if i['id'] in v:
            if i['belt1'] !=0:
                i['belt1']=v[i['id']]
    # print(new_data)
            if i['belt2'] !=0:
                i['belt2']=v[i['id']]
    for i in new_data:
        print(i)
    result_output=[]
    seen=set()
    for i in new_data:
        if i['id'] not in seen:
            seen.add(i['id'])
            result_output.append(i)
    
    for i in result_output:
        i.pop('time')
        i.pop('state')
        i['avg_belt1']=i.pop('belt1')
        i['avg_belt2']=i.pop('belt2')
    
    result_output.sort(key=lambda k : k['id'])
    # print(result_output)
    return JsonResponse(result_output,safe=False)