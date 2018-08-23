from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
import random
from . import forms, models
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#主页
def dachuang(request):
    img_src = '/static/images/dachuang/train/' + str(random.randint(1,4349)) + '.jpg'
    import os
    model_names = [name for name in os.listdir('static/models') if name[-2:] == 'h5']
    template = get_template('dachuang/index.html')
    html = template.render(locals())
    return HttpResponse(html)

#返回随机图片
def random_pic(request):
    img_src = '/static/images/dachuang/train/' + str(random.randint(1,4349)) + '.jpg'
    return HttpResponse(img_src)

#识别图片
@csrf_exempt
def distinguish_0(request):
    img_name = 'static/images/dachuang/train/' + request.POST.get('img_name')
    model_name = 'static/models/' + request.POST.get('model_name')
    from .distinguish import distinguish
    if request.POST.get('model_name')[:3] == 'cnn':
        [name, zf] = distinguish.distinguish_cnn(img_name, model_name)
    else:
        [name, zf] = distinguish.distinguish_bp(img_name, model_name)
    return JsonResponse({'name':name, 'zf':zf})

#识别图片
@csrf_exempt
def distinguish_1(request):
    img_name = 'static/images/dachuang/upload/' + request.POST.get('img_name')
    model_name = 'static/models/' + request.POST.get('model_name')
    from .distinguish import distinguish
    if request.POST.get('model_name')[:3] == 'cnn':
        [name, zf] = distinguish.distinguish_cnn(img_name, model_name)
    else:
        [name, zf] = distinguish.distinguish_bp(img_name, model_name)
    return JsonResponse({'name':name, 'zf':zf})

@csrf_exempt
def upload_file(request):
    username = request.POST.get('username')
    fafafa = request.FILES.get('fafafa')
    import os
    img_path = os.path.join('static/images/dachuang/upload/',fafafa.name)    #存储的路径
    with open(img_path,'wb') as f:      #图片上传
        for item in fafafa.chunks():
            f.write(item)
    ret = {'code': True , 'data': img_path}  #'data': img_path 数据为图片的路径，
    return JsonResponse(ret)    #将数据的路径发送到前端

#项目介绍
def introduction(request):
    template = get_template('dachuang/introduction.html')
    html = template.render(locals())
    return HttpResponse(html)

#人物
def teacher(request):
    template = get_template('dachuang/teacher.html')
    html = template.render(locals())
    return HttpResponse(html)

def wzy(request):
    template = get_template('dachuang/wzy.html')
    html = template.render(locals())
    return HttpResponse(html)

def dch(request):
    template = get_template('dachuang/dch.html')
    html = template.render(locals())
    return HttpResponse(html)

def pk(request):
    template = get_template('dachuang/pk.html')
    html = template.render(locals())
    return HttpResponse(html)

#登录登出
def login(request):
    if request.session.get('is_login', None):
        return redirect('/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '所有的字段都必须填写！'
        if login_form.is_valid():
            name = login_form.cleaned_data.get('name')
            password = login_form.cleaned_data.get('password')
            # ....
            try:
                user = models.User.objects.get(name=name)
            except:
                message = '用户不存在'
                return render(request, 'dachuang/login.html', locals())

            if password == user.password:
                request.session['is_login'] = True
                request.session['user_name'] = user.name
                return redirect('/dachuang')
            else:
                message = '密码错误'
                return render(request, 'dachuang/login.html', locals())
        else:
            return render(request, 'dachuang/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'dachuang/login.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/dachuang")
    request.session.flush()
    return redirect("/dachuang")