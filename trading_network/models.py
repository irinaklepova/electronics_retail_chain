from django.db import models

from config.settings import NULLABLE


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=250, verbose_name="Наименование")
    model = models.CharField(max_length=250, **NULLABLE, verbose_name="Модель")
    release_date = models.DateField(**NULLABLE, verbose_name="Дата выхода на рынок")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("title",)


class Contact(models.Model):
    """Модель контакта"""
    email = models.EmailField(max_length=70, verbose_name="Email")
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, **NULLABLE, verbose_name="Улица")
    house_number = models.PositiveIntegerField(max_length=10, **NULLABLE, verbose_name="Номер дома")

    def __str__(self):
        return f"{self.email} {self.city} {self.country}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ("city", "country",)
