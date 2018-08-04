
/* #define Py_LIMITED_API no Py_buffer */
// should I PyBuffer_Release() "y*" buffer? Yes!!!!!!
#include <Python.h>
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>
#include "nauty.h"
#include "nausparse.h"

typedef PyObject * PyObject_p;

#define PRINT_FOR_DEBUG 0

/* assume: setword is int */
/* assume: WORDSIZE = CHAR_BIT * sizeof int */


static statsblk stats;
static PyThreadState *_save = NULL;
static PyObject *_py_userautomproc = NULL; /* prevent re-entry */
static int _exc_userautomproc = 0; /* prevent multi-exceptions */


    #define DEAD(X) X(X)
    DEAD(DEAD);
    #define DEAD2(X) (DEAD2(X))
    DEAD2(DEAD2);
    #define DEAD3(X) (0, X(DEAD3))
    /*DEAD3(DEAD3);*/
    #define DEAD4  0, DEAD4
    static int _dead4 = DEAD4;
    #define DEAD5(x)  0, x(x)
    static int _dead5 = DEAD5(DEAD5);
    #define DEAD6(x)  0, DEAD7(x)
    #define DEAD7(x)  0, DEAD6(x)
    /*static int _dead6 = DEAD6(67);*/





enum EPY_INTSBUF_IDX {ilab = 0, iptn, iworkspace, iorbits, 
    PACKED_INTSBUF_END, ibegins=PACKED_INTSBUF_END, isizes, ineighbors, 
    SPARSE_INTSBUF_END};

enum EPY_SETSBUF_IDX {
    SPARSE_SETSBUF_END = 0, igraph=SPARSE_SETSBUF_END,
    PACKED_SETSBUF_END};
    


static void init_options(optionblk *p_options)
{
    p_options->defaultptn = FALSE;
    p_options->getcanon = FALSE;
    p_options->digraph = FALSE;
    p_options->writeautoms = FALSE;
    p_options->writemarkers = FALSE;
}

static void init()
{
    /*init_options(&packed_options);
    init_options(&sparse_options);*/
}
static void print_setwords(setword* row, int m, char const* head, char const* tail)
{
    int i = 0;
    printf("%s", head);
    for (i = 0; i < m; ++i){
        printf(SETWORD_FORMAT " ", row[i]);
    }
    printf("%s", tail);
}
static void print_packed_graph(graph* g, int n, int m, 
                                char const* head, char const* tail, 
                                char const* row_head, char const* row_tail)
{
    int i = 0;
    setword *row = g;
    printf("%s", head);
    for (i = 0; i < n; ++i, row += m){
        print_setwords(row, m, row_head, row_tail);
    }
    printf("%s", tail);
}
static void print_ints(int * ints, int n, char const* head, char const* tail)
{
    int i = 0;
    printf("%s", head);
    for (i = 0; i < n; ++i){
        printf("%i ", ints[i]);
    }
    printf("%s", tail);
}


#if PRINT_FOR_DEBUG
#else
    #define EMPTY_STAT do{}while(0)
    #define puts(X) EMPTY_STAT
    #define printf(X, ...) EMPTY_STAT
    #define print_ints(X, ...) EMPTY_STAT
    #define print_setwords(X, ...) EMPTY_STAT
    #define print_packed_graph(X, ...) EMPTY_STAT
    
#endif

#define NOTHING

static void c_userautomproc(int count, permutation *perm, int *orbits,
                            int numorbits, int stabvertex, int n){
    PyObject *r = NULL;
    if (_exc_userautomproc) return NOTHING;
    assert(_py_userautomproc);
    
    assert(_save);
    Py_BLOCK_THREADS
    _save = NULL;
    
    puts("c_userautomproc");
    print_ints((int*)perm, n, "permutation = (", ")\n");
    print_ints((int*)orbits, n, "orbits = (", ")\n");
    
    r = PyObject_CallFunction(
        _py_userautomproc, "{sisy#sy#sisisi}",
        "count", count,
        "perm", perm, sizeof(perm[0]) * n,
        "orbits", orbits, sizeof(orbits[0]) * n,
        "numorbits", numorbits,
        "stabvertex", stabvertex,
        "n", n);
    
    if (NULL != r) Py_DECREF(r);
    else _exc_userautomproc = 1; /* error occured */
    
    assert(_save == NULL); 
    Py_UNBLOCK_THREADS
    assert(_save);
    
    return NOTHING;
}




static void LsPyBuffer_Release(Py_buffer bufs[], int size)
{
    while (size --> 0){
        PyBuffer_Release(bufs + size);
    }
}

static int is_buffer(Py_buffer const* buf, size_t itemsize, char const *fmt)
{
    puts("format");
    if (NULL != buf->format) puts(buf->format);
    else puts("buf->format is NULL!");
    if (NULL != buf->format && NULL != fmt && 
        0 != strcmp(buf->format, fmt)){
        PyErr_SetString(PyExc_TypeError, "bad buffer format");
        return 0;
    }
    
    puts("itemsize");
    if (itemsize != buf->itemsize){
        PyErr_SetString(PyExc_TypeError, "bad buffer itemsize");
        return 0;
    }
    
    puts("contiguous");
    if (1 != PyBuffer_IsContiguous(buf, 'C')){
        PyErr_SetString(PyExc_TypeError, "bad buffer type, should be C-style contiguous");
        return 0;
    }
    
    return 1;
}

static int is_buffers(Py_buffer const* bufs, int bufs_len, 
                      size_t itemsize, char const *fmt){
    int i = bufs_len;
    while(i --> 0){
        if (! is_buffer(bufs + i, itemsize, fmt)){
            return 0;
        }
    }
    
    return 1;
}


static int is_larger_enough(Py_buffer const* buf, Py_ssize_t len)
{
    if (buf->len < len){
        PyErr_SetString(PyExc_ValueError, "buffer size too small");
        return 0;
    }
    return 1;
    
}
static int are_larger_enough(Py_buffer const* bufs, int bufs_len, 
                            Py_ssize_t const lens[])
{
    int i = bufs_len;
    while(i --> 0){
        if (! is_larger_enough(bufs + i, lens[i])){
            return 0;
        }
    }
    
    return 1;
    
}

static int  check_lab(int* lab, int n)
{
    int i = n;
    while(i --> 0){
        if (lab[i] >= n || lab[i] < 0){
            printf("lab[%i] == %i but n == %i\n", i, lab[i], n);
            PyErr_SetString(PyExc_ValueError, "not 0 <= lab[i] < n");
            return 0;
        }
    }
    return 1;
}
static int  check_ptn(int* ptn, int n)
{
    int i = n;
    while(i --> 0){
        if (ptn[i] != 1 && ptn[i] != 0){
            PyErr_SetString(PyExc_ValueError, "ptn[i] != 1 && ptn[i] != 0");
            return 0;
        }
    }
    return 1;
}

static int pre_parse_args(){
    if (WORDSIZE != CHAR_BIT * sizeof(int)){
        PyErr_SetString(PyExc_RuntimeError, "nauty::WORDSIZE != CHAR_BIT * sizeof(int)");
        return 0;
    }
    
    if (NULL != _py_userautomproc){
        PyErr_SetString(PyExc_RuntimeError, "nauty forbid re-entrance");
        return 0;
    }
    assert(! _exc_userautomproc);
    
    
    return 1;
}
static int check_args_N_calc_worksize(
    optionblk *p_options, int directed, int n, int m, int wordsize, 
    PyObject *py_userautomproc,
    Py_buffer bufs[], int bufs_len, Py_ssize_t lens[],
    Py_buffer setbufs[], int setbufs_len, Py_ssize_t setlens[]){
    int worksize = 0;
    int i = 0;
    
    assert (directed == 0 || directed == 1);
    
    /* Note that any Python object references which are provided to the caller are borrowed references; do not decrement their reference count!*/
    if (n <= 0 || m <= 0 || 
        wordsize != WORDSIZE || (n+WORDSIZE-1)/WORDSIZE > m)
    {
        PyErr_SetString(PyExc_ValueError, "bad args: n, m, py::WORDSIZE");
        goto ERR_RELEASE_BUFS;
    }
    
    puts("bufs");
    if (! is_buffers(bufs, bufs_len, sizeof(int), "i") ||
        ! is_buffers(setbufs, setbufs_len,WORDSIZE/CHAR_BIT, NULL)){
        goto ERR_RELEASE_BUFS;
    }

    
    puts("lens");
    
    lens[ilab] = lens[iptn] = lens[iorbits] = n;
    lens[iworkspace] = bufs[iworkspace].len;
    
    worksize = lens[iworkspace];
    if (worksize <= 0 || worksize != lens[iworkspace]){
        PyErr_SetString(PyExc_ValueError, "bad args: worksize too big");
        goto ERR_RELEASE_BUFS;
    }
    if (worksize/m < 50) {
        PyErr_SetString(PyExc_ValueError, "bad args: worksize too small");
        goto ERR_RELEASE_BUFS;
    }
    
    
    if (! are_larger_enough(bufs, bufs_len, lens) ||
        ! are_larger_enough(setbufs, setbufs_len, setlens)){
        goto ERR_RELEASE_BUFS;
    }

    
    

    if (! check_lab((int*)bufs[ilab].buf, n) || 
        ! check_ptn((int*)bufs[iptn].buf, n)){
        goto ERR_RELEASE_BUFS;
    }

    
    
    p_options->digraph = directed? TRUE : FALSE;
    if (Py_None == py_userautomproc) {
        p_options->userautomproc = NULL;
    }
    else if (! PyCallable_Check(py_userautomproc)){
        PyErr_SetString(PyExc_ValueError, "bad args: userautomproc not callable");
        goto ERR_RELEASE_BUFS;
    }
    else
    {
        p_options->userautomproc = c_userautomproc;
    }
    
    assert(worksize);
    nauty_check(WORDSIZE,m,n,NAUTYVERSIONID);
    
    return worksize;
ERR_RELEASE_BUFS:
    return 0;
}



static void __real_call(PyObject *py_userautomproc, graph *p_graph, 
                        optionblk *p_options,
                        Py_buffer bufs[], int worksize, int n, int m)
{
    assert(_py_userautomproc == NULL);
    _py_userautomproc = py_userautomproc;
    
    /*MAP_F(INCR_PYOBJ, ENDOFSTAT);*/
    puts("Py_INCREF");
    Py_INCREF(_py_userautomproc);
    
    {
        assert(_exc_userautomproc == 0);
        assert(_save == NULL); 
        Py_UNBLOCK_THREADS
        assert(_save);
    
        {
            puts("before nauty");
            print_ints((int*)bufs[ilab].buf, n, "lab = (", ")\n");
            print_ints((int*)bufs[iptn].buf, n, "ptn = (", ")\n");
            puts("nauty");
            
            stats.errstatus = 0;
            nauty(p_graph,
                  (int*)bufs[ilab].buf,
                  (int*)bufs[iptn].buf,
                  NULL,
                  (int*)bufs[iorbits].buf,
                  p_options,
                  &stats,
                  (set*)bufs[iworkspace].buf,
                  worksize, m, n, NULL);
        
            if (stats.errstatus)
            {
                /* error */
            }
            else
            {
                print_ints((int*)bufs[ilab].buf, n, "lab = (", ")\n");
                print_ints((int*)bufs[iptn].buf, n, "ptn = (", ")\n");
                print_ints((int*)bufs[iorbits].buf, n, "orbits = (", ")\n");
            }
        }

        assert(_save);
        Py_BLOCK_THREADS
        _save = NULL;
        
    }

    
    Py_DECREF(_py_userautomproc);
    /*MAP_F(DECR_PYOBJ, ENDOFSTAT);*/
    _py_userautomproc = NULL;
}

static char const *get_error_info(int error)
{
    static struct {int const err; char const *const msg;} const
    errmsg[] = {
        {MTOOBIG, "MTOOBIG: n > MAXN or n > WORDSIZE*m"}, 
        {NTOOBIG, "NTOOBIG: m > MAXM"}, 
        {CANONGNIL, "CANONGNIL: canong = NULL, but getcanon = TRUE"}};
    int i = sizeof(errmsg) / sizeof(errmsg[0]);
    
    if (! error) return "";
    
    while (i --> 0){
        if (errmsg[i].err == error){
            return errmsg[i].msg;
        }
    }
    return "UNKNOWN";
}

/*/////////////////////////////////////////////////////////*/
static PyObject *call_cnauty_packed(PyObject *self, PyObject *args)
{
    Py_buffer bufs[PACKED_INTSBUF_END]; /* for ints */     
    int const bufs_len = PACKED_INTSBUF_END;
    Py_ssize_t lens[PACKED_INTSBUF_END];
    
    
    Py_buffer setbufs[PACKED_SETSBUF_END]; /* for graph */ 
    int const setbufs_len = PACKED_SETSBUF_END;
    Py_ssize_t setlens[PACKED_SETSBUF_END];
    
    
    int n = 0;
    int m = 0;
    int wordsize = 0;
    int worksize = 0;
    PyObject *result = NULL;
    int directed = FALSE;
    

    Py_buffer *const py_lab = bufs + ilab;
    Py_buffer *const py_ptn = bufs + iptn;
    Py_buffer *const py_workspace = bufs + iworkspace;
    Py_buffer *const py_orbits = bufs + iorbits;
    
    
    Py_buffer *const py_graph = setbufs + igraph;
    PyObject *py_userautomproc = NULL;    
    
    DEFAULTOPTIONS_GRAPH(packed_options);
    init_options(&packed_options);
    

    if (! pre_parse_args()) return NULL;
        
    /*MAP_F(DEFINE_PYOBJ_P, ENDOFSTAT);*/
    if (! PyArg_ParseTuple(args, "iy*w*w*w*w*Obii", 
            &n, py_graph, py_lab, py_ptn, py_workspace, 
            py_orbits, &py_userautomproc, &directed, &m, &wordsize))
    {
        return NULL;
    }
    
    puts("PyArg_ParseTuple()");
    
    setlens[igraph] = (Py_ssize_t) n * (Py_ssize_t) m;
    worksize = check_args_N_calc_worksize(
        &packed_options, directed, n, m, wordsize, py_userautomproc,
        bufs, bufs_len, lens, 
        setbufs, setbufs_len, setlens);
    if (! worksize) goto ERR_RELEASE_BUFS;

    
    if (setlens[igraph] / (Py_ssize_t)n != (Py_ssize_t)m){
        PyErr_SetString(PyExc_ValueError, "bad args: n, m too big");
        goto ERR_RELEASE_BUFS;
    }
    
    print_packed_graph((graph*)py_graph->buf, n, m, "", "", ":", "\n");
    __real_call(py_userautomproc, (graph*)py_graph->buf, 
                &packed_options,
                bufs, worksize, n, m);

    
    if (! _exc_userautomproc){
        /*result = PyLong_FromLong(stats.errstatus);*/
        result = PyUnicode_FromString(get_error_info(stats.errstatus));
    }
    _exc_userautomproc = 0;
ERR_RELEASE_BUFS:
    LsPyBuffer_Release(setbufs, setbufs_len);
    LsPyBuffer_Release(bufs, bufs_len);
    return result;
}




/*/////////////////////////////////////////////*/
static PyObject *call_cnauty_sparse(PyObject *self, PyObject *args)
{
    Py_buffer bufs[SPARSE_INTSBUF_END]; /* for ints */     
    int const bufs_len = SPARSE_INTSBUF_END;
    Py_ssize_t lens[SPARSE_INTSBUF_END];
    
    
    Py_buffer setbufs[SPARSE_SETSBUF_END+1]; /* for graph */ /* zero-length */
    int const setbufs_len = SPARSE_SETSBUF_END;
    Py_ssize_t setlens[SPARSE_SETSBUF_END+1];
    
    
    int n = 0;
    int m = 0;
    int wordsize = 0;
    int worksize = 0;
    PyObject *result = NULL;
    int directed = FALSE;
    

    Py_buffer *const py_lab = bufs + ilab;
    Py_buffer *const py_ptn = bufs + iptn;
    Py_buffer *const py_workspace = bufs + iworkspace;
    Py_buffer *const py_orbits = bufs + iorbits;
    Py_buffer *const py_begins = bufs + ibegins;
    Py_buffer *const py_sizes = bufs + isizes;
    Py_buffer *const py_neighbors = bufs + ineighbors;
    int nde = 0;
    
    PyObject *py_userautomproc = NULL;    
    
    DEFAULTOPTIONS_SPARSEGRAPH(sparse_options);
    init_options(&sparse_options);
    

    if (! pre_parse_args()) return NULL;
        
    /*MAP_F(DEFINE_PYOBJ_P, ENDOFSTAT);*/
    if (! PyArg_ParseTuple(args, "iiy*y*y*w*w*w*w*Obii", 
            &n, &nde, py_begins, py_sizes, py_neighbors, 
            py_lab, py_ptn, py_workspace, 
            py_orbits, &py_userautomproc, &directed, &m, &wordsize))
    {
        return NULL;
    }
    
    puts("PyArg_ParseTuple()");
    

    if (nde < 0) {
        PyErr_SetString(PyExc_ValueError, "bad args: nde < 0");
        goto ERR_RELEASE_BUFS;
    }
    
    lens[ibegins] = lens[isizes] = n;
    lens[ineighbors] = nde;
    worksize = check_args_N_calc_worksize(
        &sparse_options, directed, n, m, wordsize, py_userautomproc,
        bufs, bufs_len, lens, 
        setbufs, setbufs_len, setlens);
    if (! worksize) goto ERR_RELEASE_BUFS;

    

    {
        sparsegraph sg;
        SG_INIT(sg);
        sg.nv = n;
        sg.nde = nde;
        sg.v = py_begins->buf;
        sg.d = py_sizes->buf;
        sg.e = py_neighbors->buf;
        sg.w = NULL;
        sg.vlen = n;
        sg.dlen = n;
        sg.elen = nde;
        sg.wlen = 0;

        /*print_packed_graph((graph*)py_graph->buf, n, m, "", "", ":", "\n");*/
        __real_call(py_userautomproc, (graph*)&sg, 
                    &sparse_options,
                    bufs, worksize, n, m);
    }
    
    if (! _exc_userautomproc){
        /*result = PyLong_FromLong(stats.errstatus);*/
        result = PyUnicode_FromString(get_error_info(stats.errstatus));
    }
    _exc_userautomproc = 0;
ERR_RELEASE_BUFS:
    LsPyBuffer_Release(setbufs, setbufs_len);
    LsPyBuffer_Release(bufs, bufs_len);
    return result;
}



/*/////////////////////////////////////////////*/
#define TO_STRING(X) #X

static PyObject *get_NAUTYVERSIONID(PyObject *self, PyObject *args)
{
    if (! PyArg_ParseTuple(args, ""))return NULL;
    return PyLong_FromLong(NAUTYVERSIONID);
}
static PyObject *get_nauty_WORDSIZE(PyObject *self, PyObject *args)
{
    if (! PyArg_ParseTuple(args, ""))return NULL;
    return PyLong_FromLong(WORDSIZE);
}
static PyObject *get_INT_BIT(PyObject *self, PyObject *args)
{
    if (! PyArg_ParseTuple(args, ""))return NULL;
    return PyLong_FromLong(CHAR_BIT * sizeof(int));
}

static PyObject *get_CHAR_BIT(PyObject *self, PyObject *args)
{
    if (! PyArg_ParseTuple(args, ""))return NULL;
    return PyLong_FromLong(CHAR_BIT);
}

static PyObject *get_NAUTY_INFINITY(PyObject *self, PyObject *args)
{
    if (! PyArg_ParseTuple(args, ""))return NULL;
    return PyLong_FromLong(NAUTY_INFINITY);
}



/*/////////////////////////////////////////////*/

/*/////////////////////////////////////////////*/
static PyMethodDef pymodule_methods[] = {

    {"call_cnauty_packed",  call_cnauty_packed, METH_VARARGS,
     "call C nauty(). can't not re-entrance.\n\n"
     "using packed graph form, that is an adjecence matrix\n"
     "args: n, graph, lab, ptn, workspace, orbits, userautomproc, m, WORDSIZE\n"
     "in: n, graph, userautomproc, m, WORDSIZE\n"
     "out: orbits\n"
     "inout: lab, ptn\n"
     "tmpbuf: workspace\n\n"
     "type:\n\t"
     "int - n, m, WORDSIZE;\n\t"
     "int[] buf - graph, lab, ptn, workspace, orbits;\n\t"
     "void (...) - userautomproc;"
     
    },
    {"call_cnauty_sparse", call_cnauty_sparse, METH_VARARGS,
     "like call_cnauty_packed, but using sparse graph form"
    },
    {"get_INT_BIT", get_INT_BIT, METH_VARARGS,
     "bit length of c::int"
    },
    {"get_CHAR_BIT", get_CHAR_BIT, METH_VARARGS,
     "bit length of c::char"
    },
    {"get_nauty_WORDSIZE", get_nauty_WORDSIZE, METH_VARARGS,
     "nauty::WORDSIZE, bit length of nauty::setword"
    },
    {"get_NAUTYVERSIONID", get_NAUTYVERSIONID, METH_VARARGS,
     "nauty::NAUTYVERSIONID"
    },
    {"get_NAUTY_INFINITY", get_NAUTY_INFINITY, METH_VARARGS,
     "nauty::NAUTY_INFINITY"
    },
    
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef pymodule = {
   PyModuleDef_HEAD_INIT,
   "call_cnauty",   /* name of module */
   NULL, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   pymodule_methods
};

PyMODINIT_FUNC
PyInit_call_cnauty(void)
{
    init();
    return PyModule_Create(&pymodule);
}


