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
class WomenSerializer(serializers.Serializer):
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
    # Чтобы сериализатор декодировал данные необъодимо использовать параметр data.
    serializer = WomenSerializer(data=data)
    # Проверяем корректность данных.
    serializer.is_valid()
    print(serializer.validated_data)
'''