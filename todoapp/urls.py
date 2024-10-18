from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='index'), # path to the index
    path('create/', views.create_todo, name='create_todo'), # path to create todo
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),  # path to complete a todo
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo')
]