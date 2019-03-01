from django.db import models
import ModifierWatch

class ItemWatch(models.Model):
    category = models.CharField(max_length=30)
    price = models.IntegerField
    currency = models.CharField(max_length=30)
    modifiers = models.OneToManyField(ModifierWatch)
