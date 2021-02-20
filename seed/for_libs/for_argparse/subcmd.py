
r'''

wrapper for add_subparsers/add_parser/add_argument
#'''


__all__ = '''
    ArgParserPrepare
    GetArgsKwargs
    '''.split()


from seed.helper.get_args_kwargs import GetArgsKwargs, xcall
from argparse import ArgumentParser

class ArgParserPrepare:
    def __init__(sf, parents:'[ArgParserPrepare]', common_options:'[GetArgsKwargs]', subcmds:'{group:{subcmd:ArgParserPrepare}}'):
        self._parents = tuple(parents)
        self._common_options = tuple(common_options)
        self.__subcmds = tuple((group, tuple(d.items())) for group, d in subcmds.items())
    def fill_to(sf, argparser:'ArgumentParser'):
        for parent in sf._parents:
            parent.fill_to(argparser)
        for option in sf._common_options:
            xcall(argparser.add_argument, option)
        for group, subcmd_prepare_pairs in sf.__subcmds:
            #ps = argparser.add_subparsers(group)
            ps = xcall(argparser.add_subparsers, group)
            for subcmd, prepare in subcmd_prepare_pairs:
                #p = ps.add_parser(subcmd)
                p = xcall(ps.add_parser, subcmd)
                prepare.fill_to(p)


