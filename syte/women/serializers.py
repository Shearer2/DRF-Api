# Импортируем сериализаторы.
from rest_framework import serializers
from .models import Women


# Указываем сериализатор, который работает с моделями.
class WomenSerializer(serializers.ModelSerializer):
    """Сериализатор для знаменитых женщин."""

    class Meta:
        model = Women
        # Поля, которые будем использовать для сериализации, они будут отправляться обратно пользователю.
        fields = ('title', 'cat')

