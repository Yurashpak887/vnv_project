from django.shortcuts import render, redirect
from .models import Groups
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def getgroups(request):
    groups = Groups.objects.all()
    return render(request, 'groups/groups.html',  {"groups":groups})

def add_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        description = description.capitalize()

        if not name:
            messages.error(request, "Group name is required.")
        elif Groups.objects.filter(name=name).exists():
            messages.error(request, "Group with this name already exists.")
        else:
            try:
                group = Groups(name=name, description=description)
                group.save()
            except IntegrityError:
                messages.warning(request, 'Група з таким іменем вже існує!')
                return redirect('add_group')
        return redirect('getgroups')
    else:

        return render(request, 'groups/add_group.html')
