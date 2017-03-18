from django.db import models
from django.utils import timezone
# Create your models here.

class Recipe(models.Model):
	name = models.CharField(max_length=300, verbose_name="Recipe Name")
	author = models.ForeignKey('auth.User')		
	instructions = models.TextField(verbose_name="Recipe Instructions")
	source = models.URLField(blank=True, verbose_name="Recipe Source URL")
	created_date = models.DateTimeField(default=timezone.now)
	servingsize = models.IntegerField(verbose_name="Serving Size")

class RecipeIngredients(models.Model):
	recipe = models.ForeignKey('Recipe',on_delete=models.CASCADE)
	ingredient = models.CharField(max_length=100)
	qty = models.FloatField()
	units = models.CharField(max_length=50)


