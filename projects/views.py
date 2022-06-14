from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from users.forms import *
from datetime import date


# Create your views here.
@login_required
def home (request):
    return render(request, 'projects/index.html')



@login_required
def profile(request):
    return render(request, 'projects/profile.html')



@login_required
def project(request, project_id):
    project = Project.objects.get(id=project_id)
    r_form = RatingForm()
    context = {
        'r_form': r_form,
        'year': date.today().year
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
            return redirect('projects-project', project_id)
        else:
            return render(request, 'projects/project.html', context )
    else:
        r_form = RatingForm()
        context = {
            'r_form': r_form,
            'year': date.today().year
        }
        return render(request, 'projects/project.html', context)




@login_required
def logged_user(request):
    return render(request, 'projects/user.html')



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