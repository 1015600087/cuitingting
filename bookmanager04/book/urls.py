from django.urls import path
from book.views import index,book,login,weibo,site_register
from book.views import res_json
from book.views import set_cookie,get_cookie
from book.views import set_session,get_session

from book.converters import MobileConverter
from django.urls import register_converter
register_converter(MobileConverter,'phone')

urlpatterns = [
    path('index/',index),
    path('<cat_id>/<int:detail_id>/',book),
    path('login/',login),
    path('weibo/',weibo),
    path('site/register/<phone:mobile>/',site_register),
    path('json/',res_json),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_cookie),
]







