from django.conf.urls import url
from .views import *

# 当访问路径是http://localhost:8000/news/xxx的时候交给news的urls找到index_views去处理
urlpatterns = [
    url(r'^$|^index/$', index_views)
]
