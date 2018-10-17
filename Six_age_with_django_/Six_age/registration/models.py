from django.db import models


class UserDetails(models.Model):
    Username = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

    class Meta:
        db_table = "User_Details"
