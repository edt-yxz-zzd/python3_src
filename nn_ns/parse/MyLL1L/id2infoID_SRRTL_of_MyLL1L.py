

from .tools_for_id2infoID_SRRTL import *
from .MyLL1L_in_SRRTL import mainID_SRRTL_of_MyLL1L

def build_id2infoID_SRRTL_of_MyLL1L():
    sls = []
    tls = []
    def adds(ID): sls.append(toState(ID, tls));clrt()
    def addt(a): tls.append(a)
    def clrt():
        nonlocal tls
        tls = []

    addt(toIf(None, InfoGoto('startline')))
    adds(mainID_SRRTL_of_MyLL1L)

    addt(toNormal('indent', r'((?!\n)\s)*', [toIf(None, InfoGoto('endline'))]))
    adds('startline')

    addt(toNormal('string', r"'(?!'')([^'\\]|\\.)*'"))
    addt(toNormal('string', r'"(?!"")([^"\\]|\\.)*"'))
    addt(toNormal('string', "\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''"))
    addt(toNormal('string', '\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""'))

    addt(toNormal('comment', r'#.*'))
    addt(toNormal('newlines', r'\n+', [toIf(None, InfoGoto('startline'))]))
    addt(toNormal('spacesButNewline', r'((?!\n)\s)+'))
    addt(toNormal('block', '((?![\'"#])\\S)+'))

    adds('endline')


    id2infoStateID = {info.ID : info for info in sls}
    assert len(sls) == len(id2infoStateID)
    del adds, addt, clrt, sls, tls

    return id2infoStateID

id2infoID_SRRTL_of_MyLL1L = build_id2infoID_SRRTL_of_MyLL1L()

if __name__ == '__main__':
    from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
    from .MyLL1L_in_MyLL1L import MyLL1L_in_MyLL1L, mainID_MyLL1L_of_MyLL1L
    from .SRRTL_in_MyLL1L import SRRTL_in_MyLL1L, mainID_MyLL1L_of_SRRTL
    from .MyLL1L_in_SRRTL import mainID_SRRTL_of_MyLL1L


    for xl_in_MyLL1L in [MyLL1L_in_MyLL1L, SRRTL_in_MyLL1L]:
        r = raw_tokenize_SRRTL(xl_in_MyLL1L, mainID_SRRTL_of_MyLL1L, id2infoID_SRRTL_of_MyLL1L)
        for e in zip(range(4667868), r):
            print(e)







            
