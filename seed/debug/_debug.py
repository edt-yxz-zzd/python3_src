
r"""

seed.debug._debug
py -m seed.debug._debug
py -m seed.debug._debug > /sdcard/0my_files/tmp/xxx/debug_out.txt
view /sdcard/0my_files/tmp/xxx/debug_out.txt

___begin_mark_of_excluded_global_names__0___ = ...
import ...
___end_mark_of_excluded_global_names__0___ = ...
if __name__ == '__main__':
    #???put anywhere, neednot at eof
        #put anywhere to detect unbound_names, neednot at eof
        ##but SHOULD-BE put eof to print globals
        #now try to guess module qname.for __main__
    from seed.debug._debug import main__print_infos_of_modules as _main
    _main([__name__])


e ../../python3_src/seed/debug/_debug.py

original from:
    nn_ns.filedir.backup_tools._debug

#"""


__all__ = '''
    main__print_infos_of_modules
        print_unbound_names_of_modules
        print_global_names_of_modules
        print_toplevel_def_heads_of_modules

    '''.split()








r"""
py -m nn_ns.filedir.backup_tools._debug



#jump

__all__ = '''

    '''.split()


___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

# exec these two cmds in vim
%s/\(def [^/*]\+[^/*(]\)\(\(,\s\+[*].*\)\?[)]:\)$/\1, \/\2/g
%s/\(def [^/*]\+[/],\)\s\+\([*],.*[)]:\)$/\1\2/g
    from:
        def xxx(...):
        def xxx(..., *, ...):
        def xxx(..., *args, ...):
        def xxx(..., **kwargs):
    to mk:
        def xxx(..., /):
        def xxx(..., /,*...):
        def xxx(..., /, *args, ...):
        def xxx(..., /, **kwargs):
    avoid:
        def xxx():
        def xxx(*...):
            def xxx(*, ...):
            def xxx(*args, ...):
            def xxx(**kwargs, ...):
        def xxx(..., /...):
            def xxx(..., /):
            def xxx(..., /,*...):
                def xxx(..., /, *, ...):
                def xxx(..., /, *args, ...):
                def xxx(..., /, **kwargs, ...):

print_global_names _ex
    +___begin_mark_pattern_of_excluded_global_names___
    +___end_mark_pattern_of_excluded_global_names___
    +with_prefix_coomma



buttom -> bottom
virtul -> virtual

#"""







if __name__ == '__main__':
    qnames_in_lines = '''
        seed.ops.IOps4OneMainObjType
    '''
    #jump
    '''


        '''
    qnames = qnames_in_lines.split()
    del qnames_in_lines

def print_unbound_names_of_modules(qnames):
    excludes = '''
        logic err
        '''.split()
    from seed.pkg_tools.dectect_all_unbound_names import DectectAllUnboundNames


    excludes = frozenset(excludes)
    for __name__ in qnames:
        print(f'module: {__name__}: unbound_name@space_lineno_list')
        unbound_name2space_lineno_list = forgots = (DectectAllUnboundNames.from_module_qname(__name__))
        #print(unbound_name2space_lineno_list)
        for unbound_name, space_lineno_list in unbound_name2space_lineno_list.items():
            if unbound_name not in excludes:
                print(f'    {unbound_name!s}@{space_lineno_list}')

def _f2(qnames):
    from seed.helper.print_global_names import print_global_names
    import importlib

    for __name__ in qnames:
        print(f'module: {__name__}: globals')
        module = importlib.import_module(__name__)
        print_global_names(module.__dict__)
        print(bar)


def print_global_names_of_modules(qnames):
    from seed.helper.print_global_names import print_global_names_ex
    import importlib
    from pathlib import Path

    def f(__name__):
        if __name__ == '__main__':
            module = importlib.import_module(__name__)
            m = module.__package__
            if not m:
                #script???
                pass
            else:
                pkg = m
                fname = Path(module.__file__)
                qname = f'{pkg!s}.{fname.stem!s}'
                g(qname)
        else:
            pass
        g(__name__)

    def g(__name__):
        print(f'module: {__name__}: globals')
        module = importlib.import_module(__name__)
        print_global_names_ex(module.__dict__,  prefix=' '*4, ___begin_mark_pattern_of_excluded_global_names___=r'___begin_mark_of_excluded_global_names__\d+___', ___end_mark_pattern_of_excluded_global_names___=r'___end_mark_of_excluded_global_names__\d+___')
        print(bar)
    for __name__ in qnames:
        f(__name__)



def print_toplevel_def_heads_of_modules(qnames):
    from seed.helper.print_global_names import print_global_names_ex
    import importlib
    import ast

    for __name__ in qnames:
        print(f'module: {__name__}: global def heads')
        module = importlib.import_module(__name__)
        fname = module.__file__
        with open(fname, 'rt', encoding='utf8') as fin:
            src = fin.read()
        lines = src.split('\n')
            #used in handle__basic
        module_node = ast.parse(src)
        recur_names = ('''
                For
                AsyncFor
                While
                If
                With
                AsyncWith
                Try
                '''.split())
        basic_names = ('''
                FunctionDef
                AsyncFunctionDef
                ClassDef
                Assign
                AnnAssign
                '''.split())
        def handle__basic(basic_top_stmt_node):
            node = basic_top_stmt_node
            i = node.lineno
            i -= 1
            print(f'    {lines[i]!s}')
        def handles(top_stmt_nodes):
            for top_stmt_node in top_stmt_nodes:
                handle(top_stmt_node)
        def handle(top_stmt_node):
            cls = type(top_stmt_node)
            if cls.__name__ in basic_names:
                handle__basic(top_stmt_node)

            elif cls.__name__ in recur_names:
                attrs = 'body handlers orelse finalbody'
                attrs4stmts = 'body orelse finalbody'
                #...recur visit body else...
                #| Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
                #excepthandler = ExceptHandler(expr? type, identifier? name, stmt* body)
                #                attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)
                for attr in attrs4stmts:
                    stmts = getattr(top_stmt_node, attr, ())
                    #recur
                    handles(stmts)
                handlers = getattr(top_stmt_node, 'handlers', ())
                for excepthandler in handlers:
                    #handle__excepthandler(excepthandler)
                    handles(excepthandler.body)
        #end of def handle(top_stmt_node):
        handles(module_node.body)
            #main call

        r'''

    mod = Module(stmt* body, type_ignore *type_ignores)

    stmt = FunctionDef(identifier name, arguments args,
                       stmt* body, expr* decorator_list, expr? returns,
                       string? type_comment)
          | AsyncFunctionDef(identifier name, arguments args,
                             stmt* body, expr* decorator_list, expr? returns,
                             string? type_comment)

          | ClassDef(identifier name,
             expr* bases,
             keyword* keywords,
             stmt* body,
             expr* decorator_list)

          | Assign(expr* targets, expr value, string? type_comment)
          -- 'simple' indicates that we annotate simple name without parens
          | AnnAssign(expr target, expr annotation, expr? value, int simple)

          -- use 'orelse' because else is a keyword in target languages
          | For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
          | AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
          | While(expr test, stmt* body, stmt* orelse)
          | If(expr test, stmt* body, stmt* orelse)
          | With(withitem* items, stmt* body, string? type_comment)
          | AsyncWith(withitem* items, stmt* body, string? type_comment)

          | Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)

    excepthandler = ExceptHandler(expr? type, identifier? name, stmt* body)
                    attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)
          #'''
        #for line in lines:
        print(bar)


if __name__ == '__main__':
    ___end_mark_pattern_of_excluded_global_names__9999___ = ...

bar = '='*22
def main__print_infos_of_modules(qnames):
    print_unbound_names_of_modules(qnames)
    print(bar); print(bar); print(bar)
    print_global_names_of_modules(qnames)
    print(bar); print(bar); print(bar)
    print_toplevel_def_heads_of_modules(qnames)
    print(bar); print(bar); print(bar)
    print_unbound_names_of_modules(qnames)
if __name__ == '__main__':
    main__print_infos_of_modules(qnames)


