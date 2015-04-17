import unittest
from myapp.models import User


class TestUserModel(unittest.TestCase):

    def test_save(self):
        user = User.create('foobar', 'bat')
        self.assertEquals(user.username, 'foobar')
        self.assertEquals(user.password, 'bat')

    def test_full_name(self):
        user = User.create('foobar', 'bat')
        user.full_name = 'Barry Bonds'
        self.assertEquals(user.first_name, 'Barry')
