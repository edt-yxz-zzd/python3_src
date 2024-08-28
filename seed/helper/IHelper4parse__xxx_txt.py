r'''
e ../../python3_src/seed/helper/IHelper4parse__xxx_txt.py

seed.helper.IHelper4parse__xxx_txt
py -m nn_ns.app.debug_cmd   seed.helper.IHelper4parse__xxx_txt
py -m seed.helper.IHelper4parse__xxx_txt

from seed.helper.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt

view ../../python3_src/seed/helper/IConfig4load_versioned_repr_txt_file.py


[[moved:
======================
======================
mv ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/IHelper4parse__xxx_txt.py  ../../python3_src/seed/helper/
======================
======================
nn_ns.CJK.unicode.ucd_unihan.ucd.IHelper4parse__xxx_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.IHelper4parse__xxx_txt
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.IHelper4parse__xxx_txt

from nn_ns.CJK.unicode.ucd_unihan.ucd.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt


e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/IHelper4parse__xxx_txt.py
]]

used by:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__Blocks_txt.py
        view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__Blocks_txt.py


======================
.dataobj
    :: (parsed_result, extra_derived_result)
.state
    = compact_result
    mutable
        #maybe immutable
        #hidden from user

======================

#'''

__all__ = ['IHelper4parse__xxx_txt']

from abc import ABC, abstractmethod
from seed.tiny import print_err, echo


class IHelper4parse__xxx_txt(ABC):
    r'''
main methods:
    .parse__fin
        #parse__ifile
    .state2dataobj___create
    .state5dataobj___save


===
===
===
ifile
    -> parsed_result
        -> extra_derived_result
            <-> readonly__extra_derived_result
        <-> readonly__parsed_result
        <-> compact_result
            <-> state
        :::
        <-> dataobj
            <-> readonly__dataobj

<<==:
[state == compact_result]
[dataobj == (parsed_result, extra_derived_result)]
[readonly__dataobj == (readonly__parsed_result, readonly__extra_derived_result)]
==>>:

!:ifile -> parsed_result
!:parsed_result <-> compact_result
!:parsed_result -> extra_derived_result
!:parsed_result <-> readonly__parsed_result
!:extra_derived_result <-> readonly__extra_derived_result
==>>:

parsed_result <-> dataobj
    !! [dataobj == (parsed_result, extra_derived_result)]
    !:parsed_result -> extra_derived_result


compact_result <-> dataobj
    !:parsed_result <-> compact_result
    parsed_result <-> dataobj

compact_result <-> state
    !! [state == compact_result]
    echo

state <-> dataobj
    compact_result <-> state
    compact_result <-> dataobj

dataobj <-> readonly__dataobj
    !! [dataobj == (parsed_result, extra_derived_result)]
    !! [readonly__dataobj == (readonly__parsed_result, readonly__extra_derived_result)]
    !:parsed_result <-> readonly__parsed_result
    !:extra_derived_result <-> readonly__extra_derived_result


<<==:
`parse__fin
    ifile -> parsed_result

state2dataobj___create
state5dataobj___save
    state <-> dataobj

compact_result2state
compact_result5state
    compact_result <-> state

compact_result2dataobj
compact_result5dataobj
    compact_result <-> dataobj

parsed_result2dataobj
parsed_result5dataobj
    parsed_result <-> dataobj

`parsed_result2extra
    parsed_result -> extra_derived_result

`parsed_result2compact
`parsed_result5compact
    parsed_result <-> compact_result

`parsed_result2readonly
`parsed_result5readonly
    parsed_result <-> readonly__parsed_result

`extra_derived_result2readonly
`extra_derived_result5readonly
    extra_derived_result <-> readonly__extra_derived_result

dataobj2readonly
dataobj5readonly
    dataobj <-> readonly__dataobj

    #'''
    #grep 'def [^_]' ../../python3_src/seed/helper/IHelper4parse__xxx_txt.py


    @abstractmethod
    def _parse__fin_(sf, fin, /):
        '-> parsed_result'
    #def parse__lines(sf, lines, /):
    @abstractmethod
    def _parsed_result2extra_(sf, parsed_result, /):
        'parsed_result -> extra_derived_result #not bijection'
    @abstractmethod
    def _parsed_result5compact_(sf, compact_result, /):
        'compact_result -> parsed_result'
    @abstractmethod
    def _parsed_result2compact_(sf, parsed_result, /):
        'parsed_result -> compact_result'

    if 1:
        _parsed_result__is__readonly_ = False
        _extra_derived_result__is__readonly_ = False
        def _parsed_result2readonly_(sf, parsed_result, /):
            'parsed_result -> readonly__parsed_result'
            raise NotImplementedError
        def _parsed_result5readonly_(sf, readonly__parsed_result, /):
            'readonly__parsed_result -> parsed_result'
            raise NotImplementedError
        def _extra_derived_result2readonly_(sf, extra_derived_result, /):
            'extra_derived_result -> readonly__extra_derived_result'
            raise NotImplementedError
        def _extra_derived_result5readonly_(sf, readonly__extra_derived_result, /):
            'readonly__extra_derived_result -> extra_derived_result'
            raise NotImplementedError














    def parse__fin(sf, fin, /):
        parsed_result = sf._parse__fin_(fin)
        return parsed_result
    def state2dataobj___create(sf, state, /):
        compact_result = sf.compact_result5state(state)
        dataobj = sf.compact_result2dataobj(compact_result)
        return dataobj
    def state5dataobj___save(sf, dataobj, /):
        compact_result = sf.compact_result5dataobj(dataobj)
        state = sf.compact_result2state(compact_result)
        return state

    def compact_result2state(sf, compact_result, /):
        state = compact_result
        return state
    def compact_result5state(sf, state, /):
        compact_result = state
        return compact_result

    def compact_result2dataobj(sf, compact_result, /):
        parsed_result = sf.parsed_result5compact(compact_result)
        dataobj = sf.parsed_result2dataobj(parsed_result)
        return dataobj
    def compact_result5dataobj(sf, dataobj, /):
        parsed_result = sf.parsed_result5dataobj(dataobj)
        compact_result = sf.parsed_result2compact(parsed_result)
        return compact_result

    def parsed_result5dataobj(sf, dataobj, /):
        (parsed_result, extra_derived_result) = dataobj
        return parsed_result

    def parsed_result2dataobj(sf, parsed_result, /):
        extra_derived_result = sf.parsed_result2extra(parsed_result)
        dataobj = (parsed_result, extra_derived_result)
        return dataobj


    def parsed_result2extra(sf, parsed_result, /):
        extra_derived_result = sf._parsed_result2extra_(parsed_result)
        return extra_derived_result




    def parsed_result2compact(sf, parsed_result, /):
        #parsed_result5compact
        compact_result = sf._parsed_result2compact_(parsed_result)

        _parsed_result = sf._parsed_result5compact_(compact_result)
        try:
            if not _parsed_result == parsed_result:raise logic-err
        except NameError:
            if not type(_parsed_result) is type(parsed_result):
                print_err(type(parsed_result))
                print_err(type(_parsed_result))
                raise TypeError(f'not type(_parsed_result) is type(parsed_result): not {type(_parsed_result)!r} is {type(parsed_result)!r}')
            raise Exception(f'logic-err:\n\n;parsed_result={parsed_result!r}\n\n;compact_result={compact_result!r}\n\n;sf._parsed_result5compact_(compact_result)={_parsed_result!r}')
        return compact_result



    def parsed_result5compact(sf, compact_result, /):
        #parsed_result2compact
        parsed_result = sf._parsed_result5compact_(compact_result)
        return parsed_result


    def parsed_result2readonly(sf, parsed_result, /):
        if sf._parsed_result__is__readonly_:
            f = echo
        else:
            f = sf._parsed_result2readonly_

        readonly__parsed_result = f(parsed_result)
        return readonly__parsed_result
    def parsed_result5readonly(sf, readonly__parsed_result, /):
        if sf._parsed_result__is__readonly_:
            f = echo
        else:
            f = sf._parsed_result5readonly_

        parsed_result = f(readonly__parsed_result)
        return parsed_result



    def extra_derived_result2readonly(sf, extra_derived_result, /):
        if sf._extra_derived_result__is__readonly_:
            f = echo
        else:
            f = sf._extra_derived_result2readonly_

        readonly__extra_derived_result = f(extra_derived_result)
        return readonly__extra_derived_result
    def extra_derived_result5readonly(sf, readonly__extra_derived_result, /):
        if sf._extra_derived_result__is__readonly_:
            f = echo
        else:
            f = sf._extra_derived_result5readonly_

        extra_derived_result = f(readonly__extra_derived_result)
        return extra_derived_result




    def dataobj2readonly(sf, dataobj, /):
        (parsed_result, extra_derived_result) = dataobj
        readonly__parsed_result = sf.parsed_result2readonly(parsed_result)
        readonly__extra_derived_result = sf.extra_derived_result2readonly(extra_derived_result)
        readonly__dataobj = (readonly__parsed_result, readonly__extra_derived_result)
        return readonly__dataobj
    def dataobj5readonly(sf, readonly__dataobj, /):
        (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj
        parsed_result = sf.parsed_result5readonly(readonly__parsed_result)
        extra_derived_result = sf.extra_derived_result5readonly(readonly__extra_derived_result)
        dataobj = (parsed_result, extra_derived_result)
        return dataobj












from seed.helper.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt
