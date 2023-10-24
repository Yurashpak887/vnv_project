from django.urls import path

from .views import getgroups, add_group, edit_group, delete_group

urlpatterns = [
    path('groups', getgroups, name='getgroups'),
    path('add_group', add_group, name='add_group'),
    path('edit_group/<int:group_id>', edit_group, name='edit_group'),
    path('delete_group/<int:group_id>', delete_group, name='delete_group')

]
