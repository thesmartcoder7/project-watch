from django.db import models
from django.contrib.auth.models import User

# Create your models here

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