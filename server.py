"""Server for task tracking app."""

from flask import (Flask, render_template, request, flash, session, redirect)

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
    else:
        session["account_name"] = household.account_login
        flash(f"Welcome back, {household_name}!")

    return render_template('household.html')

# @app.route('/landing')
# app route for picking household user
@app.route('/add_user', methods=["POST"])
def create_user():
    """Creates a new user for household"""

    user_name = request.form.get("user_name")

    user = crud.get_user_by_name(user_name)

    if user:
        flash("That user profile already exists, please select user from dropdown")
    else:
        # need to add return household_id to login for crud function
        user = crud.create_user(household_id, user_name)
        db.session.add(user)
        db.session.commit()
        flash("User created succesfully, please select from dropdown")

if __name__ == "__main__":
    connect_to_db(app)
    # look up in notes how to store secret key in .gitignore
    app.secret_key = "supersecret"
    app.run(host="0.0.0.0", debug=True)