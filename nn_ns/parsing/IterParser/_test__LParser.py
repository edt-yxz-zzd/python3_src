
from nn_ns.parsing.IterParser.LParser import *
from nn_ns.parsing.IterParser.ExprGrammar import *
from nn_ns.parsing.IterParser.IDTypes_and_RuleTypes import *
from sand.types.TesterBase import TesterBase



############################# test #############################


p = LParser(input_id2rule, Expr)
#print(p.wanted2wantings)
#print(input_id2rule)

assert p.calc__expected_terminals() == {val, lbr, space}

# p.feed(star)
# ParseError: expects: {InputID('valuable'), InputID('(')}

p.feed(val)
assert p.calc__expected_terminals() == {star, plus, space}

if False:
    from pprint import pprint
    pprint(p.wanted2wantings)

    
class Tester__LParser(TesterBase):
    def __init__(self, abbr_text):
        self.st = toExprSentence(abbr_text)
        TesterBase.__init__(self)
        
        self.p = p = LParser(self.st.input_id2rule, self.st.main_id)
        self.feeds()
        self.d = p.calc__child_wanted2prev_instances()
    
            
    def feeds(self):
        p = self.p
        for T in self.st.in_terminals:
            try:
                p.feed(T)
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

    def show_main_instances(self):
        p = self.p
        pprint = self.pprint
        pprint(p.wanted2wanted_instances[p.main_wanted])
    def test__alt_instance2all_instance_alts(self):
        p = self.p
        print = self.print
                       
        alt_instance = OutputID(p.main_wanted, len(self.st.in_abbr_text))
        it = p.alt_instance2all_instance_alts(alt_instance)
        for t in it:
            print(t)

    def test__con_instance2all_children_instances_alts(self):
        p = self.p
        d = self.d
        print = self.print
        
        con_instance = OutputID(WantedID(OrgID(AddExpr), 0), len(self.st.in_abbr_text))
        it = p.con_instance2all_children_instances_alts(con_instance, d)
        for t in it:
            print(t)
            print(p.all_children_instances_alt2super_id(t))
    def test__build_output_grammar_rooted_by(self):
        p = self.p
        d = self.d
        print = self.print
        
        main = p.make_main_super_id()
        g = p.build_output_grammar_rooted_by(main, d)
        print(g)

    def test__build_output_grammar_end_at(self):
        p = self.p
        pprint = self.pprint
        
        g = p.build_output_grammar_end_at()
        fg = p.flatten_output_grammar(g)
        pprint(fg)
    def test__is_WantedID_to_ConChildRule(self):
        p = self.p
        wanted = WantedID(ConChildID(InputID('AddExpr'), 3), len(self.st.in_abbr_text))
        assert p.is_WantedID_to_ConChildRule(wanted)

        assert p.wanted2wanted_instances[wanted]
        #print(p.wanted2wanted_instances[wanted])

        assert wanted in map((lambda i:i.wanted_id), p.created_wanted_instances)
        
        
s = Tester__LParser(expr_sentence_in_abbr_text1)
s.turn_off_show()
s.test__is_WantedID_to_ConChildRule()
s.test__con_instance2all_children_instances_alts()
s.test__alt_instance2all_instance_alts()
s.test__build_output_grammar_rooted_by()
s.test__build_output_grammar_end_at()


