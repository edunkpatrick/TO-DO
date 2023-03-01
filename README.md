# TO-DO Task Organization for Dwelling Optimization

TO-DO is a task-tracking Flask app for communicating status of shared tasks within a household. Members of a household can assign themselves or other housemates a task, track completion of tasks, visualize each member's contributions utilizing Chart JS, and send text reminders with Twilio SMS.

TO-DO is a web app created by Erin Dunkley. As a full-time working mom, Erin wanted to create a convenient tool for checking the status of commonly shared household tasks and communicating status between household members.

![Alt text](/static/images/homepage.png "Homepage")

# Table of Contents

    :star: [Technologies Used](#technologiesused)
    :star: [Features](#features)
    :star: [How to locally run TO-DO](#run)
    :star: [How to use TO-DO](#use)
    :star: [Author](#author)

<a name="technologiesused"></a>
## Technologies Used

    * Python
    * Flask
    * PostgresSQL
    * SQLAlchemy
    * Javascript
    * AJAX/JSON
    * Jinja
    * Bootstrap
    * Chart.js
    * Twilio API

(dependencies are listed in requirements.txt)

![Alt text](/static/images/remindertext.png "Reminder Text")

<a name="run"></a>
## How to locally run TO-DO

TO-DO has not been deployed yet, so follow the instructions below to run the app locally.

### Run the TO-DO Flask App

    * Set up and activate your python virtualenv
    * Install all dependencies with pip3 install -r requirements.txt
    * Set up your secret key in secrets.sh
    * Run python3 server.py
    * Go to localhost:5000 to see the webapp

<a name="use"></a>
## How to use TO-DO

### Create an account. Once logged in, add your household users and assign tasks to users

<a name="author"></a>
## Author
Erin Dunkley is a Criminalist and Software Engineer in the East Bay Area, CA