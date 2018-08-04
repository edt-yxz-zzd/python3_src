
from nn_ns.parsing.IterParser.LeftScanIterParser import *
from nn_ns.parsing.IterParser.ExprGrammar import *
from nn_ns.parsing.IterParser.IDTypes_and_RuleTypes import *
from sand.types.TesterBase import TesterBase



############################# test #############################


    
class Tester__LeftScanIterParser(TesterBase):
    def __init__(self, abbr_text):
        self.st = toExprSentence(abbr_text)
        TesterBase.__init__(self)
        
        self.p = p = LeftScanIterParser(unbox_id2rule(self.st.input_id2rule),
                                        unbox_id(self.st.main_id))
        self.feeds()

    
            
    def feeds(self):
        p = self.p
        for T in self.st.in_terminals:
            try:
                p.feed(unbox_id(T))
            except:
                print(p.pos)
                print(self.in_terminals[:p.pos])
                print(self.in_abbr_text[:p.pos])
                print(p.shifted_pos2expected_terminals)
                print('\n'*4)
                pprint(p.wanted2wantings)
                print('\n'*4)
                pprint(p.wanting2wanteds)
                print('\n'*4)
                pprint(p.wanted2wanted_instances)
                raise

    def test__to_tree(self):
        p = self.p
        pprint = self.pprint
        
        t = p.to_tree()
        pprint(t)

s = Tester__LeftScanIterParser(expr_sentence_in_abbr_text1)
#s.turn_off_show()
s.test__to_tree()



