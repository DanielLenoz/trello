from rest_framework import serializers
from .models import Board
from listsTrello.serializers import ListsTrelloSerializer

class BoardSerializer(serializers.ModelSerializer):

    lists = ListsTrelloSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ["id", "nombre", "date_time", "lists"]
