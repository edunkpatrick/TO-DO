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

def get_user_by_name(user_name, household_name):
    """Return a user by name"""
    # need to change so that it returns a name from selected household
    household = Household.query.filter(Household.account_login == household_name).first()
    household_id = household.household_id
    return Users.query.filter(Users.user_name == user_name, Users.household_id == household_id).first()

def get_user_id(user_name):
    """Return a user id given a name"""
    user = Users.query.filter(Users.user_name == user_name).first()
    user_id = user.user_id

    return user_id

def get_users_by_household(household_name):
    """Return a list of user names for given household"""
    
    household = Household.query.filter(Household.account_login == household_name).first()
    user_list = []
    for user in household.users:
        user_list.append(user.user_name)

    return user_list

def create_task(task_name, user_assigned, completed, frequency):
    """Create and return a new task"""

    # user = Users.query.filter(Users.user_id == user_assigned)
    # user_household = user.household_id

    task = Tasks(task_name=task_name, user_id=user_assigned, completed=completed, frequency=frequency)

    return task

# FIRST CODE REVIEW 1/25/23 FINISHED HERE #

def get_tasks(user_assigned):
    """Get list of tasks assigned to selected user"""

    user = Users.query.filter(Users.user_name == user_assigned).first()
    # get user_id for user_assigned entered
    user_id = user.user_id

    # query for all uncompleted tasks assigned to that user_id
    tasks = Tasks.query.filter(Tasks.user_id == user_id, Tasks.completed != True).all()

    # unpack query list and put each task_name into a list
    tasks_list = []
    for task in tasks:
        tasks_list.append(task.task_name)

    return tasks_list

def delete_task(user_name, task_name):
    """Delete selected task from list"""

    user = Users.query.filter(Users.user_name == user_name).first()
    user_id = user.user_id
    deleted_task = Tasks.query.filter(Tasks.task_name == task_name, Tasks.user_id == user_id).first()

    return deleted_task

def complete_task(user_name, task_name):
    """Marks task complete"""

    user = Users.query.filter(Users.user_name == user_name).first()
    user_id = user.user_id
    completed_task = Tasks.query.filter(Tasks.task_name == task_name, Tasks.user_id == user_id).first()
    completed_task.completed = True

    return completed_task

def clear_task(task_name):
    """Clears task from list"""

    completed_task = Tasks.query.filter(Tasks.task_name == task_name, Tasks.completed == True).first()

    return completed_task

def get_count_of_tasks(user_id):
    """Returns a tuple of tasks, frequency per user"""
    
    tasks = Tasks.query.filter(Tasks.user_id == user_id, Tasks.completed == True).all()

    completed_list = []
    for task in tasks:
        completed_list.append(task.task_name)

    frequency = []
    for task in tasks:
        frequency.append(task.frequency)

    merge = [(completed_list[i], frequency[i]) for i in range(0, len(completed_list))]
    print('this is merge', merge)

    return


if __name__ == '__main__':
    from server import app
    connect_to_db(app)