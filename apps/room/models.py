from django.db import models
from django.contrib.auth.models import User

from store.models import Store


class Room(models.Model):
    slug = models.SlugField(unique=True)
    client = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='client')
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING, db_column='store')
    
    class Meta:
        db_table = 'rooms'