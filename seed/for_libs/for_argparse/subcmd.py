
r'''

wrapper for add_subparsers/add_parser/add_argument


seed.for_libs.for_argparse.subcmd


from seed.for_libs.for_argparse.subcmd import ArgParserPrepare, mk_group_with_dest, Main4subcmd
from seed.helper.get_args_kwargs import mk_GetArgsKwargs as mkG, xcall



used by:
    <phone_txt>/txt/script/欧路词典.py
#'''


__all__ = '''
    Main4subcmd
    ArgParserPrepare
        mk_group
    mk_group_with_dest
        GroupWithDest

    '''.split()


from seed.helper.get_args_kwargs import mk_GetArgsKwargs as mkG, xcall
from argparse import ArgumentParser
from abc import ABC, abstractmethod

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

def mk_group(group_name:str):
    'for ArgParserPrepare::subcmds::group'
    return mkG(title=group_name, dest=group_name)

class GroupWithDest:
    def __init__(sf, dest:str):
        sf.subcmd_dest_name = dest
    def mk1(sf, group_name:str):
        return mkG(title=group_name, dest=sf.subcmd_dest_name)

    def __call__(__sf, **group_name2subcmd2prepare):
        group2subcmd2prepare = {}
        mk1 = __sf.mk1
        for group_name, subcmd2prepare in group_name2subcmd2prepare.items():
            group = mk1(group_name)
            group2subcmd2prepare[group] = subcmd2prepare
        return group2subcmd2prepare
def mk_group_with_dest(__subcmd_dest_name, **group_name2subcmd2prepare):
    group2subcmd2prepare = GroupWithDest(__subcmd_dest_name)(**group_name2subcmd2prepare)
    return group2subcmd2prepare


class Main4subcmd(ABC):
    r'''
usage:
    cls.Get
    cls.Pack
    sf.subcmd_method_fmt
    sf.no_subcmd_method_name
    sf.main(user_args=None)

    #to impl
    def on_subcmd__XXX(sf, subcmd_name, parsed_args):
    def on_no_subcmd(sf, subcmd_name, parsed_args):
    @classmethod
    def _mk_option_config_(cls):
        '-> ([parent::ArgParserPrepare], [common_option::GetArgsKwargs], {group_name:{subcmd:ArgParserPrepare}})'


    #'''

    subcmd_method_fmt = 'on_subcmd__{subcmd_name}'
    no_subcmd_method_name = 'on_no_subcmd'

    def __init__(sf, *, description, epilog='', subcmd_dest_name='_subcmd_'):
        import argparse
        parser = argparse.ArgumentParser(
            description=description
            , epilog=epilog
            , formatter_class=argparse.RawDescriptionHelpFormatter
            )
        cls = type(sf)
        prepare = cls.mk_ArgParserPrepare(subcmd_dest_name)
        prepare.fill_to(parser)


        sf.subcmd_dest_name = subcmd_dest_name
        sf.prepare = prepare
        sf.parser = parser

    def main(sf, user_args=None):
        parsed_args = sf.parser.parse_args(user_args)
        subcmd_dest_name = sf.subcmd_dest_name
        #rint(dir(parsed_args), type(parsed_args))
        #subcmd_name = parsed_args.get(subcmd_dest_name)
        subcmd_name = getattr(parsed_args, subcmd_dest_name)
        if subcmd_name:
            method_name = sf.subcmd_method_fmt.format(subcmd_name=subcmd_name)
        else:
            method_name = sf.no_subcmd_method_name
        method = getattr(sf, method_name)
        return method(subcmd_name, parsed_args)



    @classmethod
    def mk_ArgParserPrepare(cls, subcmd_dest_name):
        (parents, common_options, group_name2subcmd2prepare) = cls._mk_option_config_()
        group2subcmd2prepare = mk_group_with_dest(subcmd_dest_name, **group_name2subcmd2prepare)
        prepare = ArgParserPrepare(parents, common_options, group2subcmd2prepare)
        return prepare



    from seed.for_libs.for_argparse.subcmd import ArgParserPrepare as Pack
    from seed.helper.get_args_kwargs import mk_GetArgsKwargs as Get
    @classmethod
    @abstractmethod
    def _mk_option_config_(cls):
        '-> ([parent::ArgParserPrepare], [common_option::GetArgsKwargs], {group_name:{subcmd:ArgParserPrepare}})'
        Get, Pack = cls.Get, cls.Pack

        options_XXX = (
    [Get('-v', '--method_version', type=int, required=True, choices=(1,2,3), help='XXX method impl version')
    ,Get('-i', '--input', type=str, default=None, help='input file path')
    ,Get('-o', '--output', type=str, default=None, help='output file path')
    ,Get('-e', '--encoding', type=str, default='utf8', help='input/output file encoding')
    ,Get('-f', '--force', action='store_true', default = False, required=False, help='open mode for output file')
        ])
        options_YYY = (
    [
        ])


        prepare_XXX = Pack([], options_XXX, {})
        prepare_YYY = Pack([], options_YYY, {})
        subcmd2prepare_GROUP_A = (dict
            (XXX=prepare_XXX
            ,YYY=prepare_YYY
            ))
        subcmd2prepare_GROUP_B = (dict
            (
            ))
        group_name2subcmd2prepare = (dict
            (GROUP_A=subcmd2prepare_GROUP_A
            ,GROUP_B=subcmd2prepare_GROUP_B
            ))
        return [], [], group_name2subcmd2prepare
        def on_subcmd__XXX(sf, subcmd_name, parsed_args):
            'XXX'
        def on_subcmd__YYY(sf, subcmd_name, parsed_args):
            'YYY'
        def on_no_subcmd(sf, subcmd_name, parsed_args):
            raise NotImplementedError

