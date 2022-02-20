<h2>Terminology</h2>

**View:**: python function that takes a web request and returns a web response

**URLConf**: mapping between URL path expressions to python functions

**Models (database)**: datababase layout, with additional metadata

**Context:** a dictionary with variable names as the key and their values as the value. Templates are passed contexts and use them to display data, etc.


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

The outer xxxxx/ is the root directory. Can be renamed manage.py: command-line utility that lets you interact with the django project 
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
functions, to call a view, it needs to be mapped to a URL. Can also be thought of as a type of web page in the django application.

In django, web pages and other contect are delivered by views. Each view is represented by a Python function.

A URL pattern is the general form of a URL. e.g. /newsarchive/<year>/<month>/

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

if a user requests /polls/34/, it will run the detail() method and display the ID they provide in the URL (34).
Django loads the mysite.urls python module because its pointed to by the ROOT_URLCONF setting. It finds the variable urlpatterns and traverses the patterns in order.
It will find a match at 'polls/', then strips off the matching test 'polls/' and sends the remaining text - '34/' to the polls.urls URLconf for further processing. 
There it matches '<int:question_id>/', resulting in a call to detail() like:

detail(request=<HttpRequest object>, question_id=34)

The question_id=34 part comes from <int:question_id>. Using angle brackets "captures" part of the URL and sends it as a keyword argument to the view function. The question_id part identifies the pattern name and the int part is the converter. : separates the converter and pattern name.

A view just wants the HttpResponse or an exception. The rest is up to the programmer.

**Templates:**

https://docs.djangoproject.com/en/4.0/topics/templates/

We can separate the way a page looks from python by creating a template that the view can use.

Tip: templates should be namespaced - templates should be put inside another directory named for the application itself polls/templates/polls/

It's very common to load a template, fill a context and return an HttpResponse so Django provides a shortcut with render(), which is from django.shortcuts
render takes the request object as its first argument, a template name as its second and a dictionary as its optional third argument and returns an HttpResponse.

Django templates use {% %} in the html. This is django specific.

Remove hardcoded URLs in templates by using the {% url %} template tag.

For example:

````
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
````

Here, /polls/ is hardcoded. So instead of this we can:

````
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
````

The {% url %} tag works by looking up the url definition as specified in the polls/urls module. It will look up the url in 'detail':

````
path('<int:question_id>/', views.detail, name='detail'),
````

Since in this urls.py (URLconf) we are already at the polls/ level, the {% url %} tag will return polls/.

Namespace a URLconf by adding an app_name variable. Refer to the end of the django tutorial part 3.


**Generic Views:**

A frequent case of basic web development is getting data from a database according to a parameter passed in the URL, loading a template and then returning the template.
This is very common so Django provides a shortcut. 

We make the following changes:

From:
````
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

views.py:

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
````

To:
````
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

views.py:
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.

````

Each generic view needs to know what model it will be acting upon.

The matched pattern im the URLconf is changed because the DetailView expects the primary key value captured from the URL to be called "pk".

The template_name attribute in the Views tell Django to use a specific template name instead of the default which is <app name>/<model name>_detail.html for DetailView and <app name>/<model name>_list.html.

In the non generic views, a context was passed to render, but with generic views, they are passed automatically. With DetailView, the **question** variable is provided automatically since we are using the Django model **Question**. For Listview, the automatically generated variable has _list appended to it so it is question_list, but since we made the context variable in the template latest_question_list, we can override the default by using the attribute **context_object_name**.

<h2>Django functions</h2>

**render:**

You can use render() to load a template, fill a context and return an HttpResponse object.

````
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
````

versus:

````
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
````
**get_object_or_404:**

takes a Django model as its first argument and an arbitrary number of keyword arguments which it passes to the get() function of the model's manager


Instead of
````
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
````

You can use get_object_or_404:
````
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
````

<h2>Models</h2>
A model is the database layout. It contains the essential fiels and behaviors of the data you're storing.
Models are represented as classes in models.py.

````
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
````

````
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
````

Each model has a number of class variables, which represent a database field in the model.
Each field is represented by an instance of a Field class like CharField for character fields, and DateTimeField for date times.
The database uses the field name as the column name. Some field classes have required arguments, others have several optional arguments.
Relationships are defined with ForeignKey. In the above example, the foreign key relates each choice to a single question.

https://stackoverflow.com/questions/42080864/set-in-django-for-a-queryset

Choice has a foreign key relationship with question meaning that each choice relates to a single question.
So every choice's question attribute will return its "parent" question. Every question will return its choices.
This can be done like so:

````
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save() : this saves the question into the database, must be called explicitly
q.id : this is the primary key
````

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

<h2>Automated Testing/TDD</h2>

In a sophisticated or large application there will be many interactions between components and this will be hard or tedious to test manually. Having a set of tests that are gradually built up as you write your application will save you from having to perform manual testing for the ever growing complexity of the developing application. 

In test driven development, tests are written before code. 

We create tests in the tests.py file in the specific application. To run tests we type python manage.py test polls in the shell. The test polls function will look for test methods - anything that starts with test. Therefore, tests must begin with test.

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

<h2>Query</h2>