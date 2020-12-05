from django.db import models


class Vk_Category(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=False, blank=True)
    profile_link = models.CharField(verbose_name="ссылка на профиль", max_length=128, unique=True)

    def __str__(self):
        return self.name