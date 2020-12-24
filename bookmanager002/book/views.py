from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from book.models import BookInfo,PeopleInfo

def index(request):
    return HttpResponse('cuitingting')

BookInfo.objects.all()

# 增加数据
from book.models import BookInfo
book=BookInfo()
book.name='python'
book.readcount=20
book.commentcount=200
book.pub_date='2020-12-25'

book.save()

new_book=BookInfo.objects.create(
    name='python',
    pub_date='2020-12-25',
    readcount=20,
    commentcount=200
)








