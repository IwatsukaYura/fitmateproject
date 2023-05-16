from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Welcome(TemplateView):
    template_name = 'welcome.html'


class Start(TemplateView):
    template_name = 'start.html'

@login_required
def weight_view(request):
    user = request.user

    params = {
        'weight': user.weight,
        'target_weight': user.target_weight,
        'reach_target': user.reach_target,
        'bmi': user.get_bmi,
    }
    return render(request, 'weight.html', params)

@login_required
def dashbord_view(request):
    user = request.user

    params = {
        'weight': user.weight,
        'target_weight': user.target_weight,
        'reach_target': user.reach_target,
        'bmi': user.get_bmi,
    }
    return render(request, 'dashbord.html', params)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/start/')
    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'signup.html', param)



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/dashbord/')

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'login.html', param)

@login_required
def user_view(request):
    user = request.user

    params = {
        'bmi': user.get_bmi()
    }

    return render(request, 'user.html', params)