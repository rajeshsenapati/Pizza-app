from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class StorsModel(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class PizaModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    stors = models.ForeignKey(StorsModel, on_delete=models.CASCADE, related_name="pizza_list")
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ReviewModel(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    pizzalist = models.ForeignKey(PizaModel, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)