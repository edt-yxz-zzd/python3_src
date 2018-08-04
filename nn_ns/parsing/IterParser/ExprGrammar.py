

'''
Expr {
    MaybeAddExpr
}

MaybeAddExpr {
    AddExpr
    MaybeMulExpr
}
AddExpr = MaybeAddExpr '+' MaybeMulExpr ;

MaybeMulExpr {
    MulExpr
    AtomWithSpaces
}
MulExpr = MaybeMulExpr '*'  AtomWithSpaces;

AtomWithSpaces = MaybeSpaces Atom MaybeSpaces ;
MaybeSpaces {
    Spaces
    Null
}
Spaces = 'space' MaybeSpaces ;
Null = ;

Atom {
    'valuable'
    Bracket
}
Bracket = '(' Expr ')' ;

'''


from .IDTypes_and_RuleTypes import *
from sand.types.AbbrSentenceOps import SentenceInForms, AbbrSentenceOps

Expr, MaybeAddExpr, AddExpr, MaybeMulExpr, MulExpr, Atom, Bracket\
      , AtomWithSpaces, MaybeSpaces, Spaces, Null =\
      map(InputID,
          'Expr, MaybeAddExpr, AddExpr, MaybeMulExpr, MulExpr'
          ', Atom, Bracket, AtomWithSpaces, MaybeSpaces, Spaces, Null'
          .split(', '))

plus, star, lbr, rbr, val, space = map(InputID, '+ * ( ) valuable space'.split())
    
##AddExpr_1_3, MulExpr_1_3, Bracket_1_3 =\
##      map(InputID, 'AddExpr_1_3, MulExpr_1_3, Bracket_1_3'
##          .split(', '))
##
##AddExpr_0_1 = MaybeMulExpr
##AddExpr_1_2 = plus
##AddExpr_2_3 = MaybeAddExpr
##
##MulExpr_0_1 = Atom
##MulExpr_1_2 = star
##MulExpr_2_3 = MaybeMulExpr
##
##Bracket_0_1 = lbr
##Bracket_1_2 = Expr
##Bracket_2_3 = rbr

input_id2rule = {
    Expr: AltRule([MaybeAddExpr]),
    MaybeAddExpr: AltRule([AddExpr, MaybeMulExpr]),
    MaybeMulExpr: AltRule([MulExpr, AtomWithSpaces]),
    Atom: AltRule([Bracket, val]),
    MaybeSpaces: AltRule([Spaces, Null]),

    AddExpr: ConRule([MaybeAddExpr, plus, MaybeMulExpr]),
    MulExpr: ConRule([AtomWithSpaces, star, MaybeMulExpr]), # reverse the order of the above grammar cause error???
    Bracket: ConRule([lbr, Expr, rbr]),
    AtomWithSpaces: ConRule([MaybeSpaces, Atom, MaybeSpaces]),
    Spaces: ConRule([space, MaybeSpaces]),
    Null: ConRule([]),

##    AddExpr: BinConRule(AddExpr_0_1, AddExpr_1_3),
##    AddExpr_1_3 : BinConRule(AddExpr_1_2, AddExpr_2_3),
##    
##    
##    MulExpr: BinConRule(MulExpr_0_1, MulExpr_1_3),
##    MulExpr_1_3 : BinConRule(MulExpr_1_2, MulExpr_2_3),
##    
##    
##    Bracket: BinConRule(Bracket_0_1, Bracket_1_3),
##    Bracket_1_3 : BinConRule(Bracket_1_2, Bracket_2_3),

    
    plus: ter_rule,
    star: ter_rule,
    lbr: ter_rule,
    rbr: ter_rule,
    val: ter_rule,
    space: ter_rule,


    }

#main_id = Expr

if 1:
    _g = cleaned(input_id2rule, Expr)
    assert _g == input_id2rule

abbr_char2word = {'x': 'val', '(': 'lbr', ')': 'rbr', '+':'plus', '*':'star', ' ': 'space'}
expr_sentence_ops = AbbrSentenceOps(abbr_char2word, globals(), ID.unbox)
toExprSentence = lambda abbr_text: expr_sentence_ops.to_forms(abbr_text, ExprSentenceInForms)

class ExprSentenceInForms(SentenceInForms):
    main_id = Expr
ExprSentenceInForms.input_id2rule = input_id2rule




expr_sentence_in_abbr_text1 = '(x+x*x) * x+((( (x))) )*(x *x)*x*   x+x'
expr_sentence_in_abbr_text2 = 'x*x*x+x'





