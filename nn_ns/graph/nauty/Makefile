

NAUTY_HOME = D:\software\programming\library\graph\nauty24r2
NAUTY_OBJ_DIR = $(NAUTY_HOME)
NAUTY_SRC_DIR = $(NAUTY_HOME)
NAUTY_INCLUDE_DIR = $(NAUTY_HOME)
CINCLUDE = /I%py_include% /I$(NAUTY_INCLUDE_DIR)
CXXINCLUDE = 
CXX = cl
CXXFLAGS = /EHsc $(CINCLUDE) $(CXXINCLUDE)
C = $(CXX)
CFLAGS = $(CINCLUDE)

LDFLAGS = /MD /link /LIBPATH:%py_lib% /LIBPATH:$(NAUTY_OBJ_DIR)



.SUFFIXES:      .obj .cpp .c
#SOURCES:sh= ls *.cpp
#OBJECTS = $(SOURCES:.cpp=.obj)
OBJECTS = call_cnauty_module.obj nauty.obj nautil.obj naugraph.obj nausparse.obj 
#nauty.c, nautil.c naugraph.c nausparse.c

all: call_cnauty.pyd

call_cnauty.pyd: $(OBJECTS)
	$(CXX) /LD /Fe$@ $(OBJECTS) $(LDFLAGS) 

call_cnauty_module.obj : call_cnauty_module.c
nauty.obj : $(NAUTY_OBJ_DIR)\nauty.c
nautil.obj : $(NAUTY_OBJ_DIR)\nautil.c
naugraph.obj : $(NAUTY_OBJ_DIR)\naugraph.c
nausparse.obj : $(NAUTY_OBJ_DIR)\nausparse.c


#%.obj : %.cpp
.cpp.obj :
	$(CXX) $(CXXFLAGS) /c /Fo$@ $<
.c.obj :
	$(C) $(CFLAGS) /c /Fo$@ $<

clean:
	rm -f *.obj *.pyd *.dll *.exp *.lib *.a *.o *.so
