from django.test import TestCase
from django.contrib.auth.models import User
from users.models import *
from projects.models import *

# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='samuel', email='samuel.martins3.sm@gmail.com', password='thesmartcoder')
        self.project = Project.objects.create(user=self.user, title='my title', image='default.png', description='my description', link='project link')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save(self): 
        self.user.save()
        all_projects = Project.objects.all()
        self.assertEquals(len(all_projects),1)

    def test_update(self):
        self.user.save()
        self.project.user = self.user
        self.project.title = 'my new title'
        self.project.image = 'default.png'
        self.project.description = 'my description'
        self.project.link = 'project link'
        self.project.save()
        self.assertEquals(self.project.title, 'my new title')

    def test_delete(self):
        self.user.save()
        self.new_project = Project.objects.create(user=self.user, title='my 2nd title', image='default.png', description='my 2nd description', link='project link 2')
        self.new_project.save()
        self.new_project.delete()
        all_posts = Project.objects.all()
        self.assertEquals(len(all_posts),1)



class RatingTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='samuel', email='samuel.martins3.sm@gmail.com', password='thesmartcoder')
        self.project = Project.objects.create(user=self.user, title='my title', image='default.png', description='my description', link='project link')
        self.rating = Rating.objects.create(user=self.user, project=self.project, design=10, usability=10, content=10)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save(self): 
        self.user.save()
        self.project.save()
        all_ratings = Rating.objects.all()
        self.assertEquals(len(all_ratings),1)

    def test_update(self):
        self.project.save()
        self.user.save()
        self.rating.user = self.user
        self.rating.project = self.project
        self.rating.design = 9
        self.rating.usability = 10
        self.rating.content = 10
        self.rating.save()
        self.assertEquals(self.rating.design, 9)

    def test_delete(self):
        self.user.save()
        self.project.save()
        self.new_rating = Rating.objects.create(user=self.user, project=self.project, design=8, usability=8, content=10)
        self.new_rating.save()
        self.new_rating.delete()
        all_ratings = Rating.objects.all()
        self.assertEquals(len(all_ratings), 1)