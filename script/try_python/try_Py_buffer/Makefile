

PRJ_HOME = .
OBJ_DIR = $(PRJ_HOME)
SRC_DIR = $(PRJ_HOME)
INCLUDE_DIR = $(PRJ_HOME)
CINCLUDE = /I%py_include% /I$(INCLUDE_DIR)
CXXINCLUDE = 
CXX = cl
CXXFLAGS = /EHsc $(CINCLUDE) $(CXXINCLUDE)
C = $(CXX)
CFLAGS = $(CINCLUDE)

LDFLAGS = /MD /link /LIBPATH:%py_lib% /LIBPATH:$(OBJ_DIR)



.SUFFIXES:      .obj .cpp .c
#SOURCES:sh= ls *.cpp
#OBJECTS = $(SOURCES:.cpp=.obj)
OBJECTS = _try_buffer_mod.obj

all: _try_buffer.pyd
    rem mv _try_buffer.pyd ./sfsf.pyd

_try_buffer.pyd: $(OBJECTS)
	$(CXX) /LD /Fe$@ $(OBJECTS) $(LDFLAGS) 

_try_buffer_mod.obj : _try_buffer_mod.cpp



#%.obj : %.cpp
.cpp.obj :
	$(CXX) $(CXXFLAGS) /c /Fo$@ $<
.c.obj :
	$(C) $(CFLAGS) /c /Fo$@ $<

clean:
	rm -f *.obj *.pyd *.dll *.exp *.lib *.a *.o *.so
