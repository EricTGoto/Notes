<h2>Terminology</h2>

**View:**: python function that takes a web request and returns a web response

**URLConf**: mapping between URL path expressions to python functions

**Models (database)**: datababase layout, with additional metadata

<h2>General</h2>

To include an app in a project, add a reference to its configuration class in the installed_apps setting.

Default apps require the use of at least one database table so run python manage.py migrate before using them.

Don't put python code within the web server's document root, because it may be possible.

Project vs Apps: app is a web application that does something, e.g. polling app, project is a collection of configuration and apps for a particular website

To call a view, we need to map it to a URL.

URL dispatcher: https://docs.djangoproject.com/en/4.0/topics/http/urls/
How Django processes a request:
    1. Django determines the root URLconf module to use. Normally, this is the value of the root_urlconf setting, but if the incoming HttpRequest object has a urlconf
        attribute, its value will be used instead
    2. Django loads that python module and looks for the variable urlpatterns
    3. Django runs through each URL pattern, in order, and stops at the first one that matches the requested URl, matching against path_info
    4. Once the URL pattern matches, django imports and calls the given view, which is a python function. View gets passed the following arguments:
        * instance of HttpRequest
        * if the matched URl pattern contained no named groups, then the matches from the regex are provided as positional arguments
        * the keyword arguments are made up of any named parts matched by the path expression that are provided, overridden by any arguments specified in the optional kwargs argument to django.urls.path() or django.urls.re_path()
    5. If no url pattern matches, or exception raised, Django invoked an error handling view

path() function is passed 4 arguments: 2 required: route and view, two optional: kwargs and name
    route: string that contains a URL pattern
    view: when django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first arg and any "captured" values from the route as keyword elements
    kwargs: arguments
    name: can name your url to refer to it unambiguously from elsewhere in Django. lets you make global changes to the URL patterns of the project while only touching a single file

Simple three step guide to making model changes:
    1. change models in models.py
    2. run python manage.py makemigrations to create migrations for those changes (it's like staging changes like git add)
    3. run python manage.py migrate to apply those changes to the database (like running git commit)

<h2>Commands:</h2>

**startproject xxxxx**

The command startproject xxxxx will create a folder directory like so:

xxxxx/
    manage.py
    xxxxx/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

The outer xxxxx/ is the root directory. Can be renamed
manage.py: command-line utility that lets you interact with the django project
inner xxxxx/ is the actual python package for the project
settings.py: settings/configurations for the django project
urls.py the URL declarations for the django project, a "table of contents" of the django powered site
asgi.py: an entry point for ASGI compatible web servers to serve your project
wsgi.py: an entry point for WSGI compatible web servers

**startapp:**
creates an app, which includes:
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py

**runserver:**
starts the development server on internal IP at port 8000, to specify a specific port, pass it as an argument
i.e: python manage.py runserver 8000
not intended for production, just for developing. use a real webserver for development, like Apache, NGINX

**makemigrations:**
command to run when you make changes to the models and want the changes to be stored as a migration
a migration is how django stores changes to the models

**migrate:**
takes all migrations that haven't been applied and syncs changes to the models with the schema in the DB 

**sqlmigrate:**
prints to the screen what SQL Django thinks is required for the migration

**check**:
checks for any problems in project without making migrations or touching DB


<h2>Views</h2>
functions, to call a view, it needs to be mapped to a URL

<h2>Models</h2>
A model is the database layout. It contains the essnetial fiels and behaviors of the data you're storing.
Models are represented as classes in models.py.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

Each model has a number of class variables, which represent a database field in the model.
Each field is represented by an instance of a Field class like CharField for character fields, and DateTimeField for date times.
The database uses the field name as the column name. Some field classes have required arguments, others have several optional arguments.
Relationships are defined with ForeignKey. In the above example, the foreign key relates each choice to a single question.
https://stackoverflow.com/questions/42080864/set-in-django-for-a-queryset

Choice has a foreign key relationship with question meaning that each choice relates to a single question.
So every choice's question attribute will return its "parent" question. Every question will return its choices.
This can be done like so:
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save() : this saves the question into the database, must be called explicitly
q.id : this is the primary key
If we type in Question.objects.all(), we should see the question we just made:
    <QuerySet [<Question: Question object (1)>]>

We can access the question's fields like so:
q.question_text
q.pub_date

We can check for any choice objects related to this. This only works because of the foreign key relationship we created.
q.choice_set_all()
Choice is lower case because of the design of Django. q has access to a list of related choice objects with the choice_set attribute choice_set_all()
We can create choices by:
q.choice_set.create(choice_text='Not much', votes=0)

The choice objects have API access to their related question objects which is only natural do to the foreign key relationship.
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
c.question -> will return <Question: What's up?>

**Models API** 
Models API reference: https://docs.djangoproject.com/en/4.0/topics/db/queries/
[object].save() to save an object into the database
[model name].objects.all() to list all objects in the model
[model name].objects.filter(FILTER) to filter with some filter
    for example: Question.objects.filter(id=1)
                 Question.objects.filter(question_text__startswith='What')
[model name]_set/[model name]_set_all() and _set.count()

Field lookups use double underscores. https://docs.djangoproject.com/en/4.0/topics/db/queries/#field-lookups-intro

<h2>Settings</h2>
Installed apps: holds the named of all django applications that are activated in the django instance.
Default apps are:
    'django.contrib.admin'
    'django.contrib.auth': authentication system
    'django.contrib.contenttypes': framework for content types
    'django.contrib.sessions': session framework
    'django.contrib.messages': messaging framework
    'django.contrib.staticfiles: framework for managing static files

<h2>Database setup</h2>
Go to the DATABASES setting of settings.py
Put in the appropriate database connection settings.
For example, if you are using postgresql then the engine will be 'django.db.backends.postgresql'
For databases other than SQLite, you need USER, PASSSWORD and HOST.
Refer to: https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DATABASES

<h2>Admin</h2>
Can add objects to admin by registering it to admin. Open the admin.py file

Import the object you want in admin then register:
from .models import Question
admin.site.register(Question)

Now admin users can make questions
