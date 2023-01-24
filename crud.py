"""Crud operations."""
# waiting for data model approval before coding

from model import db, Household, Users, Tasks, connect_to_db

# functions start here
def create_household(login, password):
    """Create and return a new household."""

    household = Household(account_login=login, account_password=password)

    return household

def create_user(household_id, user_name):
    """Create and return a new user"""

    user = Users(household_id=household_id, user_name=user_name)

    return user

def create_task(task_name):
    """Create and return a new task"""

    task = Tasks(task_name=task_name)

    return task

if __name__ == '__main__':
    from server import app
    connect_to_db(app)