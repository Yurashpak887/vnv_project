from django.db import models
from django.contrib.auth.models import User

class Groups(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, default="")
    members = models.ManyToManyField(User, related_name='groups_user_belongs_to')


    def __str__(self):
        return self.name


