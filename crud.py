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

def create_task(task_name, user_id, completed, frequency):
    """Create and return a new task"""

    task = Tasks(task_name=task_name, user_id=user_id, completed=completed, frequency=frequency)

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

    return completed_task

# def clear_task(task_name):
#     """Clears task from list"""

#     completed_task = Tasks.query.filter(Tasks.task_name == task_name, Tasks.completed == True).first()

#     return completed_task

def get_count_of_tasks(user_id):
    """Returns a dictionary of # tasks completed"""
    get_user = Users.query.filter(Users.user_id == user_id).first()
    user_name = get_user.user_name
    tasks = Tasks.query.filter(Tasks.user_id == user_id, Tasks.completed == True).all()

    # name of all tasks, mabye not needed:
    # completed_list = []
    # for task in tasks:
    #     completed_list.append(task.task_name)

    frequency = []
    for task in tasks:
        frequency.append(task.frequency)

    num_times = [5, 7, 6, 9, 3, 4, 2, 1]
    # as_needed_comp = 0
    # daily_comp = 0
    # weekly_comp = 0
    # monthly_comp = 0

    # for item in frequency:
    #     if item == "as needed":
    #         as_needed_comp += 1
    #     elif item == "daily":
    #         daily_comp += 1
    #     elif item == "weekly":
    #         weekly_comp += 1
    #     elif item == "monthly":
    #         monthly_comp += 1

    # freq_tasks_dict = {}
    # freq_tasks_dict["user"] = user_name
    # # freq_tasks_dict["as needed"] = as_needed_comp
    # freq_tasks_dict["daily"] = daily_comp
    # # freq_tasks_dict["weekly"] = weekly_comp
    # # freq_tasks_dict["monthly"] = monthly_comp

    # tasks_data_list = []
    # tasks_data_list.append(freq_tasks_dict)


    # tasks_dict = {}
    # tasks_dict["tasks"] = completed_list
    # tasks_dict["frequency"] = frequency
    # tasks_dict["num_comp"] = num_completed

    merge = [(frequency[i], num_times[i]) for i in range(0, len(frequency))]
    # print('this is merge', merge)

    return merge


if __name__ == '__main__':
    from server import app
    connect_to_db(app)