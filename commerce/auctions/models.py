from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Bets(models.Model):
    item = models.ForeignKey('Items',  on_delete=models.PROTECT)
    max_bet = models.DecimalField( max_digits=5, decimal_places=2)
    max_bet_user = models.ForeignKey(User, on_delete=models.PROTECT)

class Items(models.Model):
    photo = models.CharField(max_length=2048)
    price_begin = models.DecimalField( max_digits=5, decimal_places=2)
    create_time = models.TimeField( auto_now_add=True)
    create_user = models.ForeignKey(User, on_delete=models.PROTECT)
    bet_id = models.ForeignKey(Bets, on_delete=models.PROTECT)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    message = models.CharField(max_length=2048)
    create_time = models.TimeField( auto_now_add=True)

class Categories(models.Model):
    name = models.CharField(max_length=64)

class Watchlist(models.Model):
    item = models.ForeignKey(Items, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
