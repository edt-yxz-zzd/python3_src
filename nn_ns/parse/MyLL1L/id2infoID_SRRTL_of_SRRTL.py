

from .tools_for_id2infoID_SRRTL import *
from .SRRTL_in_SRRTL import mainID_SRRTL_of_SRRTL

def build_id2infoID_SRRTL_of_SRRTL():
    sls = []
    tls = []
    def adds(ID): sls.append(toState(ID, tls));clrt()
    def addt(a): tls.append(a)
    def clrt():
        nonlocal tls
        tls = []

    addt(toIf(None, InfoGoto('startline')))
    adds(mainID_SRRTL_of_SRRTL)

    addt(toNormal('indent', r'((?!\n)\s)*', [toIf(None, InfoGoto('endline'))]))
    adds('startline')


    addt(toNormal('spaces', r'((?!\n)\s)+'))
    addt(toNormal('newlines', r'\n+', [toIf(None, InfoGoto('startline'))]))
    addt(toNormal('comment', r'#.*'))
    addt(toNormal('string', r"r?'(?!'')([^'\\]|\\.)*'" '|' r'r?"(?!"")([^"\\]|\\.)*"',
                  [toIf(None, InfoError('string follows sth'), r'(?!$|\s)')]))


    addt(toNormal('idstring', r"idr?'(?!'')([^'\\]|\\.)*'" '|' r'idr?"(?!"")([^"\\]|\\.)*"',
                  [toIf(None, InfoError('idstring follows sth'), r'(?!$|\s)')]))

    addt(toNormal('id', '((?!["' "'])\S)+",
                  [toIf(None, InfoError('id follows sth'), r'(?!$|\s)'),
                   toNormal("'='", '=')]))
    adds('endline')


    id2infoStateID = {info.ID : info for info in sls}
    assert len(sls) == len(id2infoStateID)
    del adds, addt, clrt, sls, tls

    return id2infoStateID

id2infoID_SRRTL_of_SRRTL = build_id2infoID_SRRTL_of_SRRTL()

if __name__ == '__main__':
    from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
    from .MyLL1L_in_SRRTL import MyLL1L_in_SRRTL, mainID_SRRTL_of_MyLL1L
    from .SRRTL_in_SRRTL import SRRTL_in_SRRTL, mainID_SRRTL_of_SRRTL

    for xl_in_SRRTL in [MyLL1L_in_SRRTL, MyLL1L_in_SRRTL]:
        r = raw_tokenize_SRRTL(xl_in_SRRTL, mainID_SRRTL_of_SRRTL, id2infoID_SRRTL_of_SRRTL)
        for e in zip(range(4667868), r):
            print(e)

