from django.shortcuts import render

# Create your views here.

# 定义视图
from django.http import HttpResponse

def index(request):
    context = {'title':'测试模板'}

    # return HttpResponse('cuitingting')
    return render(request,'book/index.html',context)

from book.models import PeopleInfo,BookInfo

# 1.增加数据
# 方法一:
# 通过实例对象
book=BookInfo()
book.name='django3'
book.readcount=100
book.commentcount=200
book.pub_date='2020-12-29'
book.save()
# 方法二:
# 通过create方法增加
new_book=BookInfo.objects.create(
    name='python03',
    readcount=200,
    commentcount=300,
    pub_date='2020-12-29'
)

# 2.更新数据
# 方法一:通过实例对象
book=BookInfo.objects.get(id=14)
book.name='django14'
book.save()

# 方法二:
# 直接更新用update方法
BookInfo.objects.filter(id=14).update(
    name='django014'
)

# 3.删除数据
# 方法一:通过实例对象
book=BookInfo.objects.filter(id=13)
book.delete()

# 方法二:
# filter和get获取id
BookInfo.objects.filter(id=12).delete()

# 4.查询操作
# 基础查询
BookInfo.objects.get(id=2)

BookInfo.objects.filter(id=2)

BookInfo.objects.all()

BookInfo.objects.count()

# 过滤查询
BookInfo.objects.filter(name__contains='湖')

BookInfo.objects.filter(name__endswith='部')

BookInfo.objects.filter(name__isnull=True)

BookInfo.objects.filter(id__in=[1,2])

BookInfo.objects.filter(id__gt=5)

BookInfo.objects.exclude(id=3)

from django.db.models import F, Q

# F对象
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# Q对象

BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)
BookInfo.objects.filter(id__gt=2,readcount__gt=20)

# 与
BookInfo.objects.filter(Q(id__gt=2)&Q(readcount__gte=20))
# 或
BookInfo.objects.filter(Q(id__gt=2)|Q(readcount__gte=20))
# 非
BookInfo.objects.filter(~Q(id=2))

# 聚合函数 min max count avg sum
from django.db.models import Sum
BookInfo.objects.aggregate(Sum('readcount'))

# 排序
BookInfo.objects.all().order_by('readcount')
BookInfo.objects.order_by('-readcount')

# 关联查询
# 由一到多
book=BookInfo.objects.get(id=3)
book.peopleinfo_set.all()

# 由多到一
person=PeopleInfo.objects.get(id=6)
print(person)
person.book

# 关联过滤查询
# 由多查一
BookInfo.objects.filter(peopleinfo__description__contains='八')

BookInfo.objects.filter(peopleinfo__name='郭靖')

# 由一查多
PeopleInfo.objects.filter(book__name='天龙八部')

PeopleInfo.objects.filter(book__readcount__gt=30)

# 查询集QuerySet
book=BookInfo.objects.all()
book

# 限制查询集
PeopleInfo.objects.all()[3]

PeopleInfo.objects.all()[:4]

# 分页
from django.core.paginator import Paginator
people=PeopleInfo.objects.all()
paginator=Paginator(object_list=people,per_page=2)
persons=paginator.page(1)
paginator.num_pages


def book(request,cat_id,detail_id):
    # GET请求-url路径参数http://127.0.0.1/1/100/
    # print(cat_id,detail_id)
    # GET请求  QueryString  http://ip:port/?key=value&key2=value2
    # 一键一值
    query_string=request.GET
    # a=query_string.get('a')
    # b=query_string.get('b')
    # print(a,b)
    # 一键多值
    alist=query_string.getlist('a')
    b=query_string.get('b')
    print(alist,b)
    return HttpResponse('看书')

# POST表单请求
def login(request):
    body=request.POST
    print(body)
    return HttpResponse('login')


# POST非表单请求
def weibo(request):
    body=request.body
    body_str=body.decode()
    import json
    data=json.loads(body_str)
    print(data)
    return HttpResponse('weibo json')

# 自定义转换器
def site_register(request,mobile):
    return HttpResponse('OK')

# JsonResponse
from django.http.response import JsonResponse
def res_json(request):
    data={
        'name':'itcast',
        'age':15
    }
    return JsonResponse(data)
    data不管是不是字典数据,我们自己改的safe自己负责,不管data是不是字典都可以
    # return JsonResponse(data,safe=False)


# cookie保持在客户端
def set_cookie(request):
    name=request.GET.get('name')
    response=HttpResponse('set_cookie')
    response.set_cookie(key='name',value=name)
    return response

def get_cookie(request):
    cookie=request.COOKIES
    name=cookie.get('name')
    return HttpResponse('get_cookie')

# session保存在服务器,依赖于cookie
def set_session(request):
    request.session['name']='abc'
    return HttpResponse('set_session')

def get_session(request):
    name=request.session('name')
    print(name)
    return HttpResponse('get_session')

from django.views import View
class JDLogin(View):
    def get(self,request):
        return HttpResponse('jd - login - get')
    def post(self,request):
        # self.abc(request)
        return HttpResponse('jd - login - post')
    # def abc(self,request):
    #     return HttpResponse('abc')

"""
CenterView.__mro__
MRO的顺序
"""

from django.contrib.auth.mixins import LoginRequiredMixin
# class CenterView(View,LoginRequiredMixin):
class CenterView(LoginRequiredMixin,View):
    def get(self,request):
        return HttpResponse('center get')
    def post(self,request):
        return HttpResponse('Center post')



