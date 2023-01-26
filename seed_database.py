"""Script to seed tasks database"""

import os
import json
from random import choice, randint
# see which date needed below:
from datetime import datetime
from datetime import date   

import crud
import model
import server

# create fake json data prior to continuing with below:

os.system("dropdb tasks_db")
os.system('createdb tasks_db')

model.connect_to_db(server.app)
model.db.create_all()

# # look into google task api for below:
# with open('data/tasks.json') as f:
#     task_data = json.loads(f.read())
# # create tasks and store in a list to assign to users
# tasks_in_db = []
# for task in task_data:

#     # look up what is needed for google task api

#     db_task = crud.create_task(task_name, user_id, frequency)
#     tasks_in_db.append(db_task)
# model.db.session.add_all(tasks_in_db)
# model.db.session.commit()

households_in_db = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tasks_in_db = ["clean kitchen", "feed dog", "laundry", "bills", "prep dinner", "grocery shopping",
    "prep kids lunches", "water plants", "clean bathroom", "help with homework"]

frequency_in_db = ["as needed", "daily", "weekly", "monthly"]

# creating 10 fake households with fake users
for n in range(1, 11):
    login = f"house{n}"
    password = f"test{n}"

    household = crud.create_household(login, password)
    model.db.session.add(household)

for n in range(1, 21):
    household_id = randint(1, 10)
    user_name = f"user{n}"

    user = crud.create_user(household_id, user_name)
    model.db.session.add(user)

    # assigning random tasks to user from list
    random_user = randint(1, 20)
    random_task = choice(tasks_in_db)
    random_frequency = choice(frequency_in_db)

    task = crud.create_task(random_task, random_user, random_frequency)
    model.db.session.add(task)

model.db.session.commit()
