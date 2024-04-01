from django.forms import model_to_dict
from django.shortcuts import render
# Импортируем generics
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


# Класс APIView является базовым классом django rest framework.
'''class WomenAPIView(APIView):
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

        # Пробуем взять нужную запись из модели Women.
        try:
            instance = Women.objects.get(pk=pk)
        # Если была указана не существующая запись, то возвращаем исключение.
        except:
            return Response({"error": "Method PUT not allowed"})
        # Если ключ есть, то удаляем запись из базы данных по ключу.
        Women.objects.filter(pk=pk).delete()
        return Response({"post": "delete post " + str(pk)})
'''

'''
# Используем ListCreateAPIView для чтения по get-запросу и создания списка данных по post-запросу.
# Его можно применять чтобы не прописывать всё в ручную, как при использовании APIView.
class WomenAPIList(generics.ListCreateAPIView):
    # Возвращаем список записей клиенту.
    queryset = Women.objects.all()
    # Сериализатор для применения к данным.
    serializer_class = WomenSerializer


# Класс UpdateAPIView меняет записи по put или patch запросу.
class WomenAPIUpdate(generics.UpdateAPIView):
    # Указываем выбирать все записи, но класс сам обрабатывает записи и возвращает только одну нужную, а не все.
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# Класс RetrieveUpdateDestroyAPIView получает данные, меняет или удаляет их.
class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
'''

'''
# Viewset для замены функционала APIView и сокращения кода.
class WomenViewSet(viewsets.ModelViewSet):
    #queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # Чтобы возвращать не только все записи, но и какие-то определённые можно переопределить данный метод.
    def get_queryset(self):
        # Делаем возможность получения одной записи. Сначала получаем ключ pk.
        pk = self.kwargs.get("pk")
        # Если pk нет, то возвращаем три последние записи, а если есть, то возвращаем список из одной записи.
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)

    # Добавляем декоратор для создания новых маршрутов, первым параметром указываем список поддерживаемых запросов,
    # второй параметр при значении False возвращает все записи, а при значении True только одну запись и нужно указать
    # параметр pk в функции. Имя маршрута берётся с названия функции.
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        # В комментариях код для вывода всех записей.
        #cats = Category.objects.all()
        #return Response({'cats': [c.name for c in cats]})
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
'''

'''class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    # Указываем класс сериализатор.
    serializer_class = WomenSerializer
'''


class WomenAPIList(generics.ListCreateAPIView):
    """Возвращение списка статей."""

    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # Указываем классы для ограничения доступа, добавление новых данных доступно только авторизованных пользователей,
    # а для всех остальных доступно только чтение.
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    """Изменение определённой записи."""

    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # Возможность менять запись только автору данной записи, а остальные пользователи могут только просматривать.
    #permission_classes = (IsOwnerOrReadOnly,)
    # Возможность просматривать записи только авторизованным пользователям.
    permission_classes = (IsAuthenticated, )
    # Предоставляем доступ к данным только тем пользователям, которые заходят по токенам.
    # Необходимо закомментировать данную строку, так как она запрашивает аутентификацию по токену, а не по jwt токену.
    #authentication_classes = (TokenAuthentication,)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    """Удаление определённой записи."""

    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # Указываем ограничение удаления записей, можно удалять только администратору.
    permission_classes = (IsAdminOrReadOnly,)
