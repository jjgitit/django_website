from django.urls import path
from . import views

#name should be specific 'blog-home' not home b/c it can collide with others
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
