from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^test-01/$', test_views),
]
