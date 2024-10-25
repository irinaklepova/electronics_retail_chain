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
