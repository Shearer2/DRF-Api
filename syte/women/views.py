from django.forms import model_to_dict
from django.shortcuts import render
# Импортируем generics
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


# Класс APIView является базовым классом django rest framework.
class WomenAPIView(APIView):
    # Метод get отвечает за get-запросы поступающие на сервер.
    def get(self, request):
        # Чтобы не возникла ошибка необходимо указать метод values().
        w = Women.objects.all()
        # Возвращаем клиенту, от которого пришёл запрос, json строку.
        # Чтобы сериализатор обрабатывал не одну запись, а список записей, указываем параметр mane=True.
        return Response({'posts': WomenSerializer(w, many=True).data})

    #Добавляем определённые данные в базу данных.
    def post(self, request):
        # Чтобы не возникали ошибки при вводе неверных данных необходимо сначала создать сериализатор
        # с полученными данными.
        serializer = WomenSerializer(data=request.data)
        # Если не было указано какое-то поле, то генерируем исключение.
        serializer.is_valid(raise_exception=True)

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        # Функция model_to_dict преобразует объект django в словарь.
        return Response({'post': WomenSerializer(post_new).data})


'''class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    # Указываем класс сериализатор.
    serializer_class = WomenSerializer
'''
