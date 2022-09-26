from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length = 100)
    district = models.CharField(max_length = 150)
    address = models.CharField(max_length = 50)
    number = models.CharField(max_length = 20)
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 15)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user')

    class Meta:
        db_table = 'stores'