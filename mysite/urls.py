from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('addTodo', views.addTodo),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
