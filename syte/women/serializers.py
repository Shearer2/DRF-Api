# Импортируем сериализаторы.
import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

'''
class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content
'''


# Указываем сериализатор, который работает с моделями.
'''class WomenSerializer(serializers.Serializer):
    """Сериализатор для знаменитых женщин."""

    # В сериализаиторе прописываем те же атрибуты, которые присутствуют и в классе WomenModel.
    # Чтобы сериализатор знал, что данная переменная является обычной строкой, необходимо использовать класс CharField.
    #title = serializers.CharField(max_length=255)
    #content = serializers.CharField()
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    # Метод для добавления данных.
    def create(self, validated_data):
        # Передаём распакованный словарь с данными. Данный словарь формируется при post запросе и проверке .is_valid.
        return Women.objects.create(**validated_data)

    # Метод для обновления записей в базе данных.
    # instance - это ссылка на объект модели, в данном случае на Women. А validated_data - это данные, которые
    # необходимо изменить в базе данных.
    def update(self, instance, validated_data):
        # Для заданного атрибута берём из словаря ключ с нужным значением, а если его нет, то возвращаем значение,
        # которое и так установлено.
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        # Сохраняем данные.
        instance.save()
        # Возвращаем объект instance.
        return instance

    def delete(self, pk):
        Women.objects.filter(pk=pk).delete()
'''
'''
    class Meta:
        model = Women
        # Поля, которые будем использовать для сериализации, они будут отправляться обратно пользователю.
        fields = ('title', 'cat')
'''

'''
# Функция для преобразования объектов класса WomenModel в json-формат.
def encode():
    model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
    # Пропускаем созданный объект через сериализатор.
    model_sr = WomenSerializer(model)
    # Объект сериализатор выводит полученные данные в виде data.
    print(model_sr.data, type(model_sr.data), sep='\n')
    # Представляем объект сериализтор в виде json строки.
    json = JSONRenderer().render(model_sr.data)
    print(json)


# Преобразование из json строки обратно.
def decode():
    # Имитируем поступление запроса от клиента.
    stream = io.BytesIO(b'{"title": "Angelina Jolie", "content": "Content: Angelina Jolie"}')
    # Для формирования словаря используем JSONParser.
    data = JSONParser().parse(stream)
    # Чтобы сериализатор декодировал данные необходимо использовать параметр data.
    serializer = WomenSerializer(data=data)
    # Проверяем корректность данных.
    serializer.is_valid()
    print(serializer.validated_data)
'''


# Для работы с моделями есть специальный сериализатор, в котором не нужно всё прописывать вручную,
# как при использовании Serializer.
class WomenSerializer(serializers.ModelSerializer):
    # Добавляем аттрибут пользователя, создаём скрытое поле и в нём по умолчанию прописывается текущий пользователь.
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        # Указываем какую модель используем.
        model = Women
        # Указываем поля для возвращения клиенту.
        #fields = ("title", "content", "cat")
        # Возвращение всех полей пользователю.
        fields = "__all__"
