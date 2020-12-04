
# Django Boilerplate

This app is a boilerplate with ready-to-go settings for a new Django app.

It assumes using AWS to store static files, and the production variables have been added accordingly (but they only load in case there's a `USE_AWS=True` variable in the environment).

It also assumes deploying in Heroku to make use of their database, but that can be easily changed to any other database set of variables in `your-app-name/settings/production.py`.

## How to get started

1. Download this repository to your computer and open it with your editor.

   The app contains a Pipfile, so a virtual shell will be automatically started if you have [pipenv](https://pipenv.pypa.io/en/latest/) installed, otherwise create your virtual environment with the manager of your preference.

2. Install the requirements with `$ pipenv install` and `$ pipenv install --dev` if using Pipenv, otherwise with `$ pip install -r requirements.txt`.

3. You can change the name of the project to one of your liking by running

    `$ python manage.py rename <current-project-name> <new-project-name>`

4. Apply migrations with `$ python manage.py migrate` to initialize the database with the proprietary Django models.

That's all. Happy coding!

## Notes

- The `.gitignore` file provided is ready to ignore all the commonly ignored files so if you create a local repository (`$ git init`) it will take care of ignoring sensitive information.

- The `.env` file provided (`your-app-name/settings/.env`) is the place to include your environment variables. Change `DJANGO_ENV` to either `development` or `production` for the corresponding settings to load (default is 'development').

- New settings go in the following files:

    1. `your-app-name/settings/common.py` for settings common to both development and production
    2. `your-app-name/settings/development.py` for settings used during development.
    3. `your-app-name/settings/production.py` for settings used for production.

- The app includes a handy django toolbar (only available in the development environment) that facilitates debugging.

- The app also includes my favorite settings to develop a Django app on VS Code, and a `launch.json` file to run the server in debugging mode using the integrated debugger in VS Code. Feel free to delete these and the parent `.vscode` folder if you use some other editor.

- An additional command has been added, `$ python manage.py makesuper` that creates a superuser in one line:

    1. Username: admin
    2. Password: admin
    3. Email: admin@domain.com

- If you're using VSCode's debug functionality *and* Pipenv, be aware that there's currently an issue and the request for the creation of the shell and the command to start the debugger are timed badly.

  To avoid issues, install all dependencies from the Pipfile as described in point 3 and once the environment has all dependencies installed, momentarily rename your Pipfile (for example adding a dash before the name) so pipenv won't attempt to create a new shell while the debugger is invoked.

    > Make sure to rename back Pipfile before installing new dependencies for a correct deployment.
