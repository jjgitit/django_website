from django.shortcuts import render
from .models import Post


posts = [
    {
        'author' : 'coreyMS',
        'title' : 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all() #adding data from our database
    } # now we can pass this as a third optional arg
        #connecting data
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
