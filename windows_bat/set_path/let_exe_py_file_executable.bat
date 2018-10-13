::  since I open ".py" file by GVim, ".py" file now is not executable
::  I rename ".py" script to ".exe_py", and make ".exe_py" executable
::
:: below will handle register directly!!! not environment!
assoc .exe_py="executable python script"
ftype "executable python script"=py "%1" %*
