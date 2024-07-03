r'''[[[

types.DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)¶
Route attribute access on a class to __getattr__.

This is a descriptor, used to define attributes that act differently when accessed through an instance and through a class. Instance access remains normal, but access to an attribute through a class will be routed to the class’s __getattr__ method; this is done by raising AttributeError.

This allows one to have properties active on an instance, and have virtual attributes on the class with the same name (see Enum for an example).

New in version 3.4.

.deleter(self, fdel) -> new_sf
.getter(self, fget) -> new_sf
.setter(self, fset) -> new_sf

#]]]'''#'''
from types import DynamicClassAttribute as class_property


from seed.tiny_.class_property import class_property
from seed.tiny_.class_property import *

