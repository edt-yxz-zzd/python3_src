
'''
whole_BaGuaHelper
to help remember 64重卦 name and their 上下经卦 by encoding 上卦 into 声母（可能不考虑前后鼻音的区别） and 下卦 into 韵母（可能不考虑'g'、声调的区别）


sm2ym2num2good_hanzi_str
    # :: Map sm (Map ym (Map Int String))
->[make_sm2ym_num_graph__for_good_hanzis]->
sm2ym_num_graph__for_good_hanzis
    # == sm2ym_num_ls :: Map sm [ym_num]
    # ym_num = f'{ym}{num}'
->[find_cliques__sm2ym_num_graph.iter_find_cliques__sm2ym_num_graph]->
iter_sms_yms_pairs__sm2ym_num_graph
    # :: Iter ([sm], [ym])
->[make_max_cliques__sm2ym_num_graph]->
max_cliques__sm2ym_num_graph
    # :: Map (size, size) [([sm], [ym])]
->[refine_max_cliques__sm2ym_num_graph.make_max_refined_pair2original_max_pairs]->
max_refined_pair2original_max_pairs__shT_ygT_ydT_nsm8_nym8
    # :: Map ([sm], [ym]) [([sm], [ym])]
->[refine_sm2ym2num2good_hanzis]->
refined_sm2ym2num2good_hanzi_str
    # ~ sm2ym2num2good_hanzi_str :: Map sm (Map ym (Map Int String))
->[more_refine_sm2ym2num2good_hanzi_str]->
more_refined_sm2ym2num2good_hanzi_str
    # ~ sm2ym2num2good_hanzi_str :: Map sm (Map ym (Map Int String))
'''

__all__ = '''
    whole_BaGuaHelper
    '''.split()

from .make_sm2ym_num_graph__for_good_hanzis import \
    make_sm2ym_num_graph__for_good_hanzis
from .find_cliques__sm2ym_num_graph import \
    iter_find_cliques__sm2ym_num_graph
from .make_max_cliques__sm2ym_num_graph import \
    make_max_cliques__sm2ym_num_graph
from .refine_max_cliques__sm2ym_num_graph import \
    make_max_refined_pair2original_max_pairs
from .refine_sm2ym2num2good_hanzis import \
    refine_sm2ym2num2good_hanzis
from .more_refine_sm2ym2num2good_hanzi_str import \
    more_refine_sm2ym2num2good_hanzi_str

def whole_BaGuaHelper(sm2ym2num2good_hanzi_str, chars, *
    ,sm_remove_h_1:bool
    ,ym_remove_g_1:bool
    ,sm_remove_h_2:bool
    ,ym_remove_g_2:bool
    ,ym_remove_digit_2:bool
    ,min_len_sm_ls_2:bool
    ,min_len_ym_ls_2:bool
    ):
    '-> Iter more_refined_sm2ym2num2good_hanzi_str'
    (sm2ym_num_graph__for_good_hanzis
    ) = make_sm2ym_num_graph__for_good_hanzis(sm2ym2num2good_hanzi_str)
    (iter_sms_yms_pairs__sm2ym_num_graph
    ) = iter_find_cliques__sm2ym_num_graph(
            sm2ym_num_graph__for_good_hanzis
            ,sm_remove_h=sm_remove_h_1
            ,ym_remove_g=ym_remove_g_1
            )
    (max_cliques__sm2ym_num_graph
    ) = make_max_cliques__sm2ym_num_graph(iter_sms_yms_pairs__sm2ym_num_graph)
    (max_refined_pair2original_max_pairs__shT_ygT_ydT_nsm8_nym8
    ) = make_max_refined_pair2original_max_pairs(
            max_cliques__sm2ym_num_graph
            ,sm_remove_h=sm_remove_h_2
            ,ym_remove_g=ym_remove_g_2
            ,ym_remove_digit=ym_remove_digit_2
            ,min_len_sm_ls=min_len_sm_ls_2
            ,min_len_ym_ls=min_len_ym_ls_2
            )
    for sms_yms_pairs in max_refined_pair2original_max_pairs__shT_ygT_ydT_nsm8_nym8.values():
        for sms_yms_pair in sms_yms_pairs:
            sm_ls, ym_ls = sms_yms_pair
        (refined_sm2ym2num2good_hanzi_str
        ) = refine_sm2ym2num2good_hanzis(
                sm_ls, ym_ls, sm2ym2num2good_hanzi_str)
        (more_refined_sm2ym2num2good_hanzi_str
        ) = more_refine_sm2ym2num2good_hanzi_str(
                refined_sm2ym2num2good_hanzi_str, chars
                )
        yield more_refined_sm2ym2num2good_hanzi_str




if __name__ == '__main__':
    from .more_refined_sm2ym2num2good_hanzi_str import \
        more_refined_sm2ym2num2good_hanzi_str as sm2ym2num2good_hanzi_str
    from pprint import pprint
    it = whole_BaGuaHelper(
        sm2ym2num2good_hanzi_str, None
        ,sm_remove_h_1=False
        ,ym_remove_g_1=False
        ,sm_remove_h_2=True
        ,ym_remove_g_2=True
        ,ym_remove_digit_2=True
        ,min_len_sm_ls_2=8
        ,min_len_ym_ls_2=8
        )
    for new_sm2ym2num2good_hanzi_str in it:
        print('=====')
        pprint(new_sm2ym2num2good_hanzi_str)


