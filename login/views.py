from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse('Hello，我是测试页面！')

def index(request):
    return render(request,'user/index.html')
