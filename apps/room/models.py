from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

from store.models import Store

class Room(models.Model):
    slug = models.SlugField(unique=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, db_column='client')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='store')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    class Meta:
        db_table = 'rooms'

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE, db_column='room')
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, db_column='user')
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    class Meta:
        ordering = ('created_at',)
        db_table = 'messages'
        