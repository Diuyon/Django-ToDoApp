"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import todolist.urls
urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'todo/', include(todolist.urls)),
]
# 当localhost:8000/ 接的分别是admin/ 或者 ''时，分别进行哪些处理
#这里使用include的原因是，to_do_list是一个项目，todolist是项目下的一个app，每个app自然有很多页面
#to_do_list下的urls是当这个项目执行时，第一个接受到网址的点，然后根据后面的地址分别发送给不同的app去处理，所以我们得事先在各app下创建一个属于自己的urls来充当中转站，然后通过中转站发送至对应的功能模块
#所以include的使用视为了更方便去管理项目下的众多app，每个app下所对应的功能模块
#例如网址：/todo/home   /todo/about   /admin/login   /admin/regist