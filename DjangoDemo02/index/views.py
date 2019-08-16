from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.


def test_views(request):

    # 第一种方法，使用loader
    # #1. 通过loader加载模板
    # t = loader.get_template("red_heart.html")
    #
    # #2. 将模板渲染成字符串
    # html = t.render()
    #
    # #3. 再通过HttpResponse将字符串响应给浏览器
    # return HttpResponse(html);

    # 第二种方法，使用render
    return render(request, "red_heart.html")