rem You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
rem Run 'python manage.py migrate' to apply them.

rem Ctrl+C to quit.
rem beginwith:  http://127.0.0.1:8000/old/
rem or:         http://127.0.0.1:8000/new/
rem or:         http://127.0.0.1:8000/all/
rem or:         http://127.0.0.1:8000/
rem or:         http://127.0.0.1:8000/index/
py -m nn_ns.app.Django.mzitu_com.mzitu_com_project_main.manage runserver

