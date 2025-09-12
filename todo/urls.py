from django.urls import path
from . import views

urlpatterns = [
    path('',  views.task, name='home'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task/<id>/', views.delete_task, name ='delete_task')
    ]
