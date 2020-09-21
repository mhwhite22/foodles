from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.



MAIN_INGREDIENT = (
    ('C', 'Chicken'),
    ('P', 'Pork'),
    ('B', 'Beef'),
    ('F', 'Fish'),
    ('S', 'Shellfish'),
    ('L', 'Lamb'),
    ('N', 'Pasta'),
    ('V', 'Vegetarian'),
)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    instructions = models.TextField()
    favorite = models.BooleanField(default=False)
    main_ingredient = models.CharField(
        max_length=1,
        choices=MAIN_INGREDIENT,
        default=MAIN_INGREDIENT[0][0]
    )    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipes_detail', kwargs={'pk': self.id})

class Meal(models.Model):
    date = models.DateField('meal date')
    recipe = models.ManyToManyField(Recipe)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})


