from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField(default='user-default.png', upload_to='project_watch/user_profiles/')
    work_title = models.CharField(max_length=2000, blank=True)
    bio = models.TextField()
    github = models.CharField(max_length=2000, blank=True)
    linkedin = models.CharField(max_length=2000, blank=True)
    twitter = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


