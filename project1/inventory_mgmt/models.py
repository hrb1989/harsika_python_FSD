from django.db import models

# Create your models here.

class Inventory(models.Model):
    category = models.CharField(max_length=15,null=False, blank="False")
    name = models.CharField(max_length=30,null=False, blank="False")
    pricePerGram = models.FloatField()
    pricePerPiece = models.FloatField()
    availableQtyGrams = models.FloatField()
    availableQtyPieces = models.IntegerField()

    class Meta:
        verbose_name_plural = "Inventory"