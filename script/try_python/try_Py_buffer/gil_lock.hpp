
#ifndef gil_lock_hpp_HEAD_INCLUDED
#define gil_lock_hpp_HEAD_INCLUDED
#include "gil_lock.hpp"

#include "limit_py.h"

/// @brief RAII class used to lock and unlock the GIL.

/*
Non-Python created threads
(often this will be part of a callback API provided by the aforementioned third-party library)
*/
class gil_lock
{
public:
  gil_lock()  { state_ = PyGILState_Ensure(); }
  ~gil_lock() { PyGILState_Release(state_);   }
private:
  PyGILState_STATE state_;
};


/*
Releasing the GIL from extension code

Save the thread state in a local variable.
Release the global interpreter lock.
... Do some blocking I/O operation ...
Reacquire the global interpreter lock.
Restore the thread state from the local variable.

*/
class threads_allow
{
public:
  threads_allow()  { Py_UNBLOCK_THREADS }
  ~threads_allow() { Py_BLOCK_THREADS   }
private:
  PyThreadState *_save; // used in Py_UNBLOCK_THREADS
};

#endif
