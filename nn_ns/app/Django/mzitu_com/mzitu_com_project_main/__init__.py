
import sys
import pathlib
parent_path = pathlib.Path(__file__).parent
parent_str = str(parent_path)

#bug: sys.path.insert(0, parent_path)
sys.path.insert(0, parent_str)
#print(sys.path)

