"""Server for task tracking app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)

from model import connect_to_db, db

import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
# app.secret_key = "supersecret"
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
        return render_template('household.html', household_name=household_name, user_list=user_list)


@app.route('/add_user', methods=["POST"])
def create_user():
    """Creates a new user for household"""

    user_name = request.form.get("user_name")
    user = crud.get_user_by_name(user_name)
    household_name = session["account_name"]

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

@app.route('/user_profile', methods=["POST"])
def show_user_landing():
    """Shows tasks for user profile activated"""
    household_name = session["account_name"]
    user_list = crud.get_users_by_household(household_name)
    # gets user selected 
    user_profile_selected = request.form.get("available_users")
    user = crud.get_user_by_name(user_profile_selected)
    session["user_name"] = user.user_name
    # get_tasks returns a list of assigned tasks, will unpack 
    # list in jinja loop on assigned_tasks.html
    get_tasks = crud.get_tasks(user_profile_selected)

    return render_template('household.html', get_tasks=get_tasks, user_profile_selected=user_profile_selected, household_name=household_name, user_list=user_list)

@app.route('/add_task')
def add_task():
    """Adds task to user profile"""

    household_name = session["account_name"]
    user_list = crud.get_users_by_household(household_name)

    add_task = request.args.get("add_task")
    frequency_task = request.args.get("frequency")
    user_assigned = session["user_name"]
    user_profile_selected = user_assigned

    if add_task:
        user_selected = crud.get_user_id(user_profile_selected)
        task = crud.create_task(task_name=add_task, user_assigned=user_selected, frequency=frequency_task)
        db.session.add(task)
        db.session.commit()
    
    get_tasks = crud.get_tasks(user_profile_selected)

    return render_template('household.html', user_profile_selected=user_profile_selected, get_tasks=get_tasks, household_name=household_name, user_list=user_list)

@app.route('/delete_task')
def delete_selected_task():
    """Deletes task from list"""
    household_name = session["account_name"]
    user_list = crud.get_users_by_household(household_name)
    user_assigned = session["user_name"]

    # need to query for task_id to make sure exact row is deleted
    selected_task = request.args.get('delete_task')

    delete = crud.delete_task(selected_task)

    return render_template('household.html', household_name=household_name, user_assigned=user_assigned, user_list=user_list)


# TO DO:
# add functions to remove/edit tasks and to mark complete
# add DOM manipulation to change tasks
# add chart that shows task contributions per user of household

if __name__ == "__main__":
    connect_to_db(app)
    # look up in notes how to store secret key in .gitignor/secrets.sh
    app.secret_key = "supersecret"
    app.run(host="0.0.0.0", debug=True)