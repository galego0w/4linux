from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100,blank=True,null=True)
    conteudo = models.TextField(blank=True,null=True)
    data_criado = models.DateTimeField(default=timezone.now())
    data_post = models.DateTimeField(blank=True,null=True)

    def publica(self):
        self.data_post = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
