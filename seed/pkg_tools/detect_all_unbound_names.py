
r'''
pym detect_all_unbound_names.py -i detect_all_unbound_names.py -x a -x logic
#'''

__all__ = '''
    DetectAllUnboundNames
    main
    '''.split()



from .module_qname2source_file_path import module_qname2source_file_path
from .read_python_source import read_python_source
from ._forgot_import import symtable2forgots
import ast
from pathlib import Path

import symtable
r'''
class CollectAllUnboundNamesVisitor(ast.NodeVisitor):
class PrintNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.unbound_names = set()
        self.indents = ['']
    def push(self):
        indent = self.indents[-1] + ' '*4
        self.indents.append(indent)
    def pop(self):
        self.indents.pop()
    def generic_visit(self, node):
        for fieldname, value in ast.iter_fields(node):
            print(f'{fieldname}{self.indents[-1]}{value!r}')
            if value is None:
                pass
            elif type(value) is list:
                ast_nodes = value
                self.push()
                for ast_node in ast_nodes:
                    self.visit(ast_node)
                self.pop()
            elif isinstance(value, ast.AST):
                ast_node = value
                self.push()
                self.visit(ast_node)
                self.pop()
            elif type(value) in (int, str, bool):
                pass
            else:
                raise logic-error
#'''


class DetectAllUnboundNames:
    @classmethod
    def from_module_qname(cls, module_qname):
        source_path = module_qname2source_file_path(module_qname)
        return cls.from_source_path(source_path)
    @classmethod
    def from_source_path(cls, source_path):
        #bs = Path(source_path).read_bytes()
        python_source = read_python_source(source_path)
        return cls.from_python_source(python_source, source_path)
    @classmethod
    def from_python_source(cls, python_source, filename):
        # python_source :: str|bytes
        table = symtable.symtable(python_source, filename, 'exec')
        return symtable2forgots(table, ())
        ast_tree = ast.parse(python_source)
        return cls.from_ast_node(ast_tree, filename)
    @classmethod
    def from_ast_node(cls, ast_node, filename):
        # ast_node -> {name}
        raise NotImplementedError
        table = symtable.symtable(ast_node, filename, 'exec')
        return symtable2forgots(table, ())

        c = CollectAllUnboundNamesVisitor()
        c.visit(ast_node)
        return c.unbound_names

def _t():
    def f():
        lambda : a
    r = DetectAllUnboundNames.from_module_qname(__name__)
    print(r)
    {'a': [80], 'CollectAllUnboundNamesVisitor': [67]}


def main(args=None):
    r'''
--module xxx.yyy.zzz
--input_path path/to/zzz.py
--excludes logic
--excludes error
'''
    import argparse
    parser = argparse.ArgumentParser(description='DetectAllUnboundNames')
    parser.add_argument('-x', '--excludes', type=str
                        ,action='append', default=[]
                        ,help='exclude from the result unbound_names'
                        )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--module', type=str
                        ,default=None
                        ,help='module fullname; qualified name; x.y.z'
                        )
    group.add_argument('-i', '--input_path', type=str
                        ,default=None
                        ,help='path to python script'
                        )

    args = parser.parse_args(args)
    if args.module is not None:
        r = DetectAllUnboundNames.from_module_qname(args.module)
    elif args.input_path is not None:
        r = DetectAllUnboundNames.from_source_path(args.input_path)
    else:
        raise logic-error
    unbound_names = forgots = r
    unbound_names = set(unbound_names) - set(args.excludes)
    unbound_names = sorted(unbound_names)
    for unbound_name in unbound_names:
        print(unbound_name)

if __name__ == "__main__":
    #_t()
    main()


