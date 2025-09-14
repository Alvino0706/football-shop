import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('update', 'Update'),
        ('sepatu', 'Sepatu'),
        ('topi', 'Topi'),
        ('celana', 'Celana'),
        ('botol minum', 'Botol Minum'),
    ]

    CONDITION_CHOICES = [
        ('baru', 'Baru'),
        ('bekas', 'Bekas'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    stock =  models.PositiveIntegerField(default=0)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='baru')
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
