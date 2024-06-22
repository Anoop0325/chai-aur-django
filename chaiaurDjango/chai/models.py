from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class ChaiVarity(models.Model):
    ChaiType = [
        ('ML', 'Masala'),
        ('GR', 'Ginger'),
        ('KI', 'Kiwi'),
        ('PL', 'Plain'),
        ('EL', 'Elaichi'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=ChaiType)
    description  = models.TextField(default='')

    def __str__(self):
        return self.name
    

#One to many
# class ChaiReview(models.Model):
    