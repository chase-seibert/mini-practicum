from framework import models


class User(models.Model):
    username = models.CharField(len=255)
    password = models.CharField(len=255)
    full_name = models.CharField(len=255, null=True)

    def get_first_name(self):
        return self.full_name.split(' ')[0]

    @staticmethod
    def create(username, password):
        user = User()
        user.username = username
        user.password = password
        user.save()
        return user

