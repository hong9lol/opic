# Tutorial

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

- Use MySQL as a database

  1. Install mysql
  2. Create user for django

  ```
  create user 'django'@'localhost' identified by '1111';
  grant usage on *.* to 'django'@'localhost';
  grant all privileges on <DB NAME> to 'django'@'localhost';
  ```

  3. Set below text in setting.py

  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydjango',
        'USER': 'django',
        'PASSWORD': '1111',
        'HOST': 'localhost',
        'PORT': '3306',
    }
  }
  ```

  4. Migrate databse

  ```
  python manage.py migrate
  ```

  5. Make super user for new DB

- What are the Django models

  1.  With models you can make Tables
  2.  First make Model class and makemigrations and migrata

- How to register Models to Django admin panel

  1. Import the Model in admin.py
  2. Register models

  ```
  admin.site.register(Question)
  ```

  3. You can add DB object in you admin page
  4. The function "**str**" make return value as the tile of the object

- Working with Django shell

  1. you can manage DB with Django shell (python manage.py shell)

- Working with template in Django

  1. Make a templates folder in project folder
  2. Make a html file and fill out the form
  3. return the html from view.py in your app

  ```
  return render(request, 'home.html')
  ```
