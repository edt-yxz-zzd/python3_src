
#ifndef Py_LIMITED_API
    #define Py_LIMITED_API
    #include <Python.h>
    #undef  Py_LIMITED_API
#else
    #include <Python.h>
#endif  // Py_LIMITED_API

// struct PyObject; // why fail !!!!!!!!!!!!!!!!!!!!!
