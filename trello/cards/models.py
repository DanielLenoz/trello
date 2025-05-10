from django.db import models
from users.models import User
from listsTrello.models import ListsTrello


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    listsTrello = models.ForeignKey(
        ListsTrello, on_delete=models.CASCADE, related_name="cards"
    )
    user = models.ManyToManyField(User, related_name="cards")

    def __str__(self):
        return self.title
