from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('cuitingting')

def book(request,cat_id,detail_id):
    # print(cat_id,detail_id)
    query_string=request.GET
    # a=query_string['a']
    # b=query_string['b']
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
    import json
    data=json.loads(body_str)
    print(data)
    return HttpResponse('weibo json')

#
# from book.models import BookInfo,PeopleInfo
# BookInfo.objects.all()
#
# # 一.数据库操作
# # 1.增加
# # 方法一:创建实例对象(需要save手动调用)
# # save方法是父类  ORM中已经封装好的
# book=BookInfo()
# book.name='django'
# book.readcount=10
# book.commentcount=200
# book.pub_date='2020-12-25'
# book.save()
# # 方法二:
# # objects为代理人,可以帮助我们实现增删改查操作
# new_book=BookInfo.objects.create(
#     name='Python',
#     readcount=20,
#     commentcount=300,
#     pub_date='2020-12-25'
# )
#
# # 2.更新数据
# # 方法一:
# # 通过实例对象,修改实例对象的属性来修改数
# # 第一步先获取对象
# book=BookInfo.objects.get(id=6)
# # 第二步修改实例对象的属性来修改数据
# book.name='Python2'
# # 手动调用
# book.save()
#
# # 方法二:
# # 直接更新  查询数据的方法  查询数据之后 直接调用update
# # filter()就是根据条件查询数据
# from book.models import BookInfo,PeopleInfo
# BookInfo.objects.filter(id=5).update(
#     name='django2'
# )
#
#
# # 3.删除数据
# # 方法一:
# # 通过实例对象,delete方法实现数据的删除
# book=BookInfo.objects.get(id=6)
# # 调用delete方法   在父类中ORM已经定义好的方法
# book.delete()
#
# # 4.查询-基本查询
# # get查询单一结果,如果不存在会抛出异常
# # 模型类名.objects.get(属性名=值)  精确查询
# BookInfo.objects.get(id=3)
#
# BookInfo.objects.get(name='雪山飞狐')
#
# # 捕获异常
# try:
#     BookInfo.objects.get(id=7)
#
# except BookInfo.DoesNotExist as e:
#     print(e)
#
# # all查询所有结果
# BookInfo.objects.all()
#
# # count查询结果数量
# BookInfo.objects.count()
#
# # 二.过滤查询
# # get过滤单一  filter过滤多个,返回的是列表  exclude排除掉符合条件剩下的结果
#
# BookInfo.objects.get(id=2)
#
# BookInfo.objects.filter(id=2)
#
# BookInfo.objects.filter(name__contains='湖')
#
# BookInfo.objects.filter(name__endswith='部')
#
# BookInfo.objects.filter(name__startswith='天')
#
# BookInfo.objects.filter(name__isnull=True)
#
# BookInfo.objects.filter(id__in=[1,2,3])
#
# BookInfo.objects.filter(id__gt=2)
#
# BookInfo.objects.filter(pub_date__year=1980)
#
# # BookInfo.objects.filter(pub_data__gt='1990-1-1')
#
# # 三.F对象
# from django.db.models import F
# BookInfo.objects.filter(readcount__gte=F('commentcount'))
#
#
# # 四.Q对象
# # 1.多条件查询
# # filter().filter()
# # filter(属性名__运算符=值,属性名__运算符=值)
# BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)
#
# BookInfo.objects.filter(id__gt=2,readcount__gt=20)
#
# # 2.逻辑与
# from django.db.models import Q
# BookInfo.objects.filter(Q(id__gt=2)&Q(readcount__gt=20))
#
# # 3.逻辑或
# BookInfo.objects.filter(Q(id__gt=2)|Q(readcount__gt=20))
#
# # 4.非
# BookInfo.objects.exclude(id=3)
#
# BookInfo.objects.filter(~Q(id=3))
#
# # 五.聚合函数
# from django.db.models import Max,Min,Count,Sum,Avg
# BookInfo.objects.aggregate(Sum('readcount'))
#
# BookInfo.objects.aggregate(Avg('readcount'))
#
# # 六.排序
# BookInfo.objects.order_by('readcount')
#
# from book.models import PeopleInfo,BookInfo
# # 七.关联查询
# # 1.由一到多
# # 获取书籍信息
# book=BookInfo.objects.get(id=2)
# # 根据书籍信息获取人物信息
# book.peopleinfo_set.all()
#
# # 2.由多到一
# # 查询人物信息
# person=PeopleInfo.objects.get(id=6)
# person
# # 根据人物信息查询书籍相关的数据
# person.book
#
# # 八关联过滤查询
# # 1.由多模型类查询单一模型类数据
# BookInfo.objects.filter(peopleinfo__description__contains='八')
#
# # 查询图示,要求图书人物为'郭靖'
# BookInfo.objects.filter(peopleinfo__name='郭靖')
#
# BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
#
# # 2.由一模型查询多模型
# # 查询图书阅读量大于30的所有人物
# PeopleInfo.objects.filter(book__readcount__gt=30)
#
# # 查询
# PeopleInfo.objects.filter(book__name='天龙八部')
#
#
# # 九.限制查询
# from book.models import PeopleInfo
# PeopleInfo.objects.all()[3]
#
# PeopleInfo.objects.all()[:3]
# PeopleInfo.objects.all()[:4]
#
# # 10.分页
# from django.core.paginator import Paginator
# people=PeopleInfo.objects.all()
# paginator=Paginator(object_list=people,per_page=3)
#
# persons=paginator.page(1)
# persons.object_list
# paginator.num_pages
















