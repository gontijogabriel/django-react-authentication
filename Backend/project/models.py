from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128, null=False, blank=False)  # Usar um campo de tamanho suficiente para armazenar o hash

    def save(self, *args, **kwargs):
        # Hash da senha antes de salvar
        if not self.pk:  # Apenas ao criar um novo registro
            self.password = make_password(self.password)
        super().save(*args, **kwargs)