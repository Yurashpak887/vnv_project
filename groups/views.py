from django.shortcuts import render, redirect
from .models import Groups
from django.contrib import messages
from django.db import IntegrityError
from .validation import is_valid_group_name
from django.urls import reverse


# Create your views here.
def getgroups(request):
    groups = Groups.objects.all()
    return render(request, 'groups/groups.html', {"groups": groups})


def add_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        description = description.capitalize()

        if not name:
            messages.error(request, "Group name is required.")
            return redirect('add_group')

        if not is_valid_group_name(name):
            messages.warning(request,
                             'Invalid format. Group name should start with a letter and should not exceed 30 characters.')
            return redirect('add_group')

        try:
            group = Groups(name=name, description=description)
            group.save()
        except IntegrityError:
            error_message = "Group with this name already exists."
            messages.warning(request, error_message)
            return redirect('add_group')

        return redirect('getgroups')
    else:
        return render(request, 'groups/add_group.html')

def edit_group(request, group_id):
    group = Groups.objects.get(id=group_id)

    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_description = request.POST.get('description')
        new_description = new_description.capitalize()



        try:
            group.name = new_name
            group.description = new_description
            group.save()
        except IntegrityError:
            error_message = "Group with this name already exists."
            messages.warning(request, error_message)
            return redirect(reverse('edit_group', args=[group_id]))

        return redirect('getgroups')

    return render(request, 'groups/edit_group.html', {'group': group})

def delete_group(request, group_id):
    try:
        group = Groups.objects.get(id=group_id)
        if group.members.count() == 0:
            group.delete()
            return redirect('getgroups')
        else:
            error_message = "This group cannot be deleted as it contains users."
            messages.error(request, error_message)
            return redirect('getgroups')
    except Groups.DoesNotExist:
        return redirect('getgroups')
