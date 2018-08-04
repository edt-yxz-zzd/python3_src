



import unicodedata



def search(ords, pred):
    name = unicodedata.name
    for i in ords:
        c = chr(i)
        s = name(c, None)
        if s is not None and pred(s):
            #print(c,s)
            yield c
    pass


def to_names(s):
    return list(map(unicodedata.name, s))



def gen_name2letter(s, namemap):
    names = to_names(s)
    if namemap == None:
        namemap = lambda x:x
    return {namemap(name): c
            for c, name in zip(s, names)
            if namemap(name) is not None}




    

lcgreeks = LCGreek = lowercase_greek_alphabet = 'αβγδεζηθικλμνξοπρστυφχψω'
ucgreeks = UCGreek = uppercase_greak_alphabet = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
greek_letter_name2lower_letter = gen_name2letter(LCGreek, lambda s:s.split()[-1])
{'BETA': 'β', 'CHI': 'χ', 'PHI': 'φ', 'XI': 'ξ', 'ETA': 'η', 'SIGMA': 'σ',
 'KAPPA': 'κ', 'UPSILON': 'υ', 'DELTA': 'δ', 'ALPHA': 'α', 'OMEGA': 'ω',
 'TAU': 'τ', 'OMICRON': 'ο', 'EPSILON': 'ε', 'GAMMA': 'γ', 'MU': 'μ',
 'IOTA': 'ι', 'RHO': 'ρ', 'PSI': 'ψ', 'PI': 'π', 'LAMDA': 'λ', 'NU': 'ν',
 'ZETA': 'ζ', 'THETA': 'θ'}


assert UCGreek.lower() == LCGreek
assert UCGreek == LCGreek.upper()
assert len(LCGreek) == 24
# false: sassert len(LCGreek) == ord(LCGreek[-1]) - ord(LCGreek[0]) + 1



lcgreek_name_pairs = tuple(sorted((c, name) for name, c in greek_letter_name2lower_letter.items()))
(('α', 'ALPHA'),   ('β', 'BETA'),   ('γ', 'GAMMA'),   ('δ', 'DELTA'),
 ('ε', 'EPSILON'), ('ζ', 'ZETA'),   ('η', 'ETA'),     ('θ', 'THETA'),
 ('ι', 'IOTA'),    ('κ', 'KAPPA'),  ('λ', 'LAMDA'),   ('μ', 'MU'),
 ('ν', 'NU'),      ('ξ', 'XI'),     ('ο', 'OMICRON'), ('π', 'PI'),
 ('ρ', 'RHO'),     ('σ', 'SIGMA'),  ('τ', 'TAU'),     ('υ', 'UPSILON'),
 ('φ', 'PHI'),     ('χ', 'CHI'),    ('ψ', 'PSI'),     ('ω', 'OMEGA'))









'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡ΢ΣΤΥΦΧΨΩ'
'αβγδεζηθικλμνξοπρςστυφχψω'





def _search_greek():
    
    lcgreek = ''.join(search(range(3000), lambda s: s.startswith('GREEK SMALL LETTER')))
    ucgreek = ''.join(search(range(3000), lambda s: s.startswith('GREEK CAPITAL LETTER')))
    print(len(lcgreek))
    print(len(ucgreek))
    print(lcgreek)
    print(ucgreek)
    assert len(lcgreek) == 46
    assert len(ucgreek) == 38
    
    '''

ͱ GREEK SMALL LETTER HETA
ͳ GREEK SMALL LETTER ARCHAIC SAMPI
ͷ GREEK SMALL LETTER PAMPHYLIAN DIGAMMA
ΐ GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS
ά GREEK SMALL LETTER ALPHA WITH TONOS
έ GREEK SMALL LETTER EPSILON WITH TONOS
ή GREEK SMALL LETTER ETA WITH TONOS
ί GREEK SMALL LETTER IOTA WITH TONOS
ΰ GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS
α GREEK SMALL LETTER ALPHA
β GREEK SMALL LETTER BETA
γ GREEK SMALL LETTER GAMMA
δ GREEK SMALL LETTER DELTA
ε GREEK SMALL LETTER EPSILON
ζ GREEK SMALL LETTER ZETA
η GREEK SMALL LETTER ETA
θ GREEK SMALL LETTER THETA
ι GREEK SMALL LETTER IOTA
κ GREEK SMALL LETTER KAPPA
λ GREEK SMALL LETTER LAMDA
μ GREEK SMALL LETTER MU
ν GREEK SMALL LETTER NU
ξ GREEK SMALL LETTER XI
ο GREEK SMALL LETTER OMICRON
π GREEK SMALL LETTER PI
ρ GREEK SMALL LETTER RHO
ς GREEK SMALL LETTER FINAL SIGMA
σ GREEK SMALL LETTER SIGMA
τ GREEK SMALL LETTER TAU
υ GREEK SMALL LETTER UPSILON
φ GREEK SMALL LETTER PHI
χ GREEK SMALL LETTER CHI
ψ GREEK SMALL LETTER PSI
ω GREEK SMALL LETTER OMEGA
ϊ GREEK SMALL LETTER IOTA WITH DIALYTIKA
ϋ GREEK SMALL LETTER UPSILON WITH DIALYTIKA
ό GREEK SMALL LETTER OMICRON WITH TONOS
ύ GREEK SMALL LETTER UPSILON WITH TONOS
ώ GREEK SMALL LETTER OMEGA WITH TONOS
ϙ GREEK SMALL LETTER ARCHAIC KOPPA
ϛ GREEK SMALL LETTER STIGMA
ϝ GREEK SMALL LETTER DIGAMMA
ϟ GREEK SMALL LETTER KOPPA
ϡ GREEK SMALL LETTER SAMPI
ϸ GREEK SMALL LETTER SHO
ϻ GREEK SMALL LETTER SAN
Ͱ GREEK CAPITAL LETTER HETA
Ͳ GREEK CAPITAL LETTER ARCHAIC SAMPI
Ͷ GREEK CAPITAL LETTER PAMPHYLIAN DIGAMMA
Ά GREEK CAPITAL LETTER ALPHA WITH TONOS
Έ GREEK CAPITAL LETTER EPSILON WITH TONOS
Ή GREEK CAPITAL LETTER ETA WITH TONOS
Ί GREEK CAPITAL LETTER IOTA WITH TONOS
Ό GREEK CAPITAL LETTER OMICRON WITH TONOS
Ύ GREEK CAPITAL LETTER UPSILON WITH TONOS
Ώ GREEK CAPITAL LETTER OMEGA WITH TONOS
Α GREEK CAPITAL LETTER ALPHA
Β GREEK CAPITAL LETTER BETA
Γ GREEK CAPITAL LETTER GAMMA
Δ GREEK CAPITAL LETTER DELTA
Ε GREEK CAPITAL LETTER EPSILON
Ζ GREEK CAPITAL LETTER ZETA
Η GREEK CAPITAL LETTER ETA
Θ GREEK CAPITAL LETTER THETA
Ι GREEK CAPITAL LETTER IOTA
Κ GREEK CAPITAL LETTER KAPPA
Λ GREEK CAPITAL LETTER LAMDA
Μ GREEK CAPITAL LETTER MU
Ν GREEK CAPITAL LETTER NU
Ξ GREEK CAPITAL LETTER XI
Ο GREEK CAPITAL LETTER OMICRON
Π GREEK CAPITAL LETTER PI
Ρ GREEK CAPITAL LETTER RHO
Σ GREEK CAPITAL LETTER SIGMA
Τ GREEK CAPITAL LETTER TAU
Υ GREEK CAPITAL LETTER UPSILON
Φ GREEK CAPITAL LETTER PHI
Χ GREEK CAPITAL LETTER CHI
Ψ GREEK CAPITAL LETTER PSI
Ω GREEK CAPITAL LETTER OMEGA
Ϊ GREEK CAPITAL LETTER IOTA WITH DIALYTIKA
Ϋ GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA
Ϸ GREEK CAPITAL LETTER SHO
Ϻ GREEK CAPITAL LETTER SAN
ͱͳͷΐάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϙϛϝϟϡϸϻ
ͰͲͶΆΈΉΊΌΎΏΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫϷϺ

'''

if __name__ == '__main__':
    print(to_names(LCGreek))
    print(to_names(UCGreek))
    print(greek_letter_name2lower_letter)
    print(lcgreek_name_pairs)
    
    
    

