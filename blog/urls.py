from django.urls import path
from . import views
from .views import (
    PostDeleteView,
    PostListView,
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

#name should be specific 'blog-home' not home b/c it can collide with others
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]
