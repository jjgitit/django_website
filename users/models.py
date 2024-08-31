from django.db import models
from django.contrib.auth.models import User

#making user models to have 1:1 relationship with profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # remember cascade is when user get deleted you also delete the profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} Profile'
