from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'posts': Post.objects.all() #adding data from our database
    } # now we can pass this as a third optional arg
        #connecting data
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    #by convention <app>/<model>_<view_type>.html
    context_object_name = 'posts' #b/c django takes obj list as default not the text
    ordering = ['-date_posted'] #with - sign newwest to oldest
    paginate_by = 5
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    #by convention <app>/<model>_<view_type>.html
    context_object_name = 'posts' #b/c django takes obj list as default not the text
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user # set the author as cur user before submitting
        return super().form_valid(form) #this would have been called anyway but we nee to return it

#UserPassesTestMixin is for authenticating author before editing
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user # set the author as cur user before submitting
        return super().form_valid(form) #this would have been called anyway but we nee to return it

    #this is for checking UserPassesTestMixin
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #after deleting, send to home
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
