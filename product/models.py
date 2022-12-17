from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ProductMainModel(models.Model):
    
    class SizeChoice(models.TextChoices):
        TEN = '10', _('10')
        TWENTY = '20', _('20')
        THIRTY = '30', _('30')
        
    class QualityChoice(models.TextChoices):
        HIGH = 'HIGH', _('HIGH')
        LOW = 'LOW', _('LOW')
        MEDIUM = 'MEDIUM', _('MEDIUM')
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    unique_code = models.CharField(max_length=20, unique=True)
    size = models.CharField(max_length=10, choices=SizeChoice.choices)
    quality = models.CharField(max_length=10, choices=QualityChoice.choices)
    
    def __str__(self):
        return self.title
    
    
class ProductColourModel(models.Model):
    
    class ColourChoice(models.TextChoices):
        RED = 'RED', _('RED')
        BLUE = 'BLUE', _('BLUE')
        GREEN = 'GREEN', _('GREEN')
        BLACK = 'BLACK', _('BLACK')

    product = models.ForeignKey(to=ProductMainModel, on_delete=models.CASCADE)
    colour = models.CharField(max_length=20, choices=ColourChoice.choices)
    
    def __str__(self):
        return self.colour
    

class ProductImageModel(models.Model):
    
    product = models.ForeignKey(to=ProductMainModel, on_delete=models.CASCADE)
    image = models.URLField()
    
    def __str__(self):
        return self.image
