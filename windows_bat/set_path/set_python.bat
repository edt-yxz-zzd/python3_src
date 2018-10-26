:set_python

goto start
tpl_variables:
    tpl_var_sys

set "PY_PYTHON=3.6"
set "pyhome=C:\Python36"

set "PY_PYTHON=3.6"
set "PY_PYTHON=3.6"
:start




@rem 3 ==>> ["py" -->> "py -3"]
@rem 3.6 ==>> ["py" -->> "py -3.6"]
set "PY_PYTHON=3"

:: now distingusih them
set "py_bin=C:\Python36"
set "pyhome=C:\Python36"

::: path=%path%;%pyhome%;%pyhome%\Scripts  # old
set "path=%path%;%py_bin%;%pyhome%\Scripts"
set "py_include=%pyhome%\include"
set "py_lib=%pyhome%\libs"




