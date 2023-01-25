"""Crud operations."""


from model import db, Household, Users, Tasks, connect_to_db

# functions start here

def create_household(login, password):
    """Create and return a new household."""

    household = Household(account_login=login, account_password=password)

    return household

def get_household_by_login(household_login):
    """Return a household by name"""

    return Household.query.filter(Household.account_login == household_login).first()

def create_user(household_id, user_name):
    """Create and return a new user"""

    user = Users(household_id=household_id, user_name=user_name)

    return user

def create_task(task_name, user_assigned, frequency):
    """Create and return a new task"""

    task = Tasks(task_name=task_name, user_id=user_assigned, frequency=frequency)

    return task

if __name__ == '__main__':
    from server import app
    connect_to_db(app)