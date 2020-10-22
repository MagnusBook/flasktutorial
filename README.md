# flasktutorial
A flask tutorial for getting started with flask through creating a very simple news web application.

## Installing and running

To install the requirements for this application run:

`pip install -r requirements.txt`

### Set the FLASK_APP environment variable:

*MacOS & Linux:*

`export FLASK_APP=flasktutorial`

*Windows:*

`set FLASK_APP=flasktutorial`

### Initializing the database for the first time
When you first run the app you need to initialize the database. To do this, you can run the `init_db` function in `__init__.py` through the python command, or using a single command:

`python -c "from flasktutorial import init_db; init_db()"`

### Running the application
Run the following command in the root directory of the project:

`flask run`

## Deploying to Heroku
A tutorial for deploying this and other applications to Heroku has been published in the [wiki](https://github.com/MagnusBook/flasktutorial/wiki/Deploying-to-Heroku).
