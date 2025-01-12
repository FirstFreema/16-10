from django.db import models
from django.contrib.auth import get_user_model

class Breed(models.Model):
    """
    Модель для представления породы собак.

    Атрибуты:
        name (CharField): Название породы. Должно быть уникальным.
        description (TextField): Описание породы. Может быть пустым.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Название породы"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание породы"
    )

    def __str__(self):
        """
        Возвращает строковое представление породы.

        Returns:
            str: Название породы.
        """
        return self.name

    class Meta:
        """
        Метаданные для модели Breed:
        - verbose_name: Человекочитаемое название модели в единственном числе.
        - verbose_name_plural: Название модели во множественном числе.
        """
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    """
    Модель для представления собаки.

    Атрибуты:
        name (CharField): Имя собаки.
        age (PositiveIntegerField): Возраст собаки.
        breed (ForeignKey): Связь с моделью Breed, указывает породу собаки.
        image (ImageField): Фото собаки. Может быть пустым.
    """

    name = models.CharField(
        max_length=255,
        verbose_name="Имя собаки"
    )
    age = models.PositiveIntegerField(
        verbose_name="Возраст"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name='dogs',
        verbose_name="Порода"
    )
    image = models.ImageField(
        upload_to='dog_photos/',
        null=True,
        blank=True,
        verbose_name="Фото собаки"
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_dogs',
        verbose_name="Владелец",
        null = True
    )

    def __str__(self):
        """
        Возвращает строковое представление собаки.

        Returns:
            str: Имя собаки.
        """
        return self.name

    class Meta:
        """
        Метаданные для модели Dog:
        - verbose_name: Человекочитаемое название модели в единственном числе.
        - verbose_name_plural: Название модели во множественном числе.
        """
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

from django.db import models

class Pedigree(models.Model):
    pet = models.ForeignKey('Dog', on_delete=models.CASCADE, related_name='pedigree')
    ancestor_name = models.CharField(max_length=255, verbose_name='Имя предка')
    relationship = models.CharField(max_length=100, verbose_name='Степень родства', blank=True, null=True)
    birth_year = models.PositiveIntegerField(verbose_name='Год рождения', blank=True, null=True)

    def __str__(self):
        return f"{self.ancestor_name} ({self.relationship})"

