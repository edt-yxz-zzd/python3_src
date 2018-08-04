
import bisect
from direct_translate_data import 黑暗圣剑传说



def match_one_word(sorted_list_of_word_lengths, translation_table, sentence, start):
    ls = sorted_list_of_word_lengths
    R = len(sentence) - start
    t = bisect.bisect_right(ls, R)
    assert all(R < L for L in ls[t:])
    
    for L in reversed(ls[:t]):
        assert 0 < L <= R
        old_word = sentence[start : start+L]
        new_word = translation_table.get(old_word, None)
        if new_word is not None:
            new_start = start + L
            
            return old_word, new_word, new_start

    return None


def direct_translate(translation_table, sentence, start = 0):
    ls = dict2sorted_list_of_word_lengths(translation_table)
    new_words = []
    old_words = []
    
    while True:
        r = match_one_word(ls, translation_table, sentence, start)
        if r is None:
            break
        old_word, new_word, start = r
        new_words.append(new_word)
        old_words.append(old_word)

    return old_words, new_words, start

def dict2sorted_list_of_word_lengths(d):
    ls = list(set(map(len, d.keys())))
    ls.sort()
    return ls



    

def translate_sentence(table, sentence):
    olds, news, start = direct_translate(table, sentence)
    if start < len(sentence):
        return None
    
    return ''.join(news)

def translate_sentences(table, sentences):
    for sentence in sentences:
        new = translate_sentence(table, sentence)
        if new:
            print(sentence, '  --->  ', new)

translate_sentences(黑暗圣剑传说.兽语.翻译表, 黑暗圣剑传说.兽语.例句集)








