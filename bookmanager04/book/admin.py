from django.contrib import admin

# Register your models here.
# 导入模型类
from book.models import BookInfo,PeopleInfo
# 注册书籍模型
admin.site.register(BookInfo)
# 注册人物模型
admin.site.register(PeopleInfo)




