
from .raw_id2infoID_MyLL1L_of_MyLL1L import build_raw_id2infoID_MyLL1L_of_MyLL1L
from .tools_for_id2infoID_MyLL1L import fill_raw_id2info_MyLL1L

def build_id2infoID_MyLL1L_of_MyLL1L():
    tIDDict, id2info = _build_id2infoID_MyLL1L_of_MyLL1L()
    return id2info

def _build_id2infoID_MyLL1L_of_MyLL1L():
    r = build_raw_id2infoID_MyLL1L_of_MyLL1L()
    tIDDict, id2info = fill_raw_id2info_MyLL1L(r)

    return tIDDict, id2info
    
tIDDict_MyLL1L_of_MyLL1L, id2infoID_MyLL1L_of_MyLL1L = \
                          _build_id2infoID_MyLL1L_of_MyLL1L()
