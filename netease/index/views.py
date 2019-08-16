from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_views(request):
    return HttpResponse("<h1>网站首页</h1>")

def register_views(request):
    return HttpResponse("<h1>注册页面</h1>")

def login_views(request):
    return HttpResponse("<h1>登录页面</h1>")