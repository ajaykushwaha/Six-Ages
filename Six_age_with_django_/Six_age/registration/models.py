from django.db import models


class UserDetails(models.Model):
    Username = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Avatar_image = models.CharField(max_length=50)
    is_admin = models.IntegerField(default=0)

    class Meta:
        db_table = "User_Details"


class Avatars(models.Model):
    avatar_image_name = models.CharField(max_length=50)

    class Meta:
        db_table = "avatar"
