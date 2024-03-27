from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Класс для ограничения прав доступа. Если пользователь является администратором, то он может удалять запись,
    иначе доступно только чтение."""

    def has_permission(self, request, view):
        # Если запрос является безопасным, то предоставляем права доступа для всех.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Если запрос не является безопасным, то предоставляем права доступа только администратору.
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Класс для возможности изменения записи только тому пользователю, который эту запись создал,
    все остальные пользователи могут только читать её."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Если пользователь из базы данных равен пользователю, который отправляет запрос, то возвращаем True,
        # а иначе False.
        return obj.user == request.user