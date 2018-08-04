
#ifndef __SCOPED_PYOBJ__
#define __SCOPED_PYOBJ__d
#include <Python.h>


template<typename T>
struct scoped_obj_attr
//{static void kill(T* mayNULL);}
;

template<typename T>
class scoped_obj
{
    T *obj;
public:
    scoped_obj(T *obj_):obj(obj_){}
    // move constructor... ; does compiler support it??
    
    operator T* (){return obj;}
    operator bool(){return obj;}
    T* operator -> (){return obj;}
    T& operator *(){return *obj;}
    
    T *get()const{return obj;}
    T *move_out(){T *tmp=obj; obj=NULL; return tmp;}
    void swap(scoped_obj& other){T *tmp=obj; obj=other.obj; other.obj=tmp;}
    ~scoped_obj(){scoped_obj_attr<T>::kill(obj);}
    
};

template<typename T>
void swap(scoped_obj<T>& lhs, scoped_obj<T>& rhs)
{
    lhs.swap(rhs);
}



//////////////////////////////////////
template<>
struct scoped_obj_attr<PyObject>
{
    static void kill(PyObject *obj){Py_XDECREF(obj);}
};

typedef scoped_obj<PyObject> scoped_pyobj;


////////////////////////////////////////////
#ifndef Py_LIMITED_API
template<>
struct scoped_obj_attr<Py_buffer>
{
    static void kill(Py_buffer *buf){PyBuffer_Release(buf);}
};

typedef scoped_obj<Py_buffer> scoped_pybuf;

#endif //Py_LIMITED_API



















/*
struct scoped_pyobj:public scoped_obj<PyObject>
{
    scoped_pyobj(PyObject *obj_):obj(obj_){}
    PyObject *get()const{return obj;}
    PyObject *move_out(){PyObject * tmp=obj; obj=NULL; return tmp;}
    ~scoped_pyobj(){Py_XDECREF(obj);}
    
};

#ifndef Py_LIMITED_API
class scoped_pybuf
{
    Py_buffer *buf;
public:
    scoped_pybuf(Py_buffer *buf_):buf(buf_){}
    Py_buffer *get()const{return buf;}
    Py_buffer *move_out(){Py_buffer * tmp=buf; buf=NULL; return tmp;}
    ~scoped_pybuf(){PyBuffer_Release(buf);}
    
};
#endif //Py_LIMITED_API
*/
#endif