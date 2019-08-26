

from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.hello,name='index'),
    url(r'temp/',views.temp,name='template'),
    url(r'page/',views.mypage,name='mypage'),
    url(r's/',views.img,name='mypage'),
    url(r'reg/',views.register,name='reg'),
    url(r'log/', views.logedin, name='log'),
    url(r'thanks', views.thanks, name='thnks'),
    url(r'em', views.emp, name='emp'),

]