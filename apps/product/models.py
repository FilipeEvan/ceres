from django.db import models
from datetime import datetime

from store.models import Store

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING, db_column='store')
    name = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50)
    quantity = models.CharField(max_length = 25)
    price = models.FloatField()
    description = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    created_at = models.DateField(default=datetime.now, blank=True)
    
    class Meta:
        db_table = 'products'
