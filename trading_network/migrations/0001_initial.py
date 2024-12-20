# Generated by Django 5.1.2 on 2024-10-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=250, verbose_name="Наименование"),
                ),
                (
                    "model",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="Модель"
                    ),
                ),
                (
                    "release_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата выхода на рынок"
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
