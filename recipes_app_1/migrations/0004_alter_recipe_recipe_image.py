# Generated by Django 5.0.2 on 2024-02-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app_1', '0003_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(blank=True, null=True, upload_to='Images'),
        ),
    ]
