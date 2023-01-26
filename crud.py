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

def get_household_id_by_name(household_name):
    """Return a household id, given a name"""

    household = Household.query.filter(Household.account_login == household_name).first()
    household_id = household.household_id

    return household_id

def create_user(household_id, user_name):
    """Create and return a new user"""

    user = Users(household_id=household_id, user_name=user_name)

    return user

def get_user_by_name(user_name):
    """Return a user by name"""

    return Users.query.filter(Users.user_name == user_name).first()

def get_users_by_household(household_name):
    """Return a list of user names for given household"""
    
    household = Household.query.filter(Household.account_login == household_name).first()
    user_list = []
    for user in household.users:
        user_list.append(user.user_name)

    return user_list

def create_task(task_name, user_assigned, frequency):
    """Create and return a new task"""

    task = Tasks(task_name=task_name, user_id=user_assigned, frequency=frequency)

    return task

def get_tasks(user_assigned):
    """Get list of tasks assigned to selected user"""

    user = Users.query.filter(Users.user_name == user_assigned).first()
    user_id = user.user_id
    # change below to .all() and need to unpack list returned
    tasks = Tasks.query.filter(Tasks.user_id == user_id).first()
    
    return tasks.task_name


if __name__ == '__main__':
    from server import app
    connect_to_db(app)