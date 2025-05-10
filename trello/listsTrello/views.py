from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ListsTrelloSerializer
from .models import ListsTrello


class ListsTrelloViewSet(viewsets.ModelViewSet):
    queryset = ListsTrello.objects.all()
    serializer_class = ListsTrelloSerializer
