from django.db import models


class Greeting(models.Model):
    class Meta:
        verbose_name = 'greeting'
        verbose_name_plural = 'greeting'

    name = models.CharField('name', max_length=255)
    time = models.CharField('time', max_length=255)

    def __str__(self):
        return self.name
