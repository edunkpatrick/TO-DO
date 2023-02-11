"""Server for task tracking app."""
import os

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)

from model import connect_to_db, db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined

app = Flask(__name__)


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/household', methods=["POST"])
def register_household():
    """Create a new household"""

    household_name = request.form.get("account_name")
    password = request.form.get("password")

    household = crud.get_household_by_login(household_name)
    if household:
        flash("Account with that name already exists, please select a unique name")
    
    else:
        household = crud.create_household(household_name, password)
        db.session.add(household)
        db.session.commit()
        flash("Account created succesfully, please log in")

    return redirect('/')


@app.route('/household_home', methods=["POST"])
def login_household():
    """Login household"""

    household_name = request.form.get("account_name")
    password = request.form.get("password")

    household = crud.get_household_by_login(household_name)
    
    if not household or household.account_password != password:
        flash("The household name or password was incorrect, please try again.")
        return redirect('/')
    else:
        user_list = crud.get_users_by_household(household_name)
        session["account_name"] = household.account_login
        flash(f"Welcome back, {household_name}!")
        household_id = crud.get_household_id_by_name(household_name)
        # house_completed_tasks is a dict w/ freq as keys, tasks as values list
        house_completed_tasks = crud.get_house_tasks(household_id)
        as_needed_list = []
        daily_list = []
        weekly_list = []
        monthly_list = []
        other_list = []

        for key, value in house_completed_tasks.items():
            if key == "as_needed":
                as_needed_list = value
            elif key == "daily":
                daily_list = value
            elif key == "weekly":
                weekly_list = value
            elif key == "monthly":
                monthly_list = value
            elif key == "other":
                other_list = value


        return render_template('household.html', household_name=household_name, 
        user_list=user_list, as_needed_list=as_needed_list, daily_list=daily_list,
        weekly_list=weekly_list, monthly_list=monthly_list, other_list=other_list)


@app.route('/add_user')
def create_user():
    """Creates a new user for household"""

    user_name = request.args.get("user_name")
    household_name = session["account_name"]
    user = crud.get_user_by_name(user_name, household_name)

    if user:
        flash("That user profile already exists, please select user from dropdown")
    else:
        household_id = crud.get_household_id_by_name(household_name)
        user = crud.create_user(household_id, user_name)
        db.session.add(user)
        db.session.commit()
        flash("User created succesfully, please select from dropdown")

    user_list = crud.get_users_by_household(household_name)

    return render_template('household.html', household_name=household_name, user_name=user_name, user_list=user_list)

# FIRST CODE REVIEW 1/25/23 FINISHED HERE #

@app.route('/user_profile')
def show_user_landing():
    """Shows tasks for user profile selected"""

    household_name = session["account_name"]
    user_list = crud.get_users_by_household(household_name)

    user_profile_selected = request.args.get("available_users")
    user = crud.get_user_by_name(user_profile_selected, household_name)
    session["user_name"] = user.user_name

    get_tasks = crud.get_tasks(user_profile_selected, household_name)

    household_id = crud.get_household_id_by_name(household_name)
    house_completed_tasks = crud.get_house_tasks(household_id)

    house_completed_tasks = crud.get_house_tasks(household_id)
    as_needed_list = []
    daily_list = []
    weekly_list = []
    monthly_list = []
    other_list = []

    for key, value in house_completed_tasks.items():
        if key == "as_needed":
            as_needed_list = value
        elif key == "daily":
            daily_list = value
        elif key == "weekly":
            weekly_list = value
        elif key == "monthly":
            monthly_list = value
        elif key == "other":
            other_list = value

    return render_template('household.html', get_tasks=get_tasks, 
    user_profile_selected=user_profile_selected, 
    household_name=household_name, user_list=user_list, 
    house_completed_tasks=house_completed_tasks, as_needed_list=as_needed_list,
    daily_list=daily_list, weekly_list=weekly_list, monthly_list=monthly_list,
    other_list=other_list)

@app.route('/delete_user')
def delete_user():
    """Deletes user from household"""

    user = session["user_name"]
    household_name = session["account_name"]
    
    household_id = crud.get_household_id_by_name(household_name)

    deleted_user = crud.delete_user(user, household_id)
    flash(f"{deleted_user.user_name}, deleted")
    db.session.delete(deleted_user)
    db.session.commit()


    return


@app.route('/add_task')
def add_task():
    """Adds task to user profile"""

    household_name = session["account_name"]
    user_list = crud.get_users_by_household(household_name)
    household_id = crud.get_household_id_by_name(household_name)
   
    add_task = request.args.get("add_task")
    frequency_task = request.args.get("frequency")
    user_assigned = session["user_name"]

    if add_task:
        user_id = crud.get_user_id(user_assigned, household_id)
        task = crud.create_task(task_name=add_task, user_id=user_id, household_id=household_id, completed=False, frequency=frequency_task)
        db.session.add(task)
        db.session.commit()
    
    get_tasks = crud.get_tasks(user_assigned, household_name)

    return render_template('household.html', user_profile_selected=user_assigned, get_tasks=get_tasks, household_name=household_name, user_list=user_list)


@app.route('/delete_task')
def delete_selected_task():
    """Deletes task from list"""

    user_assigned = session["user_name"]
    
    selected_task = request.args.get("task")

    if selected_task:
        delete = crud.delete_task(user_assigned, selected_task)
        db.session.delete(delete)
        db.session.commit()
        return selected_task
    else:
        return "task not deleted"


@app.route('/complete_task')
def complete_selected_task():
    """Marks selected task complete"""

    user_assigned = session["user_name"]
    
    selected_task = request.args.get("task")

    if selected_task:
        complete = crud.complete_task(user_assigned, selected_task)
        db.session.commit()
        completed_task = complete.task_name
        return completed_task
    else:
        return "task not completed"


@app.route('/tasks_complete.json')
def get_all_tasks_complete():
    """Returns object of all tasks completed for chartjs"""

    household_name = session["account_name"]
    household_id = crud.get_household_id_by_name(household_name)
    user_name = session["user_name"]
    user_id = crud.get_user_id(user_name, household_id)
    # tasks_complete is a list of tuples
    tasks_complete = crud.get_count_of_tasks(user_id)

    tasks_complete_list = []
    # for tuple pair, packing into list of dicts
    for frequency, total in tasks_complete:
        tasks_complete_list.append({'freq': frequency, 'num': total})
    
    return jsonify({'data': tasks_complete_list})
    
# CODE REVIEW 2 COMPLETED 2/3/23

# IN PROGRESS
@app.route('/get_date_range.json')
def get_range():
    """Gets data for chartjs w/in specified date range"""

    household_name = session["account_name"]
    household_id = crud.get_household_id_by_name(household_name)
    user_name = session["user_name"]
    user_id = crud.get_user_id(user_name, household_id)
    # tasks_complete is a list of tuples
    # date1 = request.args.get("first_date")
    # date2 = request.args.get("second_date")
    tasks_complete = crud.get_range(user_id)

    tasks_complete_list = []
    # for tuple pair, packing into list of dicts
    for frequency, total in tasks_complete:
        tasks_complete_list.append({'freq': frequency, 'num': total})
    
    return jsonify({'data': tasks_complete_list})

@app.route('/house_tasks_complete.json')
def get_all_house_complete():
    """Returns object of all house tasks completed for chartjs"""

    household_name = session["account_name"]
    household_id = crud.get_household_id_by_name(household_name)
    
    background_dict = {}
    bar_colors = ['#bf3fbf', '#c09af8', '#9af8f3', '#adf89a', '#f8f79a']
    background_dict['colors'] = bar_colors
    # tasks_complete is a dict w/user_name as keys and
    # tuple of freq type, total as values
    tasks_complete = crud.chart_all(household_id)
    
    return jsonify({'house': tasks_complete, 'bar_colors': background_dict})

@app.route('/sign_out')
def sign_out():
    """Logs out househould and user"""
    
    del session["account_name"]
    # if session["user_name"]:
    #     session.pop("user_name")

    return redirect('/')


# FORMER HTML ROUTES/FUNCTIONS, REMOVE WHEN MVP COMPLETE
# @app.route('/user_profile', methods=["POST"])
# def show_user_landing():
#     """Shows tasks for user profile activated"""
#     # gets user selected 
#     user_profile_selected = request.form.get("available_users")
#     user = crud.get_user_by_name(user_profile_selected)
#     session["user_name"] = user.user_name
#     # get_tasks returns a list of assigned tasks, will unpack 
#     # list in jinja loop on assigned_tasks.html
#     get_tasks = crud.get_tasks(user_profile_selected)

#     return render_template('assigned_tasks.html', get_tasks=get_tasks, user_profile_selected=user_profile_selected)

# @app.route('/add_task')
# def add_task():
#     """Adds task to user profile"""

#     add_task = request.args.get("add_task")
#     frequency_task = request.args.get("frequency")
#     user_assigned = session["user_name"]
#     user_profile_selected = user_assigned

#     if add_task:
#         user_selected = crud.get_user_id(user_profile_selected)
#         task = crud.create_task(task_name=add_task, user_assigned=user_selected, frequency=frequency_task)
#         db.session.add(task)
#         db.session.commit()
    
#     get_tasks = crud.get_tasks(user_profile_selected)

#     return render_template('assigned_tasks.html', user_profile_selected=user_profile_selected, get_tasks=get_tasks)

# @app.route('/clear_task')
# def clear_selected_task():
#     """Clears task from list"""

#     selected_task = request.args.get("task")

#     if selected_task:
#         clear = crud.clear_task(selected_task)
#         cleared_task = clear.task_name
#         return cleared_task
#     else:
#         return

if __name__ == "__main__":
    connect_to_db(app)
    # look up in notes how to store secret key in .gitignor/secrets.sh
    app.secret_key = 'supersecret'
    app.run(host="0.0.0.0", debug=True)