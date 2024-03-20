from django.contrib import admin
from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    """Список знаменитых женщин."""

    list_display = ('title', 'cat')
    ordering = ('pk',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Список профессий."""

    list_display = ('name',)
    ordering = ('name',)

