from django.db import models
from django.utils import timezone


class Post(models.Model): # define o nosso modelo (é um objeto). Class indica que está se definindo um objeto, post é o nome do modelo (sempre começar com letra maiuscula), models.Model significa que é um modelo de django
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title