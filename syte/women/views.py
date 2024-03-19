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
        # Метод save автоматически вызовет метод create сериализатора и добавит новые данные.
        serializer.save()

        # После использования метода save можно не создавать новый объект, а использовать тот, который уже имеется.
        # data ссылается на новый созданный объект.
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        # Забираем из словаря идентификатор записи, которую нужно поменять, если его нет, то возвращаем None.
        pk = kwargs.get("pk", None)
        # Если ключа нет, то возвращаем ответ клиенту.
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        # Пробуем взять нужную запись из модели Women.
        try:
            instance = Women.objects.get(pk=pk)
        # Если была указана не существующая запись, то возвращаем исключение.
        except:
            return Response({"error": "Method PUT not allowed"})

        # Если мы получили и ключ и запись по ключу, то создаём сериализатор.
        # data это данные для изменения, а instance это запись, которую необходимо поменять.
        serializer = WomenSerializer(data=request.data, instance=instance)
        # Проверяем полученные данные.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    # Метод для удаления записи.
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        # Если ключ есть, то удаляем запись из базы данных по ключу.

        return Response({"post": "delete post " + str(pk)})



'''class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    # Указываем класс сериализатор.
    serializer_class = WomenSerializer
'''
