# Django
Django is a Python-based web framework that will allow us to write Python code that dynamically generates HTML and CSS. The advantage to using a framework like Django is that a lot of code is already written for us that we can take advantage of.

To get started, we’ll have to install Django, which means you’ll also have to install pip if you haven’t already done so.
Once you have Pip installed, you can run
    ```bash
    pip3 install Django 


After installing Django, we can go through the steps of creating a new Django project:

Run django-admin startproject PROJECT_NAME to create a number of starter files for our project.
Run 
    ```bash
    cd PROJECT_NAME
 
Open the directory in your text editor of choice. You’ll notice that some files have been created for you. We won’t need to look at most of these for now, but there are three that will be very important from the start:
- manage.py is what we use to execute commands on our terminal. We won’t have to edit it, but we’ll use it often.
- settings.py contains some important configuration settings for our new project. There are some default settings, but we may wish to change some of them from time to time.
- urls.py contains directions for where users should be routed after navigating to a certain URL.

Start the project by running 

    ```bash
    python manage.py 
    ```
runserver. This will open a development server, which you can access by visiting the URL provided. This development server is being run locally on your machine, meaning other people cannot access your website. This should bring you to a default landing page: