from django.contrib import admin
from django.urls import path

from blog import views as blog_view

urlpatterns = [
    path('', blog_view.blog, name='blog'),
    path('<int:blog_id>/', blog_view.detail, name='detail'),
    path('new/', blog_view.new, name='new'),
    path('create/', blog_view.create, name='create'),
]