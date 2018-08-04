
# see nn_ns.char.unicode_database.unihan_variants2dict
#   data derived from UniHan database

__all__ = '''
    chars_with_multi_ST vary_chars all_chars_with_variant
    '''.split()


from seed.io.RCXW import make_rcxw__pickle

vary_charss = make_rcxw__pickle(..., 'vary_charss.py.obj')()

def process(chars_with_multi_ST, vary_chars, all_chars_with_variant):
    return (chars_with_multi_ST, vary_chars, all_chars_with_variant)

(chars_with_multi_ST, vary_chars, all_chars_with_variant) = \
    process(**vary_charss)



