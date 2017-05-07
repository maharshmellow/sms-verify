from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^verify/$', views.verify, name="verify"),
    url(r'^checkCode/$', views.checkCode, name="checkCode")
]
