from django.urls import path
from book.views import index,test
from book.views import JDLogin,CenterView

urlpatterns = [
    path('index/',index),
    path('test/',test),
    path('jd/',JDLogin.as_view()),
    path('center/',CenterView.as_view()),
]






