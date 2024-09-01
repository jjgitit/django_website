from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

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
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
