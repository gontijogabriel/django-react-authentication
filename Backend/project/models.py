from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.nome