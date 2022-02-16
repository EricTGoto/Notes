Don't put python code within the web server's document root, because it may be possible.

**Commands:**

startproject xxxxx
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

