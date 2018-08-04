

'''
see: "def - test_data_text.txt"
see:
    test_data_text.py

'''

__all__ = ['test_data_text2iter_test_data']

from seed.iters.icut_to import icut_seq_to

def test_data_text2iter_test_data(test_data_text):
    cases = test_data_text.split('=====')
    if cases[0].strip():
        raise ValueError('nonspaces before first =====')
    cases = cases[1:]
    for case in cases:
        yield from case_text2iter_test_data(case)

def case_text2iter_test_data(case_text):
    slots = case_text.split('-----')
    if (len(slots) & 1) == 0:
        # len(slots) is even
        raise ValueError('bad format: actions without result tree. \n{}'
                         .format(case_text))
    initial_text = slots[0]
    for action_text, result_text in icut_seq_to(slots[1:], 2):
        yield initial_text, action_text, result_text


