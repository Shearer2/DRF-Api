from django.shortcuts import render
# Импортируем generics
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    # Указываем класс сериализатор.
    serializer_class = WomenSerializer

