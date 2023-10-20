from django.contrib import admin
from django.urls import path, include

from .views import getgroups, add_group

urlpatterns = [
    path('groups', getgroups, name='getgroups'),
    path('add_group', add_group, name='add_group')
]