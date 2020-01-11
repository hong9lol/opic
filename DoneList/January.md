# January

### Fri 10th

    1. Watching Djaong guide for begginers on Youtube (about 20 mintues)

#### Note

Lecture video: <https://www.youtube.com/watch?v=LYmZB5IIwAI>

### Sat 11th

1. Eng Django lecture on youtube (4:18:00)
2. Make basic environment of Django on my Desktop
   - Install python3 and pip3 with apt
   - Install pipenv with pip3 => pip3 install pipenv
   - How to use pipenv
     1. Move to directory what you want to make a project
     2. \$ pipenv shell
     3. Now, you can develop a python project in a vitual Env
     4. You can also use python and pip instead of python3 or pip3
3. Do a tutorial
   - How to make a project of Django and run
     1. make project
     ```
     $ django-admin startproject <project-name>
     ```
     2. Change timze zone from "UTC" to "Asia/Seoul"
     3. python manage.py migrate -> i don't know why i have to do this, it's related with DB though
     4. python manage.py runserver
   - About Django amdin
     1. Interface to access to DB
     2. Using Django admin you can do DB operation easily
     3. you can make an admin account with below command
     ```
     $ python manage.py createsuperuser
     ```
   - What is "app" in django and how to make
     1. Small peice of web application
     2. Project is for an environment and have a bunch of apps
     3. How to make
     ```
     $ python manage.py startapp <app-name>
     ```
     4. Add your app name in INSTALLED_APPS of setting.py - <b><span style="color:red">need to find out why</b>
   - URL Configuration in Django
     1. To manage urls make urls.py in your each app
     2. Move to urls.py of project add import "include'
     3. Add path and link it your app urls.py like this
     ```
     path('sample/', include('sampleapp.urls')),
     ```
     4. Copy urls code from urls.py of project and paste it to urls.py of an app
     5. Make response in views.py and link it to path in urls.py of the app

#### Note

Lecture Video: <https://www.youtube.com/watch?v=6ManltU_8iU>
