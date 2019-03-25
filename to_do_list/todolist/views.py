from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def home(request):
    content = {'待办事项': Todo.objects.all()}
    if request.method == 'POST':
        if request.POST['待办事项'] == '':
            content['警告'] = '请输入内容!'
        else:
            add_row = Todo(thing=request.POST['待办事项'], done=False)
            add_row.save()
            content['信息'] = '添加成功!'
    return render(request, "todolist/home.html", content)

def about(request):
    return render(request, "todolist/about.html")

def edit(request, each_id):
    upd_row = Todo.objects.get(id=each_id)
    content = {'待修改事项': upd_row.thing}
    if request.method == 'POST':
        if request.POST['修改后事项'] == '':
            content['警告'] = '内容不能为空!'
        else:
            upd_row.thing = request.POST['修改后事项']
            upd_row.save()
            return redirect("todolist:主页")
    return render(request, "todolist/edit.html", content)

def delete(request, each_id):
    del_row = Todo.objects.get(id=each_id)
    del_row.delete()
    return redirect("todolist:主页") #redirect是重定向,也就是重新解析一次网址，注意：网址的名字不能单写一个‘主页’，而是写 APPname: WEBname，重定向是使用的GET 方法

def cross(request, each_id):
    if request.POST['完成状态'] == '已完成':
        upd_row = Todo.objects.get(id=each_id)
        upd_row.done = True
    else:
        upd_row = Todo.objects.get(id=each_id)
        upd_row.done = False
    upd_row.save()
    return redirect("todolist:主页")

#render 是转发的意思，当执行此方法时，返回一个渲染后的HTML页面
#意思是给请求对象返回一个渲染后的HTML页面

# render() 如何找到网页 ?
#     根据所提供的网页名称,找所有的templates的文件夹,取第一个匹配的
# 网页名字重复怎么办?
#     给个前缀
#     建个新文件夹在templates下,以 app的名字 命名
#     templates/app的名字/网页名字
#     views.py -> return render(request, "todolist/home.html")