import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('celana', 'Celana'),
        ('joggers', 'Joggers'),
        ('kaus kaki', 'Kaus Kaki'),
        ('bola', 'Bola'),
        ('lainnya', 'Lainnya'),
    ]
    
    name = models.CharField
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

