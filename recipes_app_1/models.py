from django.db import models

# Create your models here.



class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100,null=True, blank=True)
    recipe_desc = models.TextField(default='')
    recipe_image = models.ImageField(upload_to='Images', null=True, blank=True)


def __str__(self):
    return f'{self.id} {self.recipe_name}'
