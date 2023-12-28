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
    python manage.py runserver

This will open a development server, which you can access by visiting the URL provided. This development server is being run locally on your machine, meaning other people cannot access your website.


Next, we’ll have to create an application. Django projects are split into one or more applications. Most of our projects will only require one application, but larger sites can make use of this ability to split a site into multiple apps. To create an application, we run 

    ```bash
    python manage.py startapp APP_NAME 

    ```
This will create some additional directories and files that will be useful shortly, including views.py.
Now, we have to install our new app. To do this, we go to settings.py, scroll down to the list of INSTALLED_APPS, and add the name of our new application to this list.

### Routes

we’ll navigate to views.py. This file will contain a number of different views, and we can think of a view for now as one page the user might like to see. To create our first view, we’ll write a function that takes in a request. For now, we’ll simply return an HttpResponse (A very simple response that includes a response code of 200 and a string of text that can be displayed in a web browser) of “Hello, World”. In order to do this, we have include from django.http import HttpResponse

we need to somehow associate this view we have just created with a specific URL. To do this, we’ll create another file called urls.py in the same directory as views.py. We already have a urls.py file for the whole project, but it is best to have a separate one for each individual app.
Inside our new urls.py, we’ll create a list of url patterns that a user might visit while using our website. In order to do this:
We have to make some imports: from django.urls import path will give us the ability to reroute URLSs, and from . import views will import any functions we’ve created in views.py.
Create a list called urlpatterns
For each desired URL, add an item to the urlpatterns list that contains a call to the path function with two or three arguments: A string representing the URL path, a function from views.py that we wish to call when that URL is visited, and (optionally) a name for that path, in the format name="something".
