from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Bet(models.Model):
    item = models.ManyToManyField('Item')
    max_bet = models.DecimalField( max_digits=5, decimal_places=2)
    max_bet_user = models.ForeignKey(User, on_delete=models.PROTECT)

class Item(models.Model):
    photo = models.CharField(max_length=2048)
    price_begin = models.DecimalField( max_digits=5, decimal_places=2)
    create_time = models.TimeField( auto_now_add=True)
    create_user = models.ForeignKey(User, on_delete=models.PROTECT)
    bet_id = models.ForeignKey(Bet, on_delete=models.PROTECT, related_name='+')
    category = models.ManyToManyField('Category')
    is_active = models.BooleanField(default="True")
    description = models.CharField(max_length=4096, default=None)

class Comment(models.Model):
    author = models.ManyToManyField(User)
    message = models.CharField(max_length=2048)
    create_time = models.TimeField( auto_now_add=True)

class Category(models.Model):
    category_name = models.CharField(max_length=64)
    
    def __str__(self):
        return F"{self.category_name}"

class Watchlist(models.Model):
    item = models.ManyToManyField(Item)
    user = models.ManyToManyField(User)
