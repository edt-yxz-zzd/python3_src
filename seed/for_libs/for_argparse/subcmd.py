
r'''

wrapper for add_subparsers/add_parser/add_argument


from seed.for_libs.for_argparse.subcmd import ArgParserPrepare, mk_group
from seed.helper.get_args_kwargs import mk_GetArgsKwargs, xcall
#'''


__all__ = '''
    ArgParserPrepare
    mk_group
    '''.split()


from seed.helper.get_args_kwargs import GetArgsKwargs, xcall
from argparse import ArgumentParser

class ArgParserPrepare:
    def __init__(sf
            , parents:'[ArgParserPrepare]'
            , common_options:'[GetArgsKwargs]'
            #, subcmd_dest:str #group=title=dest
            , subcmds:'{group:{subcmd:ArgParserPrepare}}'
            ):
        sf._parents = tuple(parents)
        sf._common_options = tuple(common_options)
        sf.__subcmds = tuple((group, tuple(d.items())) for group, d in subcmds.items())
        return
        assert type(subcmd_dest) is str
        if not subcmd_dest:
            may_subcmd_dest = None
        else:
            may_subcmd_dest = subcmd_dest
        sf._may_subcmd_dest = may_subcmd_dest
    def fill_to(sf, argparser:'ArgumentParser'):
        for parent in sf._parents:
            parent.fill_to(argparser)
        for option in sf._common_options:
            xcall(argparser.add_argument, option)
        for group, subcmd_prepare_pairs in sf.__subcmds:
            #ps = argparser.add_subparsers(group)
            ps = xcall(argparser.add_subparsers, group, kwarg='dest')
            for subcmd, prepare in subcmd_prepare_pairs:
                #p = ps.add_parser(subcmd)
                p = xcall(ps.add_parser, subcmd)
                prepare.fill_to(p)

def mk_group(group:str):
    'for ArgParserPrepare::subcmds::group'
    return GetArgsKwargs(title=group, dest=group)




