from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project', default=None)
    title = models.CharField(max_length=1000)
    image = models.ImageField( default='default.png', upload_to='project_images/', blank=True)
    description = models.TextField()
    link = models.CharField(max_length=5000)

    def __str__(self):
        return self.title



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    usability = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    content = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.project.title}'s Rating"