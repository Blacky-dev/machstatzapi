from django.shortcuts import render
from django.shortcuts import render
from time import time, timezone
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import datetime
from datetime import date, timedelta
from datetimerange import DateTimeRange
# Create your views here.


def apithree(request,start_date,end_date):
    response=requests.get('https://gitlab.com/-/snippets/2094509/raw/master/sample_json_2.json')
    all_data=response.json()
    time_range_2 = DateTimeRange(start_date, end_date)
    all_date=[]
    for value in time_range_2.range(datetime.timedelta(minutes=1)):
        (all_date.append(str(value.date())+' '+str(value.time())))
    
    time_sets=set()
    for i in all_date:
        time_sets.add(i)
    
    runtime=0
    downtime=0
    
    
    for data in all_data:
        if data['time'] in time_sets:
            if data['runtime']<=1021:
                runtime+=data['runtime']
            if data['runtime']>1021:
                evaluated_downtime=data['runtime']-1021
                downtime+=evaluated_downtime
                runtime+=1021
    # print(runtime,downtime)
    total_runtime=round(((runtime)/(runtime+downtime))*100,2)
    # conversion on runtime and downtime seconds to hh:mm:ss
    
    minute, sec = divmod(runtime, 60)
    hour, minute = divmod(minute, 60)
    runtime=("%dh:%02dm:%02ds" % (hour, minute, sec))
    
    minute, sec = divmod(downtime, 60)
    hour, minute = divmod(minute, 60)
    downtime=("%dh:%02dm:%02ds" % (hour, minute, sec))
    # =====================================================
    result={'runtime':runtime,'downtime':downtime,'utilization':total_runtime}
    print(result)
    
    return JsonResponse(result,safe=False)