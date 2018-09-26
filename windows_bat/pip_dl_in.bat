set PY_DOWNLOADS=E:\software\programming\Python\all_downloads
py -m pip download %* -d %PY_DOWNLOADS%
@rem py -m pip install %* -d %PY_DOWNLOADS%
@rem py -m pip install %* --cache-dir %PY_DOWNLOADS%
py -m pip install %*

