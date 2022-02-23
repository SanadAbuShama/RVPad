
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt


def landing(request):
    if not 'userid' in request.session:
        return redirect('/rvpad/landing')
    else:
        return redirect('/rvpad/restaurants')


def profile(request):

    context = {
        'user': User.objects.get(id=request.session['userid'])
    }
    return render(request, 'profile.html', context)


def index(request):
    if 'userid' in request.session:
        return redirect('/wishes')
    else:
        return render(request, 'index.html')


def register(request):
    errors = User.objects.register_validator(request.POST)
    request.session['which_form'] = request.POST['which_form']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')
    else:

        password = request.POST['password']
        pw_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        created_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        if 'image' in request.FILES:
            created_user.image = request.FILES['image']
            created_user.save()
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            request.session['userid'] = logged_user.id
        return redirect('/profile')


def login(request):
    errors = User.objects.login_validator(request.POST)
    request.session['which_form'] = request.POST['which_form']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')
    user = User.objects.filter(email=request.POST['email'])
    if len(user) != 0:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/wishes')

    return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')
