import unittest

from app.models import ItemModel
from app.models import UserModel

from app import create_app, db
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # def test_password_hashing(self):
    #     u = UserModel('harry', 'potter')
    #     self.assertFalse(u.check_password('dog'))
    #     self.assertTrue(u.check_password('potter'))

    # def test_item(self):
    #     u = UserModel('harry', 'potter')
    #     i = ItemModel('orange',10,13,u.username)
    #     u.save_to_db()
    #     i.save_to_db()
    #     item = ItemModel.find_by_name(i.name,u.username)
    #     self.assertTrue(item.name,i.name)

    # def test_update_price_stock(self):
    #     u = UserModel('harry', 'potter')
    #     i = ItemModel('orange', 10, 13, u.username)
    #     u.save_to_db()
    #     i.save_to_db()
    #     i.price = 20
    #     i.stock = 15
    #     i.save_to_db()
    #     self.assertNotEqual(10, i.price)
    #     self.assertNotEqual(13,i.stock)


if __name__ == '__main__':
    unittest.main(verbosity=2)
