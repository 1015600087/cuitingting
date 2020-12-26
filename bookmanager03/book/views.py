from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse('OK')

def book(request,cat_id,detail_id):
    # print(cat_id,detail_id)

    query_string=request.GET
    # print(query_string)
    # a=query_string['a']
    # b=query_string.get('b')
    # print(a,b)

    alist=query_string.getlist('a')
    b=query_string.get('b')
    print(alist,b)

    return HttpResponse('我喜欢读书')

def login(request):
    body=request.POST
    print(body)
    return HttpResponse('login')

def weibo(request):
    body=request.body
    body_str=body.decode()
    print(body_str)
    import json
    data=json.loads(body)
    return HttpResponse('weibo json')




