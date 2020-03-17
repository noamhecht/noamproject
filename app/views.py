from django.http import HttpResponse
from django.template import loader
from .models import Musician
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import SignUpForm, UserUpdateForm, MusicianUpdateForm
from django.contrib.auth.decorators import login_required
from app.tokens import account_activation_token
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        m_form = MusicianUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.musician)
        if u_form.is_valid() and m_form.is_valid():
            u_form.save()
            m_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        m_form = MusicianUpdateForm(instance=request.user.musician)

    context = {
        'u_form': u_form,
        'm_form': m_form
    }

    return render(request, 'app/profile.html', context)


def index(request):
    return render(request, 'app/index.html',)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})

