from framework import models


class User(models.Model):
    username = models.CharField(len=255)
    password = models.CharField(len=255)
    full_name = models.CharField(len=255)

    @staticmethod
    def create(username, password):
        user = User()
        user.username = username
        user.password = password
        user.save()
        return user

