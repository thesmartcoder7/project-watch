from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='project_watch/user_profiles/', blank=True)
    bio = models.TextField()
    github = models.CharField(max_length=2000, blank=True)
    linkedin = models.CharField(max_length=2000, blank=True)
    twitter = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"



class Project(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='project_watch/project_images')
    description = models.TextField()
    link = models.CharField(max_length=5000)

    def __str__(self):
        return self.title



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.project.title}'s Rating"