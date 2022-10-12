from django.urls import path
from todolist.views import show_todo_list, show_json, register, login_user, logout_user, show_logout_page, create_task, add_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todo_list, name='show_todo_list'),
    path('json/', show_json, name='json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logoutpage/', show_logout_page, name='show_logout_page'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('add/', add_task, name='add_task')
]
