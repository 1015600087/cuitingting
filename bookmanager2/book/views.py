from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from book.models import BookInfo,PeopleInfo
def index(request):
    return HttpResponse('OK!')


new_book=BookInfo.objects.create(
    name='python',
    pub_date='2020-1-1',
    readcount=10,
    commentcount=100
)

BookInfo.objects.filter(name__contains='湖')

BookInfo.objects.filter(name__endswith='部')

BookInfo.objects.filter(id__gt=3)
BookInfo.objects.filter(id__in=[1,3])

# 删除数据
# 方法1
book=BookInfo.objects.get(id=9)
book.delete()
# 方法2
BookInfo.objects.get(id=8).delete()
BookInfo.objects.filter(id=7).delete()

# 更新数据
# 方法一
book=BookInfo.objects.get(id=5)
book.name='python3'
book.pub_date='2000-1-1'
book.save()


BookInfo.objects.filter(id=6).update(
    name='python2'
)

# 查询
# get查询单一结果，如果不存在会抛出模型类.DoesNotExit异常
# 模型类名.objects.get(属性名=值）  精确查找
BookInfo.objects.get(id=2)

BookInfo.objects.get(name='python3')

# all查询所有的结果
BookInfo.objects.all()

# count查询结果数量
BookInfo.objects.all().count()

# 过滤查询（实现的是sql中的where功能）
# filter过滤出多个结果 返回的是列表
# exclude 排除掉符合条件剩下的结果
# get 过滤单一结果
# 模型类名.objects.filter()/exclude()/get()

BookInfo.objects.get(id=2)

BookInfo.objects.filter(id=2)

BookInfo.objects.filter(id=20)

list=BookInfo.objects.filter(id=1)
print(list)

BookInfo.objects.filter(id=1)
BookInfo.objects.get(id__exact=2)
BookInfo.objects.get(id=2)

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名以'天'开头的图书
BookInfo.objects.filter(name__startswith='天')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为2,4
BookInfo.objects.filter(id__in=(2,4))
BookInfo.objects.filter(id__in=[2,4])


# gt大于 great大
# gte 大于等于 e equel 等于
# lt 小于little

BookInfo.objects.filter(id__gt=3)

# 查询1986年发表的图书
BookInfo.objects.filter(pub_date__year=1986)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

# 查询编号不等于3的图书
# exclude 排除掉符合条件剩下的结果
# not
BookInfo.objects.exclude(id=3)

BookInfo.objects.filter(id=3)

# F
# 两个属性值进行比较
# 查询阅读量等于等于评论量的图书
# 2个属性的比较
from django.db.models import F

BookInfo.objects.filter(readcount__gte=F('commentcount'))

# Q
# filter().filter()
# 或者
# filter(属性名__运算符=值, 属性名__运算符=值,...)
# 查询编号大于2 并且 阅读量大于20的图书

BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)
BookInfo.objects.filter(id__gt=2,readcount__gt=20)

# 逻辑与
from django.db.models import Q
BookInfo.objects.filter(Q(id__gt=2)&Q(readcount__gt=20))

# 逻辑或
# 查询编号大于2 或者 阅读量大于20的图书
BookInfo.objects.filter(Q(id__gt=2)|Q(readcount_gt=20))

# 可以使用~操作符,表示非
# ~Q not 非  和exclude类似
# 查询编号不等于3
BookInfo.objects.filter(~Q(id=2))

# 查询聚合函数
from django.db.models import Max,Min,Count,Sum,Avg
BookInfo.objects.aggregate(Sum('readcount'))

# 排序 order by
# 默认是升序
BookInfo.objects.all().order_by('readcount')
# 属性名前加负号  表示降序
BookInfo.objects.order_by('-readcount')



