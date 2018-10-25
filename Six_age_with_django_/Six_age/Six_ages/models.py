from django.db import models
from registration.models import UserDetails


class Game(models.Model):
    game_images = models.CharField(max_length=100)
    game_swf = models.CharField(max_length=100)
    game_type = models.CharField(max_length=100)
    game_rating = models.IntegerField(max_length=5)
    comment = models.CharField(max_length=300)
    game_display_name = models.CharField(max_length=100)
    class Meta:
        db_table = "Game_Details"


class Comments(models.Model):
    comment = models.CharField(max_length=300)
    game_name = models.CharField(max_length=40)
    Username = models.CharField(max_length=40)

    class Meta:
        db_table = "Comments"

