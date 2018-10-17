from django.db import models


class Game(models.Model):
    game_images = models.CharField(max_length=40)
    game_swf = models.CharField(max_length=40)
    game_type = models.CharField(max_length=40)
    game_rating = models.IntegerField(max_length=5)
    game_comments = models.CharField(max_length=200)
    game_display_name = models.CharField(max_length=40)
    class Meta:
        db_table = "Game_Details"