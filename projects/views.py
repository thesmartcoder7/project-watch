
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import math

from .forms import *
from users.forms import *
from datetime import date
from django.contrib import messages


def get_averages(project):
    project_rating = Rating.objects.filter(project=project)
    design = []
    usability = []
    content = []
    for rating in project_rating:
        design.append(rating.design)
        usability.append(rating.usability)
        content.append(rating.content)

    if sum(design) == 0 and len(design) == 0:
        average_design = 0
    else:
        average_design = round(sum(design)/len(design))
    
    if sum(usability) == 0 and len(design) == 0:
        average_usability = 0
    else:
        average_usability = round(sum(usability)/len(usability))

    if sum(content) == 0 and len(content) == 0:
        average_content = 0
    else:
        average_content = round(sum(content)/len(content))
    average_score = 0
    if average_design == 0 and average_content == 0 and average_usability == 0:
        average_score = 0
    else:
        average_score = round((average_design + average_usability + average_content)/3)

    return [average_design, average_usability, average_content, average_score]


def get_top():
    highest = None
    max = 0
    projects = Project.objects.all()
    for project in projects:
        if get_averages(project)[3] > max:
            highest = project
    
    return highest


# Create your views here.
@login_required
def home (request):
    users = User.objects.all()
    projects = Project.objects.all()
    current_user = User.objects.get(username=request.user.username)
    top_rated = get_top()

    context = {
        'users':users,
        'projects':projects,
        'current_user': current_user,
        'top_rated': top_rated,
        'averages': get_averages(top_rated),
        'year': date.today().year,
    }

    return render(request, 'projects/index.html', context)



@login_required
def profile(request, username):
    viewed_user = User.objects.get(username=username)
    user_projects = Project.objects.filter(user=viewed_user)
    current_user = User.objects.get(username=request.user.username)
    context = {
        'viewed_user': viewed_user,
        'user_projects': user_projects,
        'year': date.today().year,
        'current_user': current_user
    }
    return render(request, 'projects/profile.html',  context)



@login_required
def project(request, project_id):
    project = Project.objects.get(id=project_id)
    current_user = User.objects.get(username=request.user.username)
    project_rating = Rating.objects.filter(project=project)
    design = []
    usability = []
    content = []
    for rating in project_rating:
        design.append(rating.design)
        usability.append(rating.usability)
        content.append(rating.content)

    if sum(design) == 0 and len(design) == 0:
        average_design = 0
    else:
        average_design = round(sum(design)/len(design))
    
    if sum(usability) == 0 and len(design) == 0:
        average_usability = 0
    else:
        average_usability = round(sum(usability)/len(usability))

    if sum(content) == 0 and len(content) == 0:
        average_content = 0
    else:
        average_content = round(sum(content)/len(content))
    average_score = 0
    if average_design == 0 and average_content == 0 and average_usability == 0:
        average_score = 0
    else:
        average_score = round((average_design + average_usability + average_content)/3)


    
    r_form = RatingForm(request.POST)
    context = {
        'current_user': current_user,
        'project': project,
        'r_form': r_form,
        'year': date.today().year,
        'average_design': average_design,
        'average_usability': average_usability,
        'average_content': average_content, 
        'average_score': average_score
    }
    if request.method == 'POST':
        if r_form.is_valid():
            rating = Rating.objects.create(
                design=request.POST.get('design'), 
                usability=request.POST.get('usability'), 
                content=request.POST.get('content'),
                user=request.user,
                project=project
            )
            rating.save()
            messages.success(request, "Thank you for the rating!")
            return redirect('projects-project', project_id)
        else:
            messages.error(request, "Kindly fill in all the fields!")
            return render(request, 'projects/project.html', context )
    else:
        r_form = RatingForm(request.POST)
        context = {
            'current_user': current_user,
            'project': project,
            'r_form': r_form,
            'year': date.today().year,
            'average_design': average_design,
            'average_usability': average_usability,
            'average_content': average_content, 
            'average_score': average_score
        }
        return render(request, 'projects/project.html', context)




@login_required
def logged_user(request):
    current_user = User.objects.get(username=request.user.username)
    user_projects = Project.objects.filter(user=current_user)
    context = {
        'current_user':current_user,
        'user_projects': user_projects,
        'year': date.today().year
    }
    return render(request, 'projects/user.html',  context)




@login_required
def search(request):
    if request.method == 'POST':
        current_user = User.objects.get(username=request.user.username)
        search_term = request.POST.get('search')
        projects = Project.objects.filter(title__icontains=search_term)
        context = {
            'current_user': current_user,
            'projects': projects,
            'year': date.today().year
        }
        return render(request, 'projects/search.html', context)
    else:
        return redirect('projects-home')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile,)
        context = {
            'u_form': u_form,
            'p_form': p_form,
            'year': date.today().year
        }
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('projects-user')
        else:
            return render(request, 'projects/user_edit.html', context)
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile,)
        context = {
            'u_form': u_form,
            'p_form': p_form,
            'year': date.today().year
        }
        return render(request, 'projects/user_edit.html', context)



@login_required
def add_project(request):
    add_form = NewProjectForm()
    context = { 
        'add_form': add_form,
        'year': date.today().year
    }
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        add_form = NewProjectForm(request.POST, request.FILES,)
        if add_form.is_valid():
            project = Project.objects.create(
                user=user, image=request.FILES.get('image'), 
                title=request.POST.get('title'), link=request.POST.get('link'), 
                description=request.POST.get('description')
            )
            project.save()
            return redirect('projects-user')
        else:
            add_form = NewProjectForm(request.POST)
            return render(request, 'projects/add_project.html', context)
    
    return render(request, 'projects/add_project.html', context)




@login_required
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id)
    add_form = NewProjectForm(instance=project)

    context = { 
        'add_form': add_form,
        'year': date.today().year
    }

    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        add_form = NewProjectForm(request.POST, request.FILES, instance=project)
        if add_form.is_valid():
            project.user = user
            if request.FILES.get('image'):
                project.image = request.FILES.get('image')
            project.title = request.POST.get('title')
            project.link = request.POST.get('link')
            project.description = request.POST.get('description')
            project.save()
            return redirect('projects-user')
        else:
            add_form = NewProjectForm(request.POST, request.FILES, instance=project)
            return render(request, 'projects/edit_project.html', context)
    
    return render(request, 'projects/edit_project.html', context)



@login_required
def delete(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect('projects-user')
