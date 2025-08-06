from django.db import models
from django.db import models
from users.models import User


class Board(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, related_name="boards")

    def __str__(self):
        return self.name
