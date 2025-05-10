from django.db import models
from boards.models import Board


class ListsTrello(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    Board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name="listsTrello"
    )

    def __str__(self):
        return self.name
