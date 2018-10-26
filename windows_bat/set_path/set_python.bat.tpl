:set_python

goto start
tpl_variables:
    tpl_var_sys

set "PY_PYTHON=3.6"
set "pyhome=C:\Python36"

set "PY_PYTHON={tpl_var_sys.version_info.major}.{tpl_var_sys.version_info.minor}"
set "PY_PYTHON={tpl_var_sys.winver}"
:start




@rem 3 ==>> ["py" -->> "py -3"]
@rem 3.6 ==>> ["py" -->> "py -3.6"]
set "PY_PYTHON={tpl_var_sys.version_info.major}"

:: now distingusih them
set "py_bin={tpl_var_sys.exec_prefix}"
set "pyhome={tpl_var_sys.prefix}"

::: path=%path%;%pyhome%;%pyhome%\Scripts  # old
set "path=%path%;%py_bin%;%pyhome%\Scripts"
set "py_include=%pyhome%\include"
set "py_lib=%pyhome%\libs"




