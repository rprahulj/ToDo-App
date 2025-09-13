from django.urls import path
from . import views

urlpatterns = [
    path('',  views.task, name='home'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task/<id>/', views.delete_task, name ='delete_task'),
    path('mark_task/<id>/', views.mark_task, name = 'mark_task'),
    path('unmark_task/<id>/', views.unmark_task, name = 'unmark_task'),
    path('update_task/<id>/', views.update_task, name = 'update_task'),
    ]
