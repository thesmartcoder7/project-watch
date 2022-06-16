from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project', default=None)
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='project_images/', blank=False, default=None)
    description = models.TextField()
    link = models.CharField(max_length=5000)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def update_project(self, user, title , image, description, link):
        self.user = user
        self.title = title
        self.image = image
        self.description = description
        self.link = link
        self.save()

    def delete_project(self):
        self.delete()



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    usability = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    content = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.project.title}'s Rating"

    def save_rating(self):
        self.save()


    def update_rating(self, user, project, design, usability, content):
        self.user = user
        self.project = project
        self.design = design
        self.usability = usability
        self.content = content
        self.save()

    
    def delete_rating(self):
        self.delete()