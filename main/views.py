from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.db import IntegrityError
from django.contrib import messages

from groups.models import Groups
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.shortcuts import redirect
from .validation import is_valid_username

def home(request):
    return render(request, 'main/index.html')


def getusers(request):
    users = User.objects.all()
    return render(request, 'main/users.html', {"users": users})


def add_user(request):
    if request.method == 'POST':
        if request.POST.get('username'):
            username = request.POST.get('username')
            groups = request.POST.getlist('group')

            if not username or not is_valid_username(username):
                messages.warning(request,
                                 'Invalid username format. The username should start with a capital letter of the English alphabet, \n '
                                 'should not contain digits or spaces.')
                return redirect('add_user')

            try:
                user = User.objects.create_user(username=username)
            except IntegrityError:
                messages.warning(request, 'Користувач з таким іменем вже існує!')
                return redirect('add_user')

            for group_id in groups:
                group = Groups.objects.get(id=group_id)
                group.members.add(user)
            return redirect('getusers')
    else:
        groups = Groups.objects.all()
        return render(request, 'main/add_user.html', {'groups': groups})

    return redirect('/')

def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    groups = Groups.objects.all()

    if request.method == 'POST':
        new_username = request.POST.get('username')
        selected_group_ids = request.POST.getlist('group')

        # Оновлюємо ім'я користувача
        user.username = new_username
        user.save()

        # Очищаємо існуючі групи користувача та додаємо нові групи
        user.groups_user_belongs_to.clear()
        user.groups_user_belongs_to.add(*selected_group_ids)

        return redirect('getusers')

    return render(request, 'main/edit_user.html', {"user": user, 'groups': groups})