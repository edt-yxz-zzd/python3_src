
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xa2L2\xe5;\x9e\x17\x19\xf7\xeeFZ\x85W~\x9e'
    
_lr_action_items = {'$end':([0,1,3,5,6,7,8,9,11,13,14,15,34,37,],[-26,-10,-9,-18,-26,0,-1,-19,-7,-2,-6,-14,-5,-3,]),'RULE_BODY_BEGIN':([3,12,18,21,29,30,31,32,33,38,],[-9,18,-26,18,-20,-26,-11,-4,-21,-15,]),'SYMBOL':([0,3,4,6,11,13,14,16,18,23,24,30,34,37,],[3,-9,3,3,-7,-2,-6,3,3,3,-8,3,-5,-3,]),'AT_START_SYMBOL':([0,3,6,11,13,14,34,37,],[4,-9,4,-7,-2,-6,-5,-3,]),'BODY_BEGIN':([2,3,10,11,],[12,-9,16,-7,]),'BODY_END':([3,12,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,],[-9,-26,-26,-13,-26,-24,34,-26,-25,-26,-8,-12,-22,37,-23,-20,-26,-11,-4,-21,-17,-16,-15,]),'AT_TERMINALS':([0,3,6,11,13,14,34,37,],[10,-9,10,-7,-2,-6,-5,-3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'StatementCrossOption':([0,6,],[1,1,]),'SymbolCrossOption':([18,30,],[31,31,]),'RuleBody':([12,21,],[21,21,]),'Symbol':([0,4,6,16,18,23,30,],[11,11,11,24,30,24,30,]),'SymbolStar':([18,30,],[32,38,]),'RuleBodyCrossOption':([12,21,],[17,17,]),'StatementStar':([0,6,],[8,15,]),'Terminal':([16,23,],[23,23,]),'StartSymbol':([4,],[13,]),'Nonterminal':([0,4,6,],[2,14,2,]),'StatementCross':([0,6,],[5,5,]),'Statement':([0,6,],[6,6,]),'SymbolCross':([18,30,],[29,29,]),'GrammarB':([0,],[7,]),'TerminalCrossOption':([16,23,],[25,25,]),'RuleBodyCross':([12,21,],[19,19,]),'TerminalCross':([16,23,],[26,26,]),'TerminalStar':([16,23,],[27,36,]),'Null':([0,6,12,16,18,21,23,30,],[9,9,22,28,33,22,28,33,]),'RuleBodyStar':([12,21,],[20,35,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> GrammarB","S'",1,None,None,None),
  ('GrammarB -> StatementStar','GrammarB',1,'p_GrammarB','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',18),
  ('Statement -> AT_START_SYMBOL StartSymbol','Statement',2,'p_SetStartSymbolStmt','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',32),
  ('Statement -> AT_TERMINALS BODY_BEGIN TerminalStar BODY_END','Statement',4,'p_ImportTerminals','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',37),
  ('RuleBody -> RULE_BODY_BEGIN SymbolStar','RuleBody',2,'p_RuleBody','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',45),
  ('Statement -> Nonterminal BODY_BEGIN RuleBodyStar BODY_END','Statement',4,'p_DefineRule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',48),
  ('StartSymbol -> Nonterminal','StartSymbol',1,'p_copy_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',77),
  ('Nonterminal -> Symbol','Nonterminal',1,'p_copy_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',78),
  ('Terminal -> Symbol','Terminal',1,'p_copy_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',79),
  ('Symbol -> SYMBOL','Symbol',1,'p_copy_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',81),
  ('StatementStar -> StatementCrossOption','StatementStar',1,'p_star_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',89),
  ('SymbolStar -> SymbolCrossOption','SymbolStar',1,'p_star_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',90),
  ('TerminalStar -> TerminalCrossOption','TerminalStar',1,'p_star_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',91),
  ('RuleBodyStar -> RuleBodyCrossOption','RuleBodyStar',1,'p_star_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',92),
  ('StatementCross -> Statement StatementStar','StatementCross',2,'p_cross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',105),
  ('SymbolCross -> Symbol SymbolStar','SymbolCross',2,'p_cross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',106),
  ('TerminalCross -> Terminal TerminalStar','TerminalCross',2,'p_cross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',107),
  ('RuleBodyCross -> RuleBody RuleBodyStar','RuleBodyCross',2,'p_cross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',108),
  ('StatementCrossOption -> StatementCross','StatementCrossOption',1,'p_optioncross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',111),
  ('StatementCrossOption -> Null','StatementCrossOption',1,'p_optioncross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',112),
  ('SymbolCrossOption -> SymbolCross','SymbolCrossOption',1,'p_optioncross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',113),
  ('SymbolCrossOption -> Null','SymbolCrossOption',1,'p_optioncross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',114),
  ('TerminalCrossOption -> TerminalCross','TerminalCrossOption',1,'p_optioncross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',115),
  ('TerminalCrossOption -> Null','TerminalCrossOption',1,'p_optioncross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',116),
  ('RuleBodyCrossOption -> RuleBodyCross','RuleBodyCrossOption',1,'p_optioncross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',117),
  ('RuleBodyCrossOption -> Null','RuleBodyCrossOption',1,'p_optioncross_rule','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\GrammarB_yacc.py',118),
  ('Null -> <empty>','Null',0,'p_Null','E:\\my_data\\program_source\\python3_src\\nn_ns\\using\\using_PLY\\parse_common.py',154),
]
