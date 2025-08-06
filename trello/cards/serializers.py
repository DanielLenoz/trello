from rest_framework import serializers
from .models import Card
from users.views import UserSerializers
from users.models import User


class CardSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Card
        fields = [
            "id",
            "title",
            "description",
            "date_time",
            "listsTrello",
            "user",
        ]
