from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('index')


# 面向过程
def test(request):
    # print(request.method)
    if request.method == 'GET':
        return HttpResponse('get')
    else:
        return HttpResponse('post')


# 面向对象
# 类视图
# 1.类视图继承自View
# 2.类视图的方法  是根据请求方式来实现的
from django.views import View
class JDLogin(View):
    # self为实例对象
    # request危机请求对象
    def get(self,request):
        return HttpResponse('jd-login-get')

    def post(self,request):
        return HttpResponse('jd-login-post')

# 类视图的多继承重写dispatch
# class CenterView(View):
#     def get(self,request):
#         isLogin=False
#         if isLogin:
#             return HttpResponse('center get')
#         else:
#             return HttpResponse('请登录')
#
#     def post(self,request):
#         isLogin=False
#         if isLogin:
#             return HttpResponse('center post')
#         else:
#             return HttpResponse('请登录')

from django.contrib.auth.mixins import LoginRequiredMixin

# class CenterView(View,LoginRequiredMixin):
class CenterView(LoginRequiredMixin,View):
    def get(self,request):
        return HttpResponse('center get')
    def post(self,request):
        return HttpResponse('center post')













