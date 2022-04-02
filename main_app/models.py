from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FinchToy(models.Model):
    name = models.CharField(max_length = 100)
    color = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


GENDER_CHOICES = (
    ("f", "female"),
    ("m", "male")
)

class Finch(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    finchtoys = models.ManyToManyField(FinchToy)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']




