from django.urls import path
from tasks.views import  filter_tasks, home,login_view, Add_task,update_task, delete_task,register_view,logout_view

urlpatterns = [
    path('', home, name='home'),
    path('login/',login_view , name='login'),
    path('add/', Add_task, name='add_task'),
    path('tasks/<str:foo>/', filter_tasks, name='tasks'),
    path('task/<int:pk>/',update_task, name='task'),    
    path('delete/<int:pk>/', delete_task, name='delete'),
    path('register/', register_view, name='register'),
    path('logout/',logout_view, name='logout')
]