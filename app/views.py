from .models import Musician
from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import SignUpForm, UserUpdateForm, MusicianUpdateForm, SearchForm
from django.contrib.auth.decorators import login_required


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
    return render(request, 'app/base.html',)


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


@login_required
def search(request):
    title = 'Search For Musicians'
    form = SearchForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Musician.objects.all().order_by('user_id').filter(
            instrument__icontains=form['instrument'].value(),
            playing_level__icontains=form['playing_level'].value(),
            city__id__icontains=form['city'].value()).all()[:5]
        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }
    return render(request, 'app/search.html', context)

