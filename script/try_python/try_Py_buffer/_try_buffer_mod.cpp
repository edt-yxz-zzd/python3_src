


/* #define Py_LIMITED_API no Py_buffer */
// call PyBuffer_Release !! for "w*" ? "y*" ...!!
#include <Python.h>
#include <iostream>

//#include "limit_py.h"
#include "gil_lock.hpp"
#include "scoped_pyobj.hpp"



using namespace std;



static PyObject *_try_buffer(PyObject *self, PyObject *args)
{
    Py_buffer w_star_readwrite, y_star_readonly;
    PyObject *getrefcount = NULL;
    
    if (! PyArg_ParseTuple(args, "Ow*y*", 
            &getrefcount, &w_star_readwrite, &y_star_readonly))
    {
        return NULL;
    }
    
    scoped_obj<Py_buffer> _w(&w_star_readwrite);
    scoped_obj<Py_buffer> _y(&y_star_readonly);
    


    
    PyObject *r = NULL;
    try { do
    {
        if (! PyCallable_Check(getrefcount)){
            PyErr_SetString(PyExc_TypeError, "getrefcount not callable");
            break;
        }
        scoped_obj<PyObject> w_count = PyObject_CallFunctionObjArgs(
                        getrefcount, w_star_readwrite.obj, NULL);
        if (! w_count) break;
        
        scoped_obj<PyObject> y_count = PyObject_CallFunctionObjArgs(
                        getrefcount, y_star_readonly.obj, NULL);
        if (! y_count) break; // auto decref w_count
        
        
        int res;
        {threads_allow _t;
        
        // ....
        res = 3;
        }
        
        r = Py_BuildValue("OO", w_count.get(), y_count.get());
        // what if...
        // _y.move_out(); // try not to release y*, fail!
        // _w.move_out(); // try not to release w*, fail!
        
    } while(0); }
    catch(char const* e){
        cerr << "C++ exception:" << e << endl;
        PyErr_SetString(PyExc_RuntimeError, e);
        r = NULL;
    }
    catch(...){
        cerr << "C++ exception" << endl;
        PyErr_SetString(PyExc_RuntimeError, "C++ exception");
        r = NULL;
    }
    
    
    //PyBuffer_Release(&w_star_readwrite);
    //PyBuffer_Release(&y_star_readonly);
    return r;
}



/*/////////////////////////////////////////////*/
static PyMethodDef pymodule_methods[] = {

    {"_try_buffer",  _try_buffer, METH_VARARGS,
     "try Py_buffer. y* and w* are both needed to be released?"
     
    },

    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef pymodule = {
   PyModuleDef_HEAD_INIT,
   "_try_buffer",   /* name of module */
   NULL, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   pymodule_methods
};

PyMODINIT_FUNC
PyInit__try_buffer(void)
{
    
    return PyModule_Create(&pymodule);
}


