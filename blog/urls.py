from django.urls import path
from . import views
from .views import PostListView

#name should be specific 'blog-home' not home b/c it can collide with others
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
