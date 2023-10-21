from django.contrib import admin
from django.urls import path, include

from .views import home, getusers, add_user, edit_user, delete_user

urlpatterns = [
    path('', home, name='home'),
    path('users', getusers, name='getusers'),
    path('add_user', add_user, name='add_user'),
    path('edit_user/<int:user_id>', edit_user, name='edit_user'),
    path('delete_user/<int:user_id>', delete_user, name='delete_user')
]