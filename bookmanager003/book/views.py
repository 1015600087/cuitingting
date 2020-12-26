from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):

    return HttpResponse('index')

def book(request,cat_id,detail_id):
    # print(cat_id,detail_id)
    query_string=request.GET
    print(query_string)
    # a=query_string['a']
    # b=query_string.get('b')
    # print(a,b)

    alist=query_string.getlist('a')
    b=query_string.get('b')
    print(alist,b)
    return HttpResponse('读书')

def login(request):

    body=request.POST
    print(body)
    return HttpResponse('login')

def weibo(request):

    body=request.body
    body_str=body.decode()
    import json
    data=json.loads(body_str)
    print(data)
    return HttpResponse('weibo json')




