"""Tests for python functions"""

# from crud import create_household, get_household_by_login, get_household_id_by_name, create_user
import crud
from model import db, Household, Users, Tasks, connect_to_db, db
from unittest import TestCase
from server import app

import unittest

# def create_test_data():
#     """creates fake data for testing"""

#     house100 = Household(account_login="house100", account_password="test100")
#     user100 = Users(user_name="user100", cellphone="555-555-1234")
#     task100 = Tasks(task_name="test_task", completed=False, frequency="daily")

#     db.session.add_all(house100, user100, task100)
#     db.session.commit()


class TestCrud(TestCase):
    """crud functions tests"""

    # def setUp(self):
    #     """Set up the test"""

    #     self.client = app.test_client()
    #     app.config['TESTING'] = True
    #     connect_to_db(app, "postgresql:///test_db")
    #     db.create_all()
    #     create_test_data()

    # def tearDown(self):
    #     """Tear down the test"""

    #     db.session.remove()
    #     db.drop_all()
    #     db.engine.dispose()

    def test_create_household(self):
        """Tests create_household function"""

        result = crud.create_household("house11", "test11")
        self.assertIsNotNone(result.account_login)
    
    def test_create_user(self):
        """Tests create_user function"""

        result = crud.create_user(11, "user11", "555-555-1234")
        self.assertIsNotNone(result.user_name)

    def test_get_household_by_login(self):
        result = crud.get_household_by_login("house1")
        print(result)
        self.assertIsNotNone(result.account_login)

# if __name__ == "__main__":
#     unittest.main()
#     print("Everything passed")




# def test_get_household_by_login():
#     result = get_household_by_login("house11")
#     assert result.account_login == "house11", "should be house11"

# def test_get_household_id_by_name():
#     result = get_household_id_by_name("house11")
#     assert result == 11, "should be 11"



if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    unittest.main()
    # test_create_household()
    # test_get_household_by_login()
    # test_get_household_id_by_name()
    # test_create_user()