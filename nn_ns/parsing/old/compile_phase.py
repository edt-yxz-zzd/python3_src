
#                         parse                   translate
grammar__text             ==>> grammar__syntax_tree ==>> grammar__rules
source                    ==>> tokens               ==>> symbols
(grammar__rules, symbols) ==>> syntax_tree          ==>> result??
