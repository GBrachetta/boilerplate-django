
# Django Boilerplate

This app is a boilerplate with ready-to-go settings for a new Django app.

## Steps to get started

1. Create a folder to host the app.

2. Create a virtual environment in that folder.

3. Install the requirements from `Pipfile` with

    `pipenv install` and `pipenv install --dev`

4. Change the name of the app by running

    `python manage.py rename your-app-name`

5. Delete the app `main` used to rename the boilerplate, and remove it from the installed apps.

6. Create the relevant environment variables in the `.env` file provided.

7. Run eventually `python manage.py collectstatic`.

8. Settings are divided in the module `settings/environments`. Edit these for the different environments or `settings/components/base.py` for settings common to both development and production.

9. The `.env` file provided should include your environment variables. Change `DJANGO_ENV` to either `development` or `production` for the settings to load.

That's all. Start coding!

## **Note**

If you're using VSCode's debug functionality *and* Pipenv, be aware that there's currently an issue and the request for the creation of the shell and the command to start the debugger are timed badly.

To avoid issues, install all dependencies from the Pipfile as:

`pipenv install`

`pipenv install --dev`

and once the environment has all dependencies installed, momentarily rename your Pipfile (for example adding a dash before the name) so pipenv won't attempt to create a new shell while the debugger is invoked.

Make sure to rename back Pipfile for a correct deployment.
