from django.db import models

# Create your models here.
class recipeModel(models.Model):
    recipeTitle = models.CharField(max_length=100)
    recipeDescription = models.TextField()
    recipeIngredients = models.TextField()
    recipeInstructions = models.TextField()
    recipeImage = models.ImageField(upload_to='media/recipe')