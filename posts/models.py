from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length = 255)
    corpo = models.TextField()
    data_criacao = models.DateTimeField()
    
    class Meta:
        verbose_name = 'publicacao'
        verbose_name_plural = 'publicacoes'
    
    def __unicode__(self):
        
        return self.titulo
