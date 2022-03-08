from django.urls import path
from . import views


urlpatterns = [
   path('list', views.index),
   path('delete/<int:todo_id>/', views.remove),
   path('update/<int:todo_id>/', views.updatetask),
]