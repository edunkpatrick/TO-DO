"""Models for task tracking app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# classes start here

class Household(db.Model):
    """Household"""

    __tablename__ = "household"

    household_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # revisit length of log in and password requirements
    account_login = db.Column(db.String(20), nullable=False, unique=True)
    account_password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        """Show info about household"""
        return f"<Household id={self.household_id} account_login={self.account_login}>"

    users = db.relationship("Users", back_populates="household")
    tasks = db.relationship("Tasks", back_populates="household")


class Users(db.Model):
    """Users"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    household_id = db.Column(db.Integer, db.ForeignKey('household.household_id'))
    user_name = db.Column(db.String(20), nullable=False)
    cellphone = db.Column(db.String(12), nullable=True)

    def __repr__(self):
        """Show info about user"""
        return f"<Users user_id={self.user_id} name={self.user_name} household_id={self.household_id}>"

    household = db.relationship("Household", back_populates="users")
    tasks = db.relationship("Tasks", back_populates="users")

class Tasks(db.Model):
    """Tasks"""

    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    household_id = db.Column(db.Integer, db.ForeignKey('household.household_id'))
    # task_description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean)
    date_completed = db.Column(db.Date)
    frequency = db.Column(db.String(20))

    def __repr__(self):
        """Show info about task"""
        return f"<Tasks task_id={self.task_id} task_name={self.task_name}>"

    users = db.relationship("Users", back_populates="tasks")
    household = db.relationship("Household", back_populates="tasks")

# CODE REVIEW 1/25/23 COMPLETED #

def connect_to_db(flask_app, db_uri="postgresql:///tasks_db", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)