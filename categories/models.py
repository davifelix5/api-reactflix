from django.db import models
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=7, validators=[
        RegexValidator(
            regex=r'^#(?:[0-9a-fA-F]{3}){2}$',
            message='Cor inválida'
        )
    ])
    priority = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.name
