from django.db import models

# Create your models here.

class weather(models.Model):
    location = models.CharField(max_length=32)
    weather = models.CharField(max_length=32)
    temperature = models.IntegerField()

    def __str__(self):
        return self.location

    # 管理画面上で表示するときにweatherではなく、「天気情報」を表示
    class Meta:
        verbose_name = verbose_name_plural = '天気情報'
