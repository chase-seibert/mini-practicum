from framework import models


class User(models.Model):
    username = models.CharField(len=255)
    password = models.CharField(len=255)
    full_name = models.CharField(len=255)

