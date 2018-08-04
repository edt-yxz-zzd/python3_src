from . import sibling
#print(sibling.__file__)
print(__name__)
print(__import__(__name__))
print(__import__('importlib').import_module(__name__))
