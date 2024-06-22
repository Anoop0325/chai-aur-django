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
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username} reviews for {self.chai.name}'
    


# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name
    

# One to One
class Certificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_util = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai}'
    