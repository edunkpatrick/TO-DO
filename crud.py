"""Crud operations."""

from model import db, Household, Users, Tasks, connect_to_db
from datetime import datetime

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

    household = Household.query.filter(Household.account_login == household_name).first()
    household_id = household.household_id

    return Users.query.filter(Users.user_name == user_name, Users.household_id == household_id).first()


def get_user_id(user_name, household_id):
    """Return a user id given a name and household id"""    

    household = Household.query.filter(Household.household_id == household_id).first()
    household_id = household.household_id

    user = Users.query.filter(Users.user_name == user_name, Users.household_id == household_id).first()
    user_id = user.user_id

    return user_id


def get_users_by_household(household_name):
    """Return a list of user names for given household"""
    
    household = Household.query.filter(Household.account_login == household_name).first()
    user_list = []
    for user in household.users:
        user_list.append(user.user_name)

    return user_list


def create_task(task_name, user_id, household_id, completed, frequency):
    """Create and return a new task"""

    task = Tasks(task_name=task_name, user_id=user_id, household_id = household_id, completed=completed, frequency=frequency)

    return task


# FIRST CODE REVIEW 1/25/23 FINISHED HERE #

def get_tasks(user_assigned, household_name):
    """Get list of tasks assigned to selected user"""

    house_name = Household.query.filter(Household.account_login == household_name).first()
    house_id = house_name.household_id

    user = Users.query.filter(Users.user_name == user_assigned, Users.household_id == house_id).first()
    user_id = user.user_id

    tasks = Tasks.query.filter(Tasks.user_id == user_id, Tasks.completed != True).all()

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
    completed_task.date_completed = datetime.now()

    return completed_task

# 2.0 FUNCTIONS FOR CHARTS - IN PROGRESS
def get_count_of_tasks(user_id):
    """Returns a list of tuples of all tasks completed for chartsjs"""
    
    tasks = Tasks.query.filter(Tasks.user_id == user_id, Tasks.completed == True).all()

    frequency = []
    for task in tasks:
        frequency.append(task.frequency)

    as_needed_comp = 0
    daily_comp = 0
    weekly_comp = 0
    monthly_comp = 0

    for item in frequency:
        if item == "as_needed":
            as_needed_comp += 1
        elif item == "daily":
            daily_comp += 1
        elif item == "weekly":
            weekly_comp += 1
        elif item == "monthly":
            monthly_comp += 1

    freq_tasks_dict = {}
    freq_tasks_dict["as_needed"] = as_needed_comp
    freq_tasks_dict["daily"] = daily_comp
    freq_tasks_dict["weekly"] = weekly_comp
    freq_tasks_dict["monthly"] = monthly_comp

    list_for_chart = [(freq, count) for freq, count in freq_tasks_dict.items()]

    return list_for_chart

# IN PROGRESS
def get_range(user_id, date1, date2):
    """Returns a list of tuples of all tasks completed for chartsjs"""
    
    tasks = Tasks.query.filter(Tasks.user_id == user_id, Tasks.completed == True, Tasks.date_completed > date1, Tasks.date_completed <= date2).all()

    frequency = []
    for task in tasks:
        frequency.append(task.frequency)

    as_needed_comp = 0
    daily_comp = 0
    weekly_comp = 0
    monthly_comp = 0

    for item in frequency:
        if item == "as_needed":
            as_needed_comp += 1
        elif item == "daily":
            daily_comp += 1
        elif item == "weekly":
            weekly_comp += 1
        elif item == "monthly":
            monthly_comp += 1

    freq_tasks_dict = {}
    freq_tasks_dict["as_needed"] = as_needed_comp
    freq_tasks_dict["daily"] = daily_comp
    freq_tasks_dict["weekly"] = weekly_comp
    freq_tasks_dict["monthly"] = monthly_comp

    list_for_chart = [(freq, count) for freq, count in freq_tasks_dict.items()]

    return list_for_chart

# FORMER CRUD FUNCTIONS NOT IN USE
# def clear_task(task_name):
#     """Clears task from list"""

#     completed_task = Tasks.query.filter(Tasks.task_name == task_name, Tasks.completed == True).first()

#     return completed_task

if __name__ == '__main__':
    from server import app
    connect_to_db(app)