from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'toy_id': self.id})


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    temperment = models.TextField(max_length=250)
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})



class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    class Meta:
        ordering = ('-date', 'meal')


# Create your models here.
