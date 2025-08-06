from rest_framework import serializers
from .models import Board
from listsTrello.serializers import ListsTrelloSerializer


class BoardSerializer(serializers.ModelSerializer):

    listsTrello = ListsTrelloSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ["id", "name", "date_time", "users", "listsTrello"]
