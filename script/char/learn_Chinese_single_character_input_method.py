
'''
map table:
    char2input_seq_ls
learning characters:
    chars_to_learn

length per paragraph:
    len_p

randomly generate a paragraph to ask learner to input
# using '.' as the wild charactor.
print the correct input sequence list if miss matched.

极点郑码　反查询　ctrl+/ ==>> 郑码+拼音
'''

from sand import fixed__package__
fixed__package__(globals())
from random import randrange
from itertools import zip_longest
from .char2zm.frequent_chars__from_novel__L0 import frequent_chars__from_novel__L0 as _chars

def learn_Chinese_single_character_input_method(
    char2input_seq_ls, chars_to_learn, len_p):
    L = len(chars_to_learn)
    while True:
        paragraph = ''.join(chars_to_learn[randrange(L)] for _ in range(len_p))
        print('input:\n  {}'.format(paragraph))
        ans = input('>>')
        if not ans:
            break
        for i, correct_ch, input_ch in zip(range(len_p), paragraph, ans):
            if correct_ch != input_ch:
                print('{}: {!r} -> {!r} : {}'.format(
                    i, input_ch, correct_ch, char2input_seq_ls[correct_ch]))


frequent_chars = '''\
的一了是不这我人有在他道来大个你就着到上\
也那说下然出么之子看时可地要们没过后为都\
她自中还天心小得去对和只能里以头会起想手\
身好如而无面些声眼事李什笑却己知前多已真\
经现但将意开气力生张点样所情白此话方间让\
被两军见家很女清才神又回当发于再明动从风\
老正三长成年几把十法打实星少色口主本光用\
向死定其太最听问给次王边住门觉走便脸战原\
何行种进果等高重儿分直怎全衣水公外山啊候\
做同杀更微相'''

# before 擞, count>=100, after/include 擞, count<100
assert 4209 == _chars.index('擞')
frequent_chars = _chars[:2000]



if __name__ == '__main__':
    from char2zm.char2zm import char2zm_ls
    char2input_seq_ls = char2zm_ls
    print('极点郑码　反查询　ctrl+/ ==>> 郑码+拼音')
    print('frequent charaters: {}'.format(frequent_chars))
    
    chars_to_learn = input('chars_to_learn: ')
    chars_to_learn = chars_to_learn.strip()
    if chars_to_learn:
        len_p = input('length per paragraph: ')
        len_p = int(len_p)
        
        if chars_to_learn and len_p > 0:
            learn_Chinese_single_character_input_method(
                char2input_seq_ls, chars_to_learn, len_p)
    









    
