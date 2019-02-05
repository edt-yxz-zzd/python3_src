"Django for Beginners -- Learn Web Development with Django 2.0 (2018).pdf"


###############################################
Chapter 2: Hello World app
###############################################

project:
    $ mkdir helloworld
    $ cd helloworld
    $ django-admin startproject helloworld_project .
        # NOTE: "." at last
    $ tree
        # see below 'tree.com . /F' for DOS
    $ py manage.py runserver
        # website: http://127.0.0.1:8000/
        # Ctrl+C to quit

> tree.com . /F
.../HELLOWORLD
│  manage.py
│
└─helloworld_project
        settings.py
        urls.py
        wsgi.py
        __init__.py


app:
    $ py manage.py startapp pages
    ...update<helloworld_project.settings.py::INSTALLED_APPS>+=['pages']
    ...add<pages.views.py::def homePageView>
    ...add<pages.urls.py>::urlpatterns = [path('', views.homePageView, name='home')]
        # regular expression of path: ''
        # an optional url name: 'home'
        #   URL pattern name used in templates
        #       as argument for template tag # see ch3
    ...update<helloworld_project.urls.py::urlpatterns> += [path('', include('pages.urls'))]




###############################################
Chapter 3: Pages app
###############################################
$ mkdir ch3
$ cd ch3
$ django-admin startproject pages_project .
$ python manage.py startapp pages
...update<pages_project.settings.py::INSTALLED_APPS>+=['pages']

$ mkdir templates
$ touch templates/home.html
    # make empty html file
    # then write:
    <!-- templates/home.html -->
    <h1>Homepage.</h1>
...update<pages_project.settings.py::TEMPLATES[0]['DIRS']>+=[os.path.join(BASE_DIR, 'templates')]


...add<pages.views.py::class HomePageView(TemplateView)>
...update<pages_project.urls.py::urlpatterns> += [path('', include('pages.urls'))]
...add<pages.urls.py>::urlpatterns = [path('', views.HomePageView.as_view(), name='home')]

$ touch templates/about.html
    <!-- templates/about.html -->
    <h1>About page.</h1>
...add<pages.views.py::class AboutPageView(TemplateView)>
...update<pages.urls.py::urlpatterns> += [path('about/', views.AboutPageView.as_view(), name='about')]



$ touch templates/base.html
    <!-- templates/base.html -->
    <header>
        <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>
    </header>

    {% block content %}
    {% endblock %}
    <!-- At the bottom we've added a "block" tag called "content". Blocks can be overwritten by child templates via inheritance. -->


...update "home.html" & "about.html"
    <!-- templates/home.html -->
    {% extends 'base.html' %}
    {% block content %}
        <h1>Homepage.</h1>
    {% endblock %}

    <!-- templates/about.html -->
    {% extends 'base.html' %}
    {% block content %}
        <h1>About page.</h1>
    {% endblock %}

...test add<pages.tests.py::class SimpleTests(SimpleTestCase)>
$ py manage.py test
