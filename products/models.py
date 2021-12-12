from django.db import models

# Create your models here.
class Categories(models.Model):
 menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
 name = models.CharField(max_length=45)
					
class Menu(models.Model):
 name = models.CharField(max_length=45)

class Drinks(models.Model):
 category = models.ForeignKey('Categories', on_delete=models.CASCADE)
 korean_name = models.CharField(max_length=45)
 english_name = models.CharField(max_length=45)
 description = models.TextField()

class Images(models.Model):
 drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)
 image_url = models.CharField(max_length=2000)

class Allergy(models.Model):
 name = models.CharField(max_length=45)

class Sizes(models.Model):
 name = models.CharField(max_length=45)
 size_ml = models.CharField(max_length=45, null=True)
 size_fluid_ounce = models.CharField(max_length=45, null=True)

class Allergy_drink(models.Model):
 allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
 drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)

class Nutritions(models.Model): 
 drink = models.ForeignKey('Drinks', on_delete=models.CASCADE, null=True)
 
 size = models.ForeignKey('Sizes', on_delete=models.CASCADE, null=True)
 
 one_serving_kca = models.DecimalField(max_digits = 10, decimal_places = 2, null=True) 

 sodium_mg = models.DecimalField(max_digits = 10, decimal_places = 2, null=True) 
 saturated_fat_g = models.DecimalField(max_digits = 10, decimal_places = 2, null=True) 
 
 sugars_g = models.DecimalField(max_digits = 10, decimal_places = 2, null=True) 
 
 protein_g = models.DecimalField(max_digits = 10, decimal_places = 2, null=True) 
 caffeine_mg = models.DecimalField(max_digits = 10, decimal_places = 2, null=True) 
 

 
