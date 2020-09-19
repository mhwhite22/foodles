from django.contrib import admin
from .models import Recipe, Meal

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Meal)
