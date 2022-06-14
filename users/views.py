from django.shortcuts import render,  redirect
from .forms import SignUpForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-signin')
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})


def signin(request):
    return render(request, 'users/login.html')