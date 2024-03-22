# HigherUp
## Git Setup
Clone the repository by running
```git clone https://github.com/AustinfHunter/higherup```

Then navigate to the project folder with ```cd higherup```

Set your remote by running ```git remote add origin https://github.com/AustinfHunter/higherup.git```

Create a new development branch to work in by running ```git branch <author-last-name>-<branch-name>```

Note: It's helpful if ```<branch-name>``` is meaningful, for example, if I were working on authentication, I'd create the branch with the command ```git branch hunter-authentication```

Now you're ready to start setting up your development environment!

## Environment Setup
This is designed to be a big project (in the long run) so there are few dependencies that will need to be installed to get things up and running. You should use a virtual environment to manage these dependencies.

### Create a virtual environment
To create your virtual environment, run ```python -m venv /path-to-virtual-environment``` in your project folder.

### Activate the virtual enviroment
To active your virtual environment, run ```source /path-to-virtual-environment/bin/activate```

### Install Dependencies
The following dependencies are required:
- [Flask](https://flask.palletsprojects.com/en/3.0.x/): ```pip install Flask```
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/): ```pip install flask-login```
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/): ```pip install Flask-SQLAlchemy```
- [Dotenv](https://pypi.org/project/python-dotenv/): ```pip install python-dotenv```

### Setup Environment Variables
A .env file is the simplest way to manage environment variables. 

Create a .env file in the root directory of the project and add at least all required variables from the following:
| Environment Variable | Required Value | Required |
| -------------------- | -------------- | -------- |
| FLASK_APP            | Path to app folder | Yes |
| FLASK_ENV            | Can be set to development or production | Yes |
| SECRET_KEY           | A random secret key | Yes |
| DATABASE_URI         | The URI for the database | No, defualts to local sqlite database |
| SQLALCHEMY_TRACK_MODIFICATIONS | True or False | No, defaults to false |

Note: If you don't set the DATABASE_URI variable, a sqlite database called app.db can be created instead, which is fine for development.

## Database Management
### Setup and initialization
To initialize your local Sqlite database and make it available for your app, navigate to the root directory of the project, activate your virtual environment, and run ```flask shell```

Once you are in the shell run the following commands:
1. ```from app import db, models```
2. ```db.create_all()```

This should run without any output, unless there are errors. Run the ```quit()``` to exit the flask shell.

You should see a new file in the root directory called app.db

To test that everything worked correctly, run the following commands:
1. ```sqlite3 app.db```
2. ```.tables``` (should show all tables in the database)
3. ```.schema <table-name>``` (should show the SQL schema for the given table)

### Updating the Database
If there are major changes to the models during development, it is best to drop the tables and create fresh versions. This can be achieved by running the following commands:
1. ```flask shell```
2. ```from app import db, models``` 
3. ```db.drop_all()``` (Drops all tables)
4. ```db.create_all()``` (Creates all tables using up-to-date models)

## Project Structure
Your project structure should look like this by the time you're done with all of the above.
```
.
├── app
│   ├── auth
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models
│   │   ├── company.py
│   │   ├── post.py
│   │   └── user.py
│   ├── posts
│   │   └── __init__.py
│   ├── static
│   │   ├── css
│   │   │   └── bootstrap.min.css
│   │   └── js
│   │       └── bootstrap.bundle.min.js
│   ├── templates
│   │   ├── base.html
│   │   └── index.html
│   └── users
│       └── __init__.py
├── app.db
├── config.py
├── __pycache__
│   └── config.cpython-310.pyc
└── README.md
```
Note: Hidden files, such as .env, .venv, and .gitignore are not shown in the project structure but the should exist in your project.

---

That's it! You're ready to start working on HigherUp!
