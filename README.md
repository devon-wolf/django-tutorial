# django-tutorial

## How to Run this Project from Scratch
1) set up (or start up) your virtual environment
    - on my Mac on 2022-02-14, this looks like 
        - `python3 -m venv ~/.venv/django-base`
        - `source ~/.venv/django-base/bin/activate` or `source ~/.venv/django-base/Scripts/activate`
    - if the environment has been set up successfully, you will see the environment's name before your shell prompt
        - for me, after the above commands, it looks like this:
            - `(django-base) username@machine ~ %`
    - **you'll need to do this in any terminal you're using to run commands for the app**; my most common issue is trying to run things in a fresh terminal and forgetting to boot up the environment first
1) install dependences to the virtual environment
    - `cd` into the **project directory** (in my case `~/Code/django-tutorial` - all future steps will assume you are in the project directory unless otherwise specified) and run `pip install -r requirements.txt` to install dependencies
    - to confirm Django has been installed, you can run `python -m django --version`
        - if this doesn't output the version number (in my case here it's `4.0.2`), you'll need to troubleshoot your setup; confirm you've activated your virtual environment and are running the command from the project directory
1) run the server
    - run `python manage.py runserver`
    - that should do it! if you're seeing something like this at the end of the output you're all set to get started.
        ```
        Django version 4.0.2, using settings 'tutorialproject.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.
        ```
1) set up the database and create an admin user
    - migrations and the database are gitignored; you'll need to set up your local database
        1) run `python manage.py migrate` to run the default Django migrations
        1) run `python manage.py makemigrations polls` to generate migrations for the models in the `polls` app
        1) run `python manage.py migrate` again to run the polls migrations; I'm guessing you can probably skip the first run of this (above) and just run it all now, but I tend to like to do things in smaller bits
    - after running the polls migrations, you should be able to visit `http://localhost:8000/polls/` and see the view (which should simply say 'No polls available' until you've added some)
    - you can visit `http://localhost:8000/admin`, but you won't be able to login until you create an admin user
        1) run `python manage.py createsuperuser` and follow the prompts; you can then use the credentials you create to login to the admin site

1) run tests with `python manage.py test` and confirm everything is working as intended

- Everything should work now! If not, consult the following resources for troubleshooting:
    - [Django Installation Docs](https://docs.djangoproject.com/en/4.0/intro/install/)
    - [venv Docs](https://docs.python.org/3/tutorial/venv.html)
    - [Django Polls App Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)

## Integrating Remote Changes
After pulling down from remote:
1) activate your virtual environment `source ~/.venv/django-base/bin/activate` or `source ~/.venv/django-base/Scripts/activate`
1) install dependencies `pip install -r requirements.txt`; only necessary if dependencies have changed, but doesn't hurt to run it to check
1) check for migration changes with `python manage.py makemigrations` or `python manage.py makemigrations polls` - this will generate migrations if there are any to apply
    - if needed, run migrations with `python manage.py migrate`
1) run tests to confirm all is well `python manage.py test`
1) run server `python manage.py runserver`
And you should be set!