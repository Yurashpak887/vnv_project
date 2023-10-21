from django.shortcuts import render, redirect
from django.db import IntegrityError
from groups.models import Groups
from django.contrib.auth.models import User
from django.contrib import messages
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
                messages.warning(request, "The user with this name already exists")
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
        user.username = new_username
        user.save()
        user.groups_user_belongs_to.clear()
        user.groups_user_belongs_to.add(*selected_group_ids)

        return redirect('getusers')

    return render(request, 'main/edit_user.html', {"user": user, 'groups': groups})


def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect('getusers')
    except User.DoesNotExist:
        return redirect('getusers')
