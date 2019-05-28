
sm,ym - 声母、韵母
    for more defs see: normal_pinyin_prime2full_pinyin_prime.py
所有函数用法见whole_BaGuaHelper.py


######################
=>0
###################### sources:
allHanyuPinyinPrime_list.txt
●CJK汉字拼音表_更新_42856字.txt
中华字经[郭保华][2003].txt
=>3
###################### others:
__pycache__
__init__.py
readme.txt
more_refined_sm2ym2num2good_hanzi_str__by_hand[halt].py
=>7


######################
######################
######################
=>0
######################
normal_pinyin_prime2full_pinyin_prime.py
    +allHanyuPinyinPrime_list.txt
    normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair.txt
read_CJK汉字拼音表_更新_42856字.py
    +●CJK汉字拼音表_更新_42856字.txt
    hanzi2pinyins.py
=>4
######################
make_sm2ym2num2good_hanzis.py
    +normal_pinyin_prime2full_pinyin_prime.py
    +hanzi2pinyins.py
        sm2ym2num2good_hanzi_str.py
=>6
######################
make_sm2ym_num_graph__for_good_hanzis.py
    +sm2ym2num2good_hanzi_str.py
        sm2ym_num_graph__for_good_hanzis.py
=>8
######################
find_cliques__sm2ym_num_graph.py
    +sm2ym_num_graph__for_good_hanzis.py
        all_cliques__sm2ym_num_graph.txt
=>10
######################
make_max_cliques__sm2ym_num_graph.py
    +all_cliques__sm2ym_num_graph.txt
    max_cliques__sm2ym_num_graph.py
=>12
######################
refine_max_cliques__sm2ym_num_graph.py
    +max_cliques__sm2ym_num_graph.py
    max_refined_pair2original_max_pairs__shT_ygT_ydT_nsm8_nym8.py
=>14
### unique clique!!! when args = shT_ygT_ydT_nsm8_nym8
(['c', 'ch', 'd', 'g', 'h', 'k', 's', 't', 'z', 'zh'], ['a1', 'a3', 'ai1', 'ai3', 'ai4', 'an1', 'an3', 'an4', 'ang1', 'ang3', 'ang4', 'ao1', 'ao3', 'ao4', 'eng1', 'ong1', 'ong3', 'ong4', 'ou1', 'ou3', 'ou4', 'u1', 'u2', 'u3', 'u4', 'uei1', 'uei3', 'uei4', 'uo4'])

######################
refine_sm2ym2num2good_hanzis.py
    +sm2ym2num2good_hanzi_str.py
    +max_refined_pair2original_max_pairs__shT_ygT_ydT_nsm8_nym8.py
    refined_sm2ym2num2good_hanzi_str.py
=>16
######################
read_中华字经.py
    +中华字经[郭保华][2003].txt
    chars_3980.py
=>18
######################
more_refine_sm2ym2num2good_hanzi_str.py
    +chars_3980.py
    +refined_sm2ym2num2good_hanzi_str.py
    more_refined_sm2ym2num2good_hanzi_str.py
=>20

######################
whole_BaGuaHelper.py
    +...all above...
    final_sm2ym2num2good_hanzi_str.txt
=>22


