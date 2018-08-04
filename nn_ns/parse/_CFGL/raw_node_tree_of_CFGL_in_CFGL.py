
cfgl_rnode_tree_of_xtokenized_style_CFGL = \
    [   (   'list',
            'free_style_CFGL',
            [('lchild', ('top_def',), (1, None), None, [])]),
        (   'filter',
            'top_def',
            [   (   'list',
                    'group_def',
                    [('lchild', ('group_def',), (1, 1), None, [])]),
                (   'list',
                    'filter_def',
                    [('lchild', ('filter_def',), (1, 1), None, [])]),
                (   'list',
                    'list_def',
                    [('lchild', ('list_def',), (1, 1), None, [])]),
                (   'list',
                    'token_def',
                    [('lchild', ('token_def',), (1, 1), None, [])])]),
        (   'list',
            'ref_id;',
            [   ('lchild', ('ref_id',), (1, 1), None, []),
                ('lchild', ("';'",), (1, 1), None, [])]),
        (   'list',
            'fchild_def;',
            [   ('lchild', ('fchild_def',), (1, 1), None, []),
                ('lchild', ("';'",), (1, 1), None, [])]),
        (   'list',
            'list_id=',
            [   ('lchild', ('list_id',), (1, 1), None, []),
                ('lchild', ("'='",), (1, 1), None, [])]),
        (   'list',
            'flist_id=',
            [   ('lchild', ('flist_id',), (1, 1), None, []),
                ('lchild', ("'='",), (1, 1), None, [])]),
        (   'list',
            'group_def',
            [   ('lchild', ('group_id',), (1, 1), None, []),
                ('lchild', ("':'",), (1, 1), None, []),
                ('lchild', ("'{'",), (1, 1), None, []),
                ('lchild', ('ref_id;',), (1, None), None, []),
                ('lchild', ("'}'",), (1, 1), None, [])]),
        (   'list',
            'filter_def',
            [   ('lchild', ('filter_id',), (1, 1), None, []),
                ('lchild', ("'{'",), (1, 1), None, []),
                ('lchild', ('fchild_def;',), (1, None), None, []),
                ('lchild', ("'}'",), (1, 1), None, [])]),
        (   'list',
            'list_def',
            [   ('lchild', ('list_id=',), (1, None), None, []),
                ('lchild', ('lchild_def',), (0, None), None, []),
                ('lchild', ("';'",), (1, 1), None, [])]),
        (   'list',
            'token_def',
            [   ('lchild', ('token_id',), (1, 1), None, []),
                ('lchild', ("'is'",), (1, 1), None, []),
                ('lchild', ('token_name',), (1, 1), None, []),
                ('lchild', ("';'",), (1, 1), None, [])]),
        ('list', 'token_name', [('lchild', ('tag',), (1, 1), None, [])]),
        (   'filter',
            'fchild_def',
            [   (   'list',
                    'ffilter_def',
                    [   ('lchild', ('ffilter_id',), (1, 1), None, []),
                        ('lchild', ("'{'",), (1, 1), None, []),
                        ('lchild', ('fchild_def;',), (1, None), None, []),
                        ('lchild', ("'}'",), (1, 1), None, [])]),
                (   'list',
                    'flist_def',
                    [   ('lchild', ('flist_id=',), (1, 1), None, []),
                        ('lchild', ('lchild_def',), (0, None), None, []),
                        ('lchild', ("';'",), (1, 1), None, [])]),
                (   'list',
                    'fref_def',
                    [   ('lchild', ('top_id',), (1, 1), None, []),
                        ('lchild', ("';'",), (1, 1), None, [])])]),
        (   'list',
            'lchild_def',
            [   ('lchild', ('argname_endflag',), (0, 1), None, []),
                ('lchild', ('ref_id',), (1, 1), None, []),
                ('lchild', ('count',), (0, 1), None, []),
                ('lchild', ('tag',), (0, None), None, [])]),
        (   'list',
            'argname_endflag',
            [   ('lchild', ('argname',), (1, 1), None, []),
                ('lchild', ('endflag',), (1, 1), None, [])]),
        (   'filter',
            'endflag',
            [   (   'list',
                    'endflag_yes',
                    [('lchild', ("':'",), (1, 1), None, [])]),
                (   'list',
                    'endflag_no',
                    [('lchild', ("':-'",), (1, 1), None, [])])]),
        (   'filter',
            'ref_id',
            [   ('list', 'top_id', [('lchild', ('top_id',), (1, 1), None, [])]),
                (   'list',
                    'ffilter_ref_id',
                    [('lchild', ('ffilter_ref_id',), (1, 1), None, [])])]),
        (   'list',
            'ffilter_ref_id',
            [   ('lchild', ('filter_id',), (1, 1), None, []),
                ('lchild', ('.ffilter_id',), (1, None), None, [])]),
        (   'list',
            '.ffilter_id',
            [   ('lchild', ("'.'",), (1, 1), None, []),
                ('lchild', ('ffilter_id',), (1, 1), None, [])]),
        (   'filter',
            'top_id',
            [   (   'list',
                    'group_id',
                    [('lchild', ('group_id',), (1, 1), None, [])]),
                (   'list',
                    'filter_id',
                    [('lchild', ('filter_id',), (1, 1), None, [])]),
                (   'list',
                    'list_id',
                    [('lchild', ('list_id',), (1, 1), None, [])]),
                (   'list',
                    'token_id',
                    [('lchild', ('token_id',), (1, 1), None, [])])]),
        ('list', 'group_id', [('lchild', ('id',), (1, 1), None, [])]),
        ('list', 'filter_id', [('lchild', ('id',), (1, 1), None, [])]),
        ('list', 'list_id', [('lchild', ('id',), (1, 1), None, [])]),
        ('list', 'token_id', [('lchild', ('id',), (1, 1), None, [])]),
        ('list', 'ffilter_id', [('lchild', ('id',), (1, 1), None, [])]),
        ('list', 'flist_id', [('lchild', ('id',), (1, 1), None, [])]),
        ('list', 'argname', [('lchild', ('id',), (1, 1), None, [])]),
        (   'filter',
            'count',
            [   ('list', 'star', [('lchild', ('star',), (1, 1), None, [])]),
                ('list', 'plus', [('lchild', ('plus',), (1, 1), None, [])]),
                (   'list',
                    'optional',
                    [('lchild', ('optional',), (1, 1), None, [])]),
                ('list', 'star?', [('lchild', ('star?',), (1, 1), None, [])]),
                ('list', 'plus?', [('lchild', ('plus?',), (1, 1), None, [])]),
                (   'list',
                    'optional?',
                    [('lchild', ('optional?',), (1, 1), None, [])]),
                (   'list',
                    'min_max',
                    [   ('lchild', ("'{{'",), (1, 1), None, []),
                        ('lchild', ('min',), (1, 1), None, []),
                        ('lchild', ("':'",), (1, 1), None, []),
                        ('lchild', ('max',), (1, 1), None, []),
                        ('lchild', ("'}}'",), (1, 1), None, [])]),
                (   'list',
                    'len',
                    [   ('lchild', ("'[['",), (1, 1), None, []),
                        ('lchild', ('len',), (1, 1), None, []),
                        ('lchild', ("']]'",), (1, 1), None, [])])]),
        ('list', "'{{'", [('lchild', ("'{'",), (1, 1), None, [])]),
        ('list', "'}}'", [('lchild', ("'}'",), (1, 1), None, [])]),
        ('list', 'min', [('lchild', ('int',), (1, 1), None, [])]),
        ('list', 'max', [('lchild', ('int',), (1, 1), None, [])]),
        ('list', 'len', [('lchild', ('int',), (1, 1), None, [])]),
        ('token', 'id', 'w'),
        ('token', 'int', 'w'),
        ('token', 'tag', '#'),
        ('token', 'star', '*'),
        ('token', 'plus', '+'),
        ('token', 'optional', '?'),
        ('token', 'star?', '*?'),
        ('token', 'plus?', '+?'),
        ('token', 'optional?', '??'),
        ('token', "'is'", 'is'),
        ('token', "'='", '='),
        ('token', "'{'", '{'),
        ('token', "'}'", '}'),
        ('token', "'[['", '['),
        ('token', "']]'", ']'),
        ('token', "';'", ';'),
        ('token', "':'", ':'),
        ('token', "'.'", '.'),
        ('token', "':-'", ':-')]

