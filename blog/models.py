from django.db import models

class Post(models.Model):
    autor = models.CharField(max_length = 100)
    titulo = models.CharField(max_length = 100)
    resumo = models.CharField(max_length = 250)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.titulo
