from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *


# Create your views here.
@login_required
def home (request):
    return render(request, 'projects/index.html')



@login_required
def profile(request):
    return render(request, 'projects/profile.html')



@login_required
def project(request):
    return render(request, 'projects/project.html')



@login_required
def logged_user(request):
    return render(request, 'projects/user.html')



@login_required
def add_project(request):
    add_form = NewProjectForm()
    context = { 
        'add_form': add_form
    }
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        add_form = NewProjectForm(request.POST, request.FILES,)
        if add_form.is_valid():
            print('\n form is validated \n')
            project = Project.objects.create(
                user=user, image=request.FILES.get('image'), 
                title=request.POST.get('title'), link=request.POST.get('link'), 
                description=request.POST.get('description')
            )
            project.save()
            return redirect('projects-user')
        else:
            print('\n form not validated \n')
            add_form = NewProjectForm(request.POST)
            return render(request, 'projects/add_project.html', context)
    
    print('\n form did not send a post request\n')
    return render(request, 'projects/add_project.html', context)