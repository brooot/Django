from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    # 如果请求路径是logon，则交给login_views去处理
    url(r'^login/$', login_views),
    url(r'^register/$', register_views),
    url(r'^$|^index$', index_views),
]
