from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class UsuarioPersonalizado(AbstractUser):   
    """ 
    modelo de usuário personalizado para adicionar novos campos data_de_nascimento
    e numero_telefone para coletar informações adicionais do usuário. 
    """
    data_de_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de nascimento')
    numero_telefone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Número de telefone')
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='usuarios'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='usuarios'
    )

    def __str__(self):
        return self.username