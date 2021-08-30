from django.db import models

from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse #reverse - get_absolute_url.
from datetime import datetime, date

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    tag_titulo = models.CharField(max_length=255, default="Blog")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id))) #devuelve el articulo creado por el arg(id)
    
