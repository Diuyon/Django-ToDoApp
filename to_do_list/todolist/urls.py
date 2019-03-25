from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('home/', views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('edit/<each_id>', views.edit, name='编辑'),
    path('del/<each_id>', views.delete, name='删除'),
    path('cross/<each_id>', views.cross, name='划掉'),
]
#<>表示在里面的内容是数字，forloop_counter要与前台的变量名一致，只是将. 换成了_