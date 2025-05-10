from rest_framework import serializers
from .models import ListsTrello
from cards.serializers import CardSerializer


class ListsTrelloSerializer(serializers.ModelSerializer):

    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = ListsTrello
        fields = ["id", "name", "Board", "date_time", "cards"]
