from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User #this is one to many relation as one person 
#can post many posts


#we create our data here as classes which is an intuitive way of constructing
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user get deleted we also delete related posts

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})
