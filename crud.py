"""Crud operations."""

from model import db, Household, Users, Tasks, connect_to_db
from datetime import datetime, timedelta

# from twilio.rest import Client
# import os



from argon2 import PasswordHasher

# functions start here

def create_household(login, password):
    """Create and return a new household."""

    ph = PasswordHasher()
    hashed = ph.hash(password)

    household = Household(account_login=login, account_password=hashed)

    return household


def get_household_by_login(household_login):
    """Return a household by name"""

    household = Household.query.filter(Household.account_login == household_login).first()
    

    return Household.query.filter(Household.account_login == household_login).first()


def get_household_id_by_name(household_name):
    """Return a household id, given a name"""

    household = Household.query.filter(Household.account_login == household_name).first()
    household_id = household.household_id

    return household_id


def create_user(household_id, user_name, phone_num):
    """Create and return a new user"""

    user = Users(household_id=household_id, user_name=user_name, cellphone = phone_num)

    return user

def delete_user(user_name, household_id):
    """Delete user from household"""

    user = Users.query.filter(Users.user_name == user_name, Users.household_id == household_id).first()

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
def get_house_tasks(household_id):
    """Get dictionary of completed task w/in appropriate timeframe by household id"""

    date1 = datetime.now()
    day24_hr = (date1 - timedelta(hours=24))
    date7 = (date1 - timedelta(days=7))
    date30 = (date1 - timedelta(days=30))

    as_house_completed_tasks = []
    d_house_completed_tasks = []
    w_house_completed_tasks = []
    m_house_completed_tasks = []
    o_house_completed_tasks = []

    # tasks completed in last day
    tasks_24 = Tasks.query.filter(Tasks.household_id == household_id, Tasks.completed == True, Tasks.date_completed >= day24_hr).all()

    
    for task in tasks_24:
        if task.frequency == "as_needed":
            as_house_completed_tasks.append(task.task_name)
        elif task.frequency == "daily":
            d_house_completed_tasks.append(task.task_name)
        elif task.frequency == "other":
            o_house_completed_tasks.append(task.task_name)

    tasks_week = Tasks.query.filter(Tasks.household_id == household_id, Tasks.completed == True, Tasks.date_completed >= date7).all()

    for task in tasks_week:
        if task.frequency == "weekly":
            w_house_completed_tasks.append(task.task_name)

    tasks_month = Tasks.query.filter(Tasks.household_id == household_id, Tasks.completed == True, Tasks.date_completed >= date30).all()

    for task in tasks_month:
        if task.frequency == "monthly":
            m_house_completed_tasks.append(task.task_name)

    house_dict = {}
    house_dict["as needed"] = as_house_completed_tasks
    house_dict["daily"] = d_house_completed_tasks
    house_dict["weekly"] = w_house_completed_tasks
    house_dict["monthly"] = m_house_completed_tasks
    house_dict["other"] = o_house_completed_tasks

    return house_dict

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

    # need to make sure specific user selected, using houseid
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
# user charts removed for better user interface
# def get_count_of_tasks(user_id):
#     """Returns a list of tuples of all tasks completed for chartsjs"""
    
#     tasks = Tasks.query.filter(Tasks.user_id == user_id, Tasks.completed == True).all()

#     frequency = []
#     for task in tasks:
#         frequency.append(task.frequency)

#     as_needed_comp = 0
#     daily_comp = 0
#     weekly_comp = 0
#     monthly_comp = 0
#     other_comp = 0

#     for item in frequency:
#         if item == "as_needed":
#             as_needed_comp += 1
#         elif item == "daily":
#             daily_comp += 1
#         elif item == "weekly":
#             weekly_comp += 1
#         elif item == "monthly":
#             monthly_comp += 1
#         elif item == "other":
#             other_comp += 1

#     freq_tasks_dict = {}
#     freq_tasks_dict["as_needed"] = as_needed_comp
#     freq_tasks_dict["daily"] = daily_comp
#     freq_tasks_dict["weekly"] = weekly_comp
#     freq_tasks_dict["monthly"] = monthly_comp
#     freq_tasks_dict["other"] = other_comp

#     list_for_chart = [(freq, count) for freq, count in freq_tasks_dict.items()]

#     return list_for_chart

# # IN PROGRESS
# def get_range(user_id):
#     """Returns a list of tuples of all tasks completed w/in 30 days for chartsjs"""
    
#     date1 = datetime.today()
#     date2 = (date1 - timedelta(days=30))
#     tasks = Tasks.query.filter(Tasks.user_id == user_id, Tasks.completed == True, Tasks.date_completed <= date1, Tasks.date_completed > date2).all()

#     frequency = []
#     for task in tasks:
#         frequency.append(task.frequency)

#     as_needed_comp = 0
#     daily_comp = 0
#     weekly_comp = 0
#     monthly_comp = 0
#     other_comp = 0

#     for item in frequency:
#         if item == "as_needed":
#             as_needed_comp += 1
#         elif item == "daily":
#             daily_comp += 1
#         elif item == "weekly":
#             weekly_comp += 1
#         elif item == "monthly":
#             monthly_comp += 1
#         elif item == "other":
#             other_comp += 1

#     freq_tasks_dict = {}
#     freq_tasks_dict["as_needed"] = as_needed_comp
#     freq_tasks_dict["daily"] = daily_comp
#     freq_tasks_dict["weekly"] = weekly_comp
#     freq_tasks_dict["monthly"] = monthly_comp
#     freq_tasks_dict["other"] = other_comp

#     list_for_chart = [(freq, count) for freq, count in freq_tasks_dict.items()]

#     return list_for_chart

def chart_all(household_id):
    """Returns a dict of all tasks completed for all users for chartsjs"""
    
    # query all users of given household_id
    all_users = Users.query.filter(Users.household_id == household_id).all()
            
    freq_tasks_dict = {}

    # iterate through user objects to get user_id
    for user in all_users:
        # query all completed tasks for user
        user_tasks = Tasks.query.filter(Tasks.user_id == user.user_id, Tasks.completed == True).all()
        
        as_needed_comp = 0
        daily_comp = 0
        weekly_comp = 0
        monthly_comp = 0
        other_comp = 0

        for task in user_tasks:
            if task.frequency == "as_needed":
                as_needed_comp += 1
            elif task.frequency == "daily":
                daily_comp += 1
            elif task.frequency == "weekly":
                weekly_comp += 1
            elif task.frequency == "monthly":
                monthly_comp += 1
            elif task.frequency == "other":
                other_comp += 1              

        # makes a list of totals per frequency type
        freq_list = [as_needed_comp, daily_comp, weekly_comp, monthly_comp, other_comp]
        # makes a list of frequeny types
        freq_str_list = ["as needed", "daily", "weekly", "monthly", "other"]
        # merge two lists together to make a tuple of each frequency type, total
        tuple_merge = tuple(zip(freq_str_list, freq_list))

        # combine user and user tasks into dictionary w/
        # user_name as keys and tuple of freq type, total as values
        freq_tasks_dict[user.user_name] = tuple_merge

    return freq_tasks_dict


def send_reminder(user_id):
    """Sends text reminder to complete task(s)"""
    from send_sms import message

    # user = Users.query.filter(Users.user_id == user_id).first()

    # user_phone = user.cellphone

    # convert_phone = user_phone.replace("-", "")
    # us_code_phone = "+1" + convert_phone
    
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']

    # client = Client(account_sid, auth_token)

    # # find arguments needed for message function to run
    # message = client.messages.create(
    #     body="Hello from TO-DO...please log-in and complete your task(s)",
    #     from_=os.environ['PHONE_ORIGIN'],
    #     to=us_code_phone
    # )
    # print(message.sid)
    # print(us_code_phone)

    # bc trial account:
    # message


# FORMER CRUD FUNCTIONS NOT IN USE
# def clear_task(task_name):
#     """Clears task from list"""

#     completed_task = Tasks.query.filter(Tasks.task_name == task_name, Tasks.completed == True).first()

#     return completed_task

if __name__ == '__main__':
    from server import app
    connect_to_db(app)