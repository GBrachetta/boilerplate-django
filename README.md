
# Django Boilerplate

![image](https://res.cloudinary.com/gbrachetta/image/upload/v1607301400/oob_bfglzw.jpg)

This app is a boilerplate with ready-to-go settings for a new Django app.

It assumes using AWS to store static files, and the production variables have been added accordingly (but they only load in case there's a `USE_AWS=True` variable in the environment).

It also assumes deploying in Heroku to make use of their database, but that can be easily changed to any other database set of variables in `your-app-name/settings/production.py`.

## How to get started

1. Download this repository to your computer and open it with your editor.

   The app contains a Pipfile, so a virtual shell will be automatically started if you have [pipenv](https://pipenv.pypa.io/en/latest/) installed, otherwise create your virtual environment with the manager of your preference.

2. Install the requirements with `$ pipenv install` and `$ pipenv install --dev` if using Pipenv, otherwise with `$ pip install -r requirements.txt`.

3. You can change the name of the project to one of your liking by running

    `$ python manage.py rename <current-project-name> <new-project-name>`

    > **Don't rename your project once you've started adding apps. The rename script looks for boilerplate files only in order to rename them. Once you renamed your project and started developing, stick to that name!**

4. Apply migrations with `$ python manage.py migrate` to initialize the database with the proprietary Django models.

5. Run the server with `$ python manage.py runserver`.

That's all. Happy coding!

## Notes

- The `.gitignore` file provided is ready to ignore all the commonly ignored files so if you create a local repository (`$ git init`) it will take care of ignoring sensitive information.

- The `.env` file provided (`your-app-name/settings/.env`) is the place to include your environment variables. Change `DJANGO_ENV` to either `development` or `production` for the corresponding settings to load (default is 'development').

- New settings go in the following files:

  - `your-app-name/settings/common.py` for settings common to both development and production
  - `your-app-name/settings/development.py` for settings used during development.
  - `your-app-name/settings/production.py` for settings used for production.

- **Read the comments in `<your_project>/settings/production.py` for the env variables to add to your production server!**

- The app includes a handy django toolbar (only available in the development environment) that facilitates debugging.

- The app also includes my favorite settings to develop a Django app on VS Code, and a `launch.json` file to run the server in debugging mode using the integrated debugger in VS Code. Feel free to delete these and the parent `.vscode` folder if you use some other editor.

- An additional command has been added, `$ python manage.py makesuper` that creates a superuser in one line:

  - Username: admin
  - Password: admin
  - Email: admin@domain.com
