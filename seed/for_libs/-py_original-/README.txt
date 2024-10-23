
e ../../python3_src/seed/for_libs/-py_original-/README.txt
some py std lib in both pure form & binary form:
  io
  importlib
  ...



[[[
io
importlib
===
Python 3.11.9 (main, Jun 10 2024, 00:57:33) [Clang 17.0.2 (https://android.googlesource.com/toolchain/llvm-project d9f89f4d1 on linux
  #patch:...)]

>>> import _pyio
>>> help(_pyio)

>>> import importlib
>>> help(importlib)


-->:
/data/data/com.termux/files/usr/lib/python3.11/_pyio.py
/data/data/com.termux/files/usr/lib/python3.11/importlib/__init__.py

-->:
~/../usr/lib/python3.11/_pyio.py
~/../usr/lib/python3.11/importlib/__init__.py

ls ~/../usr/lib/python3.11/importlib/


!mkdir ../../python3_src/seed/for_libs/-py_original-/
!mkdir ../../python3_src/seed/for_libs/-py_original-/py3_11_9
#cp -iv -t ../../python3_src/seed/for_libs/-py_original-/py3_11_9/ -r ~/../usr/lib/python3.11/importlib/*
#rm -r ../../python3_src/seed/for_libs/-py_original-/py3_11_9/*
du -h  ~/../usr/lib/python3.11/importlib/
cp -iv -t ../../python3_src/seed/for_libs/-py_original-/py3_11_9/  -r ~/../usr/lib/python3.11/importlib/
find ../../python3_src/seed/for_libs/-py_original-/py3_11_9/  -type d -name __pycache__ -delete
find: cannot delete ‘../../python3_src/seed/for_libs/-py_original-/py3_11_9/importlib/__pycache__’: Directory not empty

find ../../python3_src/seed/for_libs/-py_original-/py3_11_9/  -path '**/__pycache__/**' -delete
du -h  ../../python3_src/seed/for_libs/-py_original-/py3_11_9/
  278K
[[
tree -h --du  ../../python3_src/seed/for_libs/-py_original-/py3_11_9/
[224K]  ../../python3_src/seed/for_libs/-py_original-/py3_11_9/
└── [221K]  importlib
    ├── [5.9K]  __init__.py
    ├── [1.8K]  _abc.py
    ├── [ 47K]  _bootstrap.py
    ├── [ 67K]  _bootstrap_external.py
    ├── [ 11K]  abc.py
    ├── [ 880]  machinery.py
    ├── [ 44K]  metadata
    │   ├── [ 30K]  __init__.py
    │   ├── [1.8K]  _adapters.py
    │   ├── [ 743]  _collections.py
    │   ├── [2.8K]  _functools.py
    │   ├── [2.0K]  _itertools.py
    │   ├── [1.1K]  _meta.py
    │   └── [2.1K]  _text.py
    ├── [ 327]  readers.py
    ├── [ 26K]  resources
    │   ├── [ 506]  __init__.py
    │   ├── [4.4K]  _adapters.py
    │   ├── [2.8K]  _common.py
    │   ├── [ 884]  _itertools.py
    │   ├── [3.4K]  _legacy.py
    │   ├── [4.5K]  abc.py
    │   ├── [3.5K]  readers.py
    │   └── [3.0K]  simple.py
    ├── [ 354]  simple.py
    └── [ 12K]  util.py

 503K used in 4 directories, 24 files
  #bug??503K vs 224K
]]



===
cp -iv -t ../../python3_src/seed/for_libs/-py_original-/py3_11_9/  ~/../usr/lib/python3.11/_pyio.py
du -h ../../python3_src/seed/for_libs/-py_original-/py3_11_9/_pyio.py
  92K

===
]]]









:view +set\ nomodifiable ../../python3_src/seed/for_libs/-py_original-/py3_11_9/_pyio.py

:view +set\ nomodifiable ../../python3_src/seed/for_libs/-py_original-/py3_11_9/importlib/abc.py
:view +set\ nomodifiable ../../python3_src/seed/for_libs/-py_original-/py3_11_9/importlib/_abc.py
:view +set\ nomodifiable ../../python3_src/seed/for_libs/-py_original-/py3_11_9/importlib/machinery.py

:view +set\ nomodifiable ../../python3_src/seed/for_libs/-py_original-/py3_11_9/importlib/__init__.py
  \<_bootstrap\>
  \<util\>
:view +set\ nomodifiable ../../python3_src/seed/for_libs/-py_original-/py3_11_9/importlib/_bootstrap.py
  \<_find_spec\>
  \<_gcd_import\>
  \<_exec\>
  \<__import__\>
:view +set\ nomodifiable ../../python3_src/seed/for_libs/-py_original-/py3_11_9/importlib/util.py
  \<find_spec\>
      \<_find_spec\>


