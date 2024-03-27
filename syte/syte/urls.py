"""
URL configuration for syte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Импорт контроллера с сериализатором.
from women.views import *
# Чтобы определить набор стандартных маршрутов для viewset необходимо импортировать routers.
from rest_framework import routers

'''
# Создаём объект класса.
router = routers.DefaultRouter()
# Регистрируем в роутере наш класс viewset, первым аргументом указываем префикс для набора маршрутов,
# а вторым аргументом указываем наш класс с viewset.
# basename нужен для формирования имён маршрута, по умолчанию он берёт имя модели из queryset во views.
router.register(r'women', WomenViewSet, basename='women')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Чтобы не прописывать каждый маршрут вручную можно использовать роутеры.
    # Используем все маршруты, которые находятся в коллекции urls. Последним указывается используемый префикс.
    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/
    # Для viewset можно прописывать словарь в .as_view(), в качестве ключа указывается метод для обработки запроса,
    # а в качестве значения метод, который будет вызываться в самом viewset для обработки данного запроса.
    #path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    #path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    #path('api/v1/womenlist/', WomenAPIList.as_view()),
    # Указываем целочисленное значение идентификатора записи, которую нам нужно поменять.
    #path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    #path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
]
