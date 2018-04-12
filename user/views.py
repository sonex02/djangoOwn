from django.contrib import messages
from django.shortcuts import render, redirect
from user.forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, '注册成功，请登录！')
            return redirect('/user/login')
    else:
        # 如果不是post方法，则返回注册页面
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})

