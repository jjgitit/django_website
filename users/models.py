from django.contrib.auth.models import User
from django.db import models
from PIL import Image


# making user models to have 1:1 relationship with profile
class Profile(models.Model):
    """for basic profile informaitons"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # remember cascade is when user get deleted you also delete the profile
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user} Profile"

    # this save already exists but we are modifying, it gets run everytime model gets saved
    def save(self):
        super().save()  # call the parent save method first
        img = Image.open(self.image.path)  # save the current saving img to resize
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
