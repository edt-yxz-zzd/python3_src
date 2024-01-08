#__all__:goto
#失败: 未考虑到 需要分别计数: [len4curr_total_prefix === num_cells4begin_cell_type +num_cells4end_cell_type +num_cells4extra_cell_type]
#   {st:count} ---> {(st,num_cells4begin_cell_type,num_cells4end_cell_type,num_cells4extra_cell_type):count}
#   [total === sum{(count * sz4alphabet9cell4begin_marker**num_cells4begin_cell_type * sz4alphabet9cell4end_marker**num_cells4end_cell_type * sz4alphabet9cell4extra**num_cells4extra_cell_type) | [((st,num_cells4begin_cell_type,num_cells4end_cell_type,num_cells4extra_cell_type),count) :<- ...][filter st]}]
#   view others/数学/矩阵乘法解释-平行世界.txt
r'''[[[
e ../../python3_src/seed/seq_tools/avoid_substrs__multi_word_delimiter_token__layout_with_std_both_marker__solid_counting.py


seed.seq_tools.avoid_substrs__multi_word_delimiter_token__layout_with_std_both_marker__solid_counting
py -m nn_ns.app.debug_cmd   seed.seq_tools.avoid_substrs__multi_word_delimiter_token__layout_with_std_both_marker__solid_counting -x
py -m nn_ns.app.doctest_cmd seed.seq_tools.avoid_substrs__multi_word_delimiter_token__layout_with_std_both_marker__solid_counting:__doc__ -ff -v
py_adhoc_call   seed.seq_tools.avoid_substrs__multi_word_delimiter_token__layout_with_std_both_marker__solid_counting   @f
from seed.seq_tools.avoid_substrs__multi_word_delimiter_token__layout_with_std_both_marker__solid_counting import *


[[
扩展编码: regex"1{m}[210]*0{w}" where [m,w>=1] && middle part doesnot contain prefix/suffix
    2 - sz4alphabet9cell4extra
    1 - sz4alphabet9cell4begin_marker
    0 - sz4alphabet9cell4end_marker
    ######################
    [len(alphabet9cell4extra \-/ alphabet9cell4begin_marker \-/ alphabet9cell4end_marker) == len(alphabet9cell4extra) + len(alphabet9cell4begin_marker) + len(alphabet9cell4end_marker) <= sz4alphabet]
        #pairwise-disjoint
    ######################
    [sz4alphabet9cell4extra >= 0]
    [sz4alphabet9cell4begin_marker >= 1]
    [sz4alphabet9cell4end_marker >= 1]
    [len4begin_marker >= 1]
        #m
    [len4end_marker >= 1]
        #w
    [min(len4begin_marker, len4end_marker) >= 1 + [sz4alphabet9cell4extra == 0]]
    ######################

===xxx:不可逆:
状态:当前后缀:
    * regex'^1{m}$'
        [st := 0]
        [st == 0]
    * regex'[20]1{n}$' [1<=n<=m-1]
        [st := n]
        [1 <= st <= m-1]
    * regex'[210]2$'
        [st := m]
        [st == m]
    * regex'[21]0{u}$' [1<=u<=w-1]
        [st := m+u]
        [m+1 <= st <= m+w-1]
    * regex'[21]0{w}$'
        [st := m+w]
        [st == m+w]
    [0 <= st <= m+w]

[L := m+w+1]
[st_trans_mx_ex_(m,w) =[def]= mk_matrix__ij2v(L,L, \irow,icolumn ->
    if [icolumn == 0] then 0 #不可逆！
    elif [icolumn == 1] then [[irow == m]or[m+1 <= irow <= m+w-1]]
    elif [2 <= icolumn <= m-1] then [irow+1 == icolumn]
    elif [icolumn == m] then [irow =!= m+w]
    elif [icolumn == m+1] then [[irow == m]or[1 <= irow <= m-1]]
    elif [m+2 <= icolumn <= m+w-1] then [irow+1 == icolumn]
    elif [icolumn == m+w] then [irow+1 == icolumn]
    else error
    )]
===
状态:当前后缀:
    * regex'[20]1{n}$' [1<=n<=m-1]
        [m >= 2]:
            [st := n-1]
            [0 <= st <= m-2]
    * regex'[210]2$'
        [st := m-1]
        [st == m-1]
    * regex'[21]0{u}$' [1<=u<=w-1]
        [w >= 2]:
            [st := m-1+u]
            [m <= st <= m+w-2]
    [0 <= st <= m+w-2]

[L := m+w-1]
[st_trans_mx_ex_(m,w) =[def]= mk_matrix__ij2v(L,L, \irow,icolumn ->
    if [m >= 2][icolumn == 0] then [m-1 <= irow <= m+w-2]
    elif [m >= 2][1 <= icolumn <= m-2] then [irow+1 == icolumn]
    elif [icolumn == m-1] then 1
    elif [w >= 2][icolumn == m] then [0 <= irow <= m-1]
    elif [w >= 2][m+1 <= icolumn <= m+w-2] then [irow+1 == icolumn]
    else error
    )]

===
[st_trans_mx_ex_(m,w) == mk_matrix__ij2v(L,L, \irow,icolumn ->
    if [icolumn == m-1] then 1
    elif [m >= 2][icolumn == 0] then [m-1 <= irow <= m+w-2]
    elif [w >= 2][icolumn == m] then [0 <= irow <= m-1]
    else [irow+1 == icolumn]
    )]
    # [:st_trans_mx_ex___m_ge1___w_ge1]:here
===
[st_trans_mx_ex_(1,1) == [1;]]
===
[st_trans_mx_ex_(2,2) ==
    [0,1,1
    ;1,1,1
    ;1,1,0
    ]]
===
[st_trans_mx_ex_(1,2) ==
    [1,1
    ;1,0
    ]]
===
[st_trans_mx_ex_(2,1) ==
    [0,1
    ;1,1
    ]]
===
[st_trans_mx_ex_(3,3) ==
    [0,1,1,1,0
    ;0,0,1,1,0
    ;1,0,1,1,0
    ;1,0,1,0,1
    ;1,0,1,0,0
    ]]
    可逆！<<==:
    [mx[:,2] := mx[:,0] +mx[:,3] -mx[:,2]]
    [mx[:,0] :-= +mx[:,2]]
    [mx[:,3] :-= +mx[:,2]]
    [0,1,0,1,0
    ;0,0,0,1,0
    ;0,0,1,0,0
    ;1,0,0,0,1
    ;1,0,0,0,0
    ]
    [mx[:,3] :-= +mx[:,1]]
    [mx[:,0] :-= +mx[:,4]]
    [0,1,0,0,0
    ;0,0,0,1,0
    ;0,0,1,0,0
    ;0,0,0,0,1
    ;1,0,0,0,0
    ]
    [swap mx[:,2], mx[:,3]]
    [0,1,0,0,0
    ;0,0,1,0,0
    ;0,0,0,1,0
    ;0,0,0,0,1
    ;1,0,0,0,0
    ]
    [left_rotate(1, mx)]
    [1,0,0,0,0
    ;0,1,0,0,0
    ;0,0,1,0,0
    ;0,0,0,1,0
    ;0,0,0,0,1
    ]
    [mx === echo_mx_(5)]
===
[st_trans_mx_ex_(2,3) ==
    [0,1,1,0
    ;1,1,1,0
    ;1,1,0,1
    ;1,1,0,0
    ]]
===
[st_trans_mx_ex_(1,3) ==
    [1,1,0
    ;1,0,1
    ;1,0,0
    ]]
===
[st_trans_mx_ex_(3,2) ==
    [0,1,1,1
    ;0,0,1,1
    ;1,0,1,1
    ;1,0,1,0
    ]]
===
[st_trans_mx_ex_(3,1) ==
    [0,1,1
    ;0,0,1
    ;1,0,1
    ]]
===
[0 <= i<j<k < L]:
    # [mx[:,j] := mx[:,i] +mx[:,k] -mx[:,j]]
    #   NOTE: rhs is j not i/k
    [mx_column_add_sub_(L; i,j,k) =[def]= mk_matrix__ij2v(L,L, \irow,icolumn ->
        if [icolumn =!= j] then [irow==icolumn]
        elif [irow==icolumn] then -1
        else [irow <- {i,k}]
    )]
===
[0 <= i,j < L][i =!= j]:
    # [mx[:,i] := mx[:,i] -mx[:,j]]
    #   NOTE: rhs is i not j
    [mx_column_sub_(L; i,j) =[def]= mk_matrix__ij2v(L,L, \irow,icolumn ->
        if [icolumn =!= i] then [irow==icolumn]
        elif [irow==j] then -1
        else [irow == icolumn]
    )]
===
[0 <= i<j < L]:
    [mx_column_swap_(L; i,j) =[def]= mk_matrix__ij2v(L,L, \irow,icolumn ->
        if [icolumn == i] then [irow==j]
        elif [icolumn == j] then [irow==i]
        else [irow == icolumn]
    )]
===
[0 <= num_steps < L]:
    [mx_left_rotate_(L; num_steps) =[def]= mk_matrix__ij2v(L,L, \irow,icolumn -> [irow == (icolumn+num_steps)%L])]

===
[min(m,w) >= 2]:
    #st_trans_mx_ex_(2,2)
    #st_trans_mx_ex_(2,3)
    #st_trans_mx_ex_(3,3)
    #st_trans_mx_ex_(3,2)
    [st_trans_mx_ex_(m,w) * mx_column_add_sub_(L;0,m-1,m) * mx_column_sub_(L; 0,m-1) * mx_column_sub_(L; m,m-1) * II{mx_column_sub_(L; 0,j) | [j :<- [m+1..=m+w-2]]} * II{mx_column_sub_(L; m,j) | [j :<- [1..=m-2]]} * mx_column_swap_(L; m-1,m) * mx_left_rotate_(L; 1) == mx_echo_(L)]
    [st_trans_mx_ex_(m,w)**-1 == mx_column_add_sub_(L;0,m-1,m) * mx_column_sub_(L; 0,m-1) * mx_column_sub_(L; m,m-1) * II{mx_column_sub_(L; 0,j) | [j :<- [m+1..=m+w-2]]} * II{mx_column_sub_(L; m,j) | [j :<- [1..=m-2]]} * mx_column_swap_(L; m-1,m) * mx_left_rotate_(L; 1)]
    [st_trans_mx_ex_(3,3)**-1 ==
    [ 0,-1, 1, 0, 0
    ; 1,-1, 0, 0, 0
    ; 0, 1,-1, 0, 1
    ; 0, 0, 1, 0,-1
    ; 0, 0, 0, 1,-1
    ]]
    [st_trans_mx_ex_(4,4)**-1 ==
    [ 0, 0,-1, 1, 0, 0, 0
    ; 1, 0,-1, 0, 0, 0, 0
    ; 0, 1,-1, 0, 0, 0, 0
    ; 0, 0, 1,-1, 0, 0, 1
    ; 0, 0, 0, 1, 0, 0,-1
    ; 0, 0, 0, 0, 1, 0,-1
    ; 0, 0, 0, 0, 0, 1,-1
    ]]
    [st_trans_mx_ex_(2,4)**-1 ==
    [-1, 1, 0, 0, 0
    ; 1,-1, 0, 0, 1
    ; 0, 1, 0, 0,-1
    ; 0, 0, 1, 0,-1
    ; 0, 0, 0, 1,-1
    ]]
    [st_trans_mx_ex_(m,w)**-1 == mk_matrix__ij2v(L,L, \irow,icolumn ->
        if [icolumn == m+w-2] then
            if [irow >= m] then -1 else [irow == m-1]
        elif [icolumn == m-1] then
            if [irow == m-1] then -1 else [irow <- {0,m}]
        elif [icolumn == m-2] then
            if [irow <= m-2] then -1 else [irow == m-1]
        else [irow == icolumn+1]
        )]
        # [:inv_st_trans_mx_ex___m_ge2___w_ge2]:here
===
[1 == m < 2 <= w]:
    #st_trans_mx_ex_(1,2)
    #st_trans_mx_ex_(1,3)
    [st_trans_mx_ex_(1,w) == mk_matrix__ij2v(L,L, \irow,icolumn ->
    if [icolumn == 0] then 1
    else [irow+1 == icolumn]
    )]
    [st_trans_mx_ex_(1,w) * II{mx_column_sub_(L; 0,j) | [j :<- [1..=w-1]]} * mx_left_rotate_(L;1) == mx_echo_(L)]
    [st_trans_mx_ex_(1,w)**-1 == II{mx_column_sub_(L; 0,j) | [j :<- [1..=w-1]]} * mx_left_rotate_(L;1)]
    [st_trans_mx_ex_(1,w)**-1 == mk_matrix__ij2v(L,L, \irow,icolumn ->
        if [icolumn == w-1] then
            if [irow == 0] then 1 else -1
        else [irow == icolumn+1]
        )]
        # [:inv_st_trans_mx_ex___m_eq1___w_ge2]:here
===
[1 == w < 2 <= m]:
    #st_trans_mx_ex_(2,1)
    #st_trans_mx_ex_(3,1)
    [st_trans_mx_ex_(m,1) == mk_matrix__ij2v(L,L, \irow,icolumn ->
        if [icolumn == m-1] then 1
        else [(irow+1)%L == icolumn]
        )]
    [st_trans_mx_ex_(m,1) * II{mx_column_sub_(L; m-1,j) | [j :<- [0..=m-2]]} * mx_left_rotate_(L;1) == mx_echo_(L)]
    [st_trans_mx_ex_(m,1) == II{mx_column_sub_(L; m-1,j) | [j :<- [0..=m-2]]} * mx_left_rotate_(L;1)]
    [st_trans_mx_ex_(m,1)**-1 == mk_matrix__ij2v(L,L, \irow,icolumn ->
        if [icolumn == m-2] then
            if [irow == m-1] then 1 else -1
        else [irow == (icolumn+1)%L]
        )]
        # [:inv_st_trans_mx_ex___m_ge2___w_eq1]:here
===
[1 == m == w]:
    [st_trans_mx_ex_(1,1) == [1;]]
    [st_trans_mx_ex_(1,1)**-1 == [1;]]
        # [:inv_st_trans_mx_ex___m_eq1___w_eq1]:here
===
]]


[[
e ../../python3_src/seed/seq_tools/avoid_substrs__multi_word_delimiter_token__layout_with_std_both_marker__solid_counting.py
    #solid_encoding
    #solid_counting
编码: regex"1{n}[01]*0{n}" where [n>=2] && middle part doesnot contain prefix/suffix
    ===
    固实型整数编码/固实计数
        view ../../python3_src/seed/seq_tools/avoid_substrs.py
            状态:当前后缀为 regex'(^$)|(((^|0)1{m}|(^|1)0{m})$)', [1 <= m <= n], [0 <= st < 2*n+1]
            状态:比下面将提出的st多了3个状态: 起始空缀 以及 应避子串[m==n]
            状态:与下面布设区别: 1前，0后
            py_adhoc_call   seed.seq_tools.avoid_substrs   ,11:iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_  =2  =2 =1 =1
        #view ./script/整数编码-多单元联合前缀-完全序号.py
            陈旧#弃置
        #无关:view ./script/bifix.py
            自相关等价类
    ===
    计算『前缀固定且后缀定长』情形下的编码空间规模
    ===
    状态转移矩阵: 状态st: 当前后缀为 regex'01{m}|10{m}$', [1 <= m <= n-1], [-(n-1) <= st < n-1]
      # [st < 0] <-> regex'01{m}' && [m==-st]
      # [st >= 0] <-> regex'10{m}' && [m==st+1]
    [st' =[def]= next st]
    [st2idx_(n;st) =[def]= if st < 0 then n-2 -st else st]
    [irow := st2idx_(n;st)]
    [icolumn := st2idx_(n;st')]
    [L := 2*(n-1)]
    [n>=2]:
        [st_trans_mx_(n) =[def]= [[if [[1 <= icolumn < n-1]or[n <= icolumn < 2*(n-1)]] then [icolumn == irow+1] elif [icolumn == 0] then [irow >= n-1] elif [icolumn == n-1] then [irow < n-1] | [icolumn :<- [0..<2*(n-1)]]] | [irow :<- [0..<2*(n-1)]]]]
    [n==2]:
        [L == 2]
        [st_trans_mx_(2) =:
        [0,1
        ;1,0
        ;]]
        [st_trans_mx_(2)**-1 == st_trans_mx_(2)]
    [n==3]:
        [L == 4]
        [st_trans_mx_(3) =:
        [0,1,1,0
        ;0,0,1,0
        ;1,0,0,1
        ;1,0,0,0
        ;]]
    [n==4]:
        [L == 6]
        [st_trans_mx_(4) =:
        [0,1,0,1,0,0
        ;0,0,1,1,0,0
        ;0,0,0,1,0,0
        ;1,0,0,0,1,0
        ;1,0,0,0,0,1
        ;1,0,0,0,0,0
        ;]]
    状态转移矩阵 可逆！
        行消元法+旋转置换
    [L >= 2][irow,icolumn :<- [0..<L]][irow =!= icolumn]:
        [mx_move_(L; irow, icolumn, scale) =[def]= [[if (irow, icolumn)==(_irow, _icolumn) then scale else [_irow==_icolumn] | [_icolumn :<- [0..<L]]] | [_irow :<- [0..<L]]]]
    [L >= 2]:
        [mx_down_rotate_(L; num_steps) =[def]= [[[(irow-num_steps)%L == icolumn] | [icolumn :<- [0..<L]]] | [irow :<- [0..<L]]]]
    [n >= 2]:
        !! [L := 2*(n-1)]
        [L >= 2]
        [mx_down_rotate_(L; 1) * II{mx_move_(L; irow, n-1, -1) | [irow :<- [0..=n-3]]} * II{mx_move_(L; irow, 0, -1) | [irow :<- [n-1..=2*n-4]]} * st_trans_mx_(n) == mx_echo_(L)]
        [st_trans_mx_(n)**-1 == mx_down_rotate_(L; 1) * II{mx_move_(L; irow, n-2, -1) | [irow :<- [0..=n-3]]} * II{mx_move_(L; irow, 2*n-3, -1) | [irow :<- [n-1..=2*n-4]]}]
    [st_trans_mx_(3)**-1 =:
        [0,0,0,1
        ;1,-1,0,0
        ;0,1,0,0
        ;0,0,1,-1
        ;]]
    [st_trans_mx_(4)**-1 =:
        [0,0,0,0,0,1
        ;1,0,-1,0,0,0
        ;0,1,-1,0,0,0
        ;0,0,1,0,0,0
        ;0,0,0,1,0,-1
        ;0,0,0,0,1,-1
        ;]]
    [n >= 2]:
        [st_trans_mx_(n)**-1 == [[if [[0 <= icolumn <= n-3]or[n-1 <= icolumn <= 2*n-4]] then [icolumn == irow-1] elif [icolumn == n-2] then (if [1 <= irow < n-1] then -1 else [irow == n-1]) elif [icolumn == 2*n-3] then (if [irow >= n] then -1 else [irow == 0]) | [icolumn :<- [0..<2*(n-1)]]] | [irow :<- [0..<2*(n-1)]]]]
    ===
    ===
ho  w to reduce computation of 『for en range(L)[::-1]: pow(mx, e)』
    ===
    view ../../python3_src/seed/data_funcs/lnkls.py
      view ../../python3_src/seed/types/BitList.py
    ===
    可逆化:给定一个方阵V，如何增广为方阵W，使W可逆，且V**e在W**e左上角？若V为整数方阵，则可否令W与W**-1皆是整数方阵？
      xxx不符合『左上角保持』: [0;] --> [0,1; 1,0;]
      [V := A] --> [W := [A, B; C, D;]]
      [W**2 == [(A**2 +B*C), (A*B +B*D); (C*A +D*C), (C*B +D**2)] == [A**2, ...; ..., ...;]]
      ==>> [B*C 为 零方阵]
      [WW * W == [AA, BB; CC, DD;] * [A, B; C, D;] == [(AA*A +BB*C), (AA*B +BB*D); (CC*A +DD*C), (CC*B +DD*D)]]
          # [W**-1 exists]
          # [WW can be any square matrix]
          # [WW can be W**k]
          # [WW can be W]
          # [BB can be B]
          # [AA can be A]
      [k>=1][WW == W**k]:
          !! [(AA*A +BB*C) == AA*A]
          [BB*C is 000mx]
          !! [BB := B -|- (AA*B +BB*D)]
          [B*C is 000mx]
          !! [BB := B -|- (AA*B +BB*D)]
          !! [BB*C is 000mx]
          [(AA*B +BB*D)*C is 000mx]
          [(AA*B +(AA*B +BB*D)*D)*C is 000mx]
          ...
          !! [B*C is 000mx]
          [BB*D*C is 000mx]
          [(AA*B +BB*D)*D*C is 000mx]
          [(AA*B +(AA*B +BB*D)*D)*D*C is 000mx]
          ...
          [B*D*C is 000mx]
          [(AA*B +B*D)*D*C is 000mx]
          [(AA*B +(AA*B +B*D)*D)*D*C is 000mx]
          ...
          [B*D*C is 000mx]
          [B*D*D*C is 000mx]
          [B*D*D*D*C is 000mx]
          ...
          [[e >= 0] -> [B*D**e*C is 000mx]]
          [[e >= 0] -> [BB*D**e*C is 000mx]]
      [B*C, (D*C or B*D) are 000mx][k>=1]:
          [W**k 左上角 A**k]
          ##有毛病:不对称！
      [[e >= 0] -> [B*D**e*C is 000mx]][k>=1]:
          [W**k 左上角 A**k]
      [C is 000mx]:
          [[e >= 0] -> [B*D**e*C is 000mx]]
          [WW * W == [AA, BB; CC, DD;] * [A, B; 0, D;] == [(AA*A), (AA*B +BB*D); (CC*A), (CC*B +DD*D)]]
          !! [A is given hence out of control #may be 000mx]
          [useful: (AA*B +BB*D), (CC*B +DD*D)]
          !! [WW can be any square matrix]
          [not$ [W**-1 exists]]
          _L
      [C is not 000mx]
      [B is not 000mx]
      [B,C are not 000mx]
      [A is 000mx][[e >= 0] -> [B*D**e*C is 000mx]]:
        [B*C == 0]
        [not$ [(B*C)**-1 exists]]
        # !! [B,C are not 000mx]
        #??? [mx_rank_(B) < min()]
        [k>=1][WW == W**k]:
          [W**k 左上角 A**k]
          [AA == A**k == 000mx]
          [[e >= 0] -> [BB*D**e*C is 000mx]]
          [WW * W == [(AA*A +BB*C), (AA*B +BB*D); (CC*A +DD*C), (CC*B +DD*D)] == [0, (BB*D); (DD*C), (CC*B +DD*D)]]
      感觉不太行，至少[A==[0;]]时不行（一阶零矩阵）。
    ===
    ===
]]


>>> print_mx__semicolon_(mk__st_trans_mx_(2))
[0,1
;1,0
]
>>> print_mx__lsls_(mk__inv_st_trans_mx_(2))
[[0,1]
,[1,0]
]

>>> print_mx__semicolon_(mk__st_trans_mx_(3))
[0,1,1,0
;0,0,1,0
;1,0,0,1
;1,0,0,0
]
>>> print_mx__lsls_(mk__inv_st_trans_mx_(3))
[[0,0,0,1]
,[1,-1,0,0]
,[0,1,0,0]
,[0,0,1,-1]
]

>>> print_mx__semicolon_(mk__st_trans_mx_(4))
[0,1,0,1,0,0
;0,0,1,1,0,0
;0,0,0,1,0,0
;1,0,0,0,1,0
;1,0,0,0,0,1
;1,0,0,0,0,0
]
>>> print_mx__lsls_(mk__inv_st_trans_mx_(4))
[[0,0,0,0,0,1]
,[1,0,-1,0,0,0]
,[0,1,-1,0,0,0]
,[0,0,1,0,0,0]
,[0,0,0,1,0,-1]
,[0,0,0,0,1,-1]
]

>>> print_mx__semicolon_(mk__st_trans_mx_(5))
[0,1,0,0,1,0,0,0
;0,0,1,0,1,0,0,0
;0,0,0,1,1,0,0,0
;0,0,0,0,1,0,0,0
;1,0,0,0,0,1,0,0
;1,0,0,0,0,0,1,0
;1,0,0,0,0,0,0,1
;1,0,0,0,0,0,0,0
]
>>> print_mx__lsls_(mk__inv_st_trans_mx_(5))
[[0,0,0,0,0,0,0,1]
,[1,0,0,-1,0,0,0,0]
,[0,1,0,-1,0,0,0,0]
,[0,0,1,-1,0,0,0,0]
,[0,0,0,1,0,0,0,0]
,[0,0,0,0,1,0,0,-1]
,[0,0,0,0,0,1,0,-1]
,[0,0,0,0,0,0,1,-1]
]





#]]]'''
__all__ = r'''
mk__st_trans_mx_ex_
    mk__inv_st_trans_mx_ex_
print_mx__semicolon_
    print_mx__lsls_









    ValidateFail

    mk__st_trans_mx_
        mk__inv_st_trans_mx_
            validate__inv_st_trans_mx_
                ValidateFail__inv_st_trans_mx
                ValidateFail__data4inv_st_trans_mx
                ValidateFail__data4st_trans_mx

    mx2str_
        print_mx_
            print_mx__semicolon_
            print_mx__lsls_


    mk__st_trans_mx_ex_
        mk__inv_st_trans_mx_ex_
            validate__inv_st_trans_mx_ex_
                ValidateFail__inv_st_trans_mx_ex
                ValidateFail__data4inv_st_trans_mx_ex
                ValidateFail__data4st_trans_mx_ex

    check_args4multi_cell_delimiter_token__layout_with_std_both_marker
'''.split()#'''
__all__

from operator import __index__
from itertools import count as count_

from seed.tiny import check_type_is, check_callable
from seed.tiny_.check import check_int_ge #check_uint_lt, check_int_ge_lt, , check_int_ge_le
from seed.tiny_.dict__add_fmap_filter import fmap4dict_value_with_key
from seed.helper.repr_input import repr_helper

from seed.math.matrix.solve_matrix import NoRowMatrix, linear_solver, ring_ex_ops__int # ring_ex_ops__Fraction, ring_ex_ops__BinaryField
    #linear_solver :: LinearEquationSolver <: BasicOps4MatrixOverRing <: BasicMatrixOps
    #
    #BasicMatrixOps.mk_matrix__ij2v/get_matrix_shape
    #def mk_matrix__ij2v(sf, num_rows, num_cols, ij2v, /):
    #def mk_matrix__seq(sf, num_rows, num_cols, seq, begin=None, end=None, step=None, /, *, row_oriented__vs__column_oriented=False):

    #seed.math.IRingOps::IRingOps.mk_ring_element5int
    #ring_ex_ops__int :: IRingExOps <: IRingOps

_ops4ring = ring_ex_ops__int
_ops4mx = linear_solver
def _fr(i, /):
    i = __index__(i)
    i = _ops4ring.mk_ring_element5int(i)
    return i
def _mk_L_(n, /):
    check_int_ge(2, n)
    L = (n-1)<<1
    return L
def mk__st_trans_mx_(n, /):
    '-> st_trans_mx'
    # [st_trans_mx_(n) =[def]= [[if [[1 <= icolumn < n-1]or[n <= icolumn < 2*(n-1)]] then [icolumn == irow+1] elif [icolumn == 0] then [irow >= n-1] elif [icolumn == n-1] then [irow < n-1] | [icolumn :<- [0..<2*(n-1)]]] | [irow :<- [0..<2*(n-1)]]]]
    L = _mk_L_(n)
    st_trans_mx = _ops4mx.mk_matrix__ij2v(L, L, lambda irow, icolumn: _fr((irow >= n-1) if icolumn == 0 else ((irow < n-1) if icolumn == n-1 else (icolumn==irow+1))))
    return st_trans_mx
def mk__inv_st_trans_mx_(n, /):
    '-> inv st_trans_mx'
    # [st_trans_mx_(n)**-1 == [[if [[0 <= icolumn <= n-3]or[n-1 <= icolumn <= 2*n-4]] then [icolumn == irow-1] elif [icolumn == n-2] then (if [1 <= irow < n-1] then -1 else [irow == n-1]) elif [icolumn == 2*n-3] then (if [irow >= n] then -1 else [irow == 0]) | [icolumn :<- [0..<2*(n-1)]]] | [irow :<- [0..<2*(n-1)]]]]
    L = _mk_L_(n)
    inv_st_trans_mx = _ops4mx.mk_matrix__ij2v(L, L, lambda irow, icolumn: _fr((-1 if irow >= n else irow==0) if icolumn == L-1 else ((-1 if 1 <= irow < n-1 else irow==n-1) if icolumn == n-2 else (icolumn==irow-1))))
    return inv_st_trans_mx

class ValidateFail(Exception):pass
class ValidateFail__inv_st_trans_mx(ValidateFail):pass
class ValidateFail__data4inv_st_trans_mx(ValidateFail):pass
class ValidateFail__data4st_trans_mx(ValidateFail):pass
def validate__inv_st_trans_mx_(n, /):
    L = _mk_L_(n)
    st_trans_mx = mk__st_trans_mx_(n)
    inv_st_trans_mx = mk__inv_st_trans_mx_(n)
    assert (L,L) == _ops4mx.get_matrix_shape(st_trans_mx)
    assert (L,L) == _ops4mx.get_matrix_shape(inv_st_trans_mx)
    ######################
    result_mx = _ops4mx.mul__matrix(_ops4ring, st_trans_mx, inv_st_trans_mx)
    echo_mx = _ops4mx.mk_matrix__echo(L, L, _ops4ring)
    if not _ops4mx.eq__matrix(_ops4ring, echo_mx, result_mx): raise ValidateFail__inv_st_trans_mx(n)

def _data4test__st_trans_mx():
    [st_trans_mx__2 :=
        [0,1
        ,1,0
        ,]]
    [st_trans_mx__3 :=
        [0,1,1,0
        ,0,0,1,0
        ,1,0,0,1
        ,1,0,0,0
        ,]]
    [st_trans_mx__4 :=
        [0,1,0,1,0,0
        ,0,0,1,1,0,0
        ,0,0,0,1,0,0
        ,1,0,0,0,1,0
        ,1,0,0,0,0,1
        ,1,0,0,0,0,0
        ,]]
    [inv_st_trans_mx__2 :=
        st_trans_mx__2]
    [inv_st_trans_mx__3 :=
        [0,0,0,1
        ,1,-1,0,0
        ,0,1,0,0
        ,0,0,1,-1
        ,]]
    [inv_st_trans_mx__4 :=
        [0,0,0,0,0,1
        ,1,0,-1,0,0,0
        ,0,1,-1,0,0,0
        ,0,0,1,0,0,0
        ,0,0,0,1,0,-1
        ,0,0,0,0,1,-1
        ,]]
    sn2mx = {(sn:=int(nm[-1]) * (-1)**(nm.startswith('inv'))) : _ops4mx.mk_matrix__seq(L:=_mk_L_(abs(sn)), L, seq, convertor=_fr) for nm, seq in locals().items()}
    return sn2mx
def _test__data4st_trans_mx():
    sn2mx = _data4test__st_trans_mx()
    for n in range(2,5):
        st_trans_mx = sn2mx[n]
        inv_st_trans_mx = sn2mx[-n]
        if not _ops4mx.eq__matrix(_ops4ring, st_trans_mx, mk__st_trans_mx_(n)): raise ValidateFail__data4st_trans_mx(n)
        if not _ops4mx.eq__matrix(_ops4ring, inv_st_trans_mx, mk__inv_st_trans_mx_(n)): raise ValidateFail__data4inv_st_trans_mx(n)

def _test__inv_st_trans_mx(max1_n, /):
    for n in range(2, max1_n):
        validate__inv_st_trans_mx_(n)
def _test__st_trans_mx(max1_n, /):
    _test__data4st_trans_mx()
    _test__inv_st_trans_mx(max1_n)
_test__st_trans_mx(7)
if __name__ == "__main__":
    _test__st_trans_mx(20)


def print_mx__semicolon_(mx, /, *, to_str=None, str__vs__repr=False):
    print_mx_(mx, to_str=to_str, str__vs__repr=str__vs__repr, semicolon__vs__list_list=False)
    return
def print_mx__lsls_(mx, /, *, to_str=None, str__vs__repr=False):
    print_mx_(mx, to_str=to_str, str__vs__repr=str__vs__repr, semicolon__vs__list_list=True)
    return
def print_mx_(mx, /, *, to_str=None, str__vs__repr=False, semicolon__vs__list_list=False):
    s = mx2str_(mx, to_str=to_str, str__vs__repr=str__vs__repr, semicolon__vs__list_list=semicolon__vs__list_list)
    print(s)
    return
def mx2str_(mx, /, *, to_str=None, str__vs__repr=False, semicolon__vs__list_list=False):
    (num_rows, num_cols) = _ops4mx.get_matrix_shape(mx)
    if str__vs__repr is False:
        _to_str_ = str
    elif str__vs__repr is True:
        _to_str_ = repr
    else:
        raise 000
    if  to_str is None:
        to_str = _to_str_
    to_str
    check_callable(to_str)

    newline = '\n'
    begin4mx = '['
    end4mx = ']'
    sep9element = ','
    if semicolon__vs__list_list is False:
        # semicolon
        sep9row = ';'
        begin4row = ''
        end4row = ''
    elif semicolon__vs__list_list is True:
        # list_list
        sep9row = ','
        begin4row = '['
        end4row = ']'
    else:
        raise 000
    ######################
    newline
    begin4mx
    end4mx
    sep9row
    begin4row
    end4row
    sep9element
    ######################
    if not num_rows:
        return _to_str_(mx)

    ######################
    def iter4mx_():
        head9line = begin4mx
        for irow in range(num_rows):
            it = iter4row_(mx[irow])
            content = sep9element.join(it)
            yield f'{head9line}{begin4row}{content}{end4row}'
            head9line = sep9row
        yield end4mx
    def iter4row_(row, /):
        for icolumn in range(num_cols):
            yield to_str(row[icolumn])

    return newline.join(iter4mx_())




######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
#### n --> (m,w) #####
######################
######################
######################


def _mk_L_ex_(m, w, /):
    check_int_ge(1, m)
    check_int_ge(1, w)
    L = m+w-1
    return L
def mk__st_trans_mx_ex_(m, w, /):
    # [:st_trans_mx_ex___m_ge1___w_ge1]:goto
    L = _mk_L_ex_(m,w)
    st_trans_mx_ex = _ops4mx.mk_matrix__ij2v(L, L, lambda irow, icolumn: _fr(1 if icolumn == m-1 else ((m-1 <= irow) if m >= 2 and icolumn == 0 else ((irow < m) if w >= 2 and icolumn == m else (irow+1 == icolumn)))))
    return st_trans_mx_ex

def mk__inv_st_trans_mx_ex_(m, w, /):
    L = _mk_L_ex_(m,w)
    if m == 1 and w == 1:
        # [:inv_st_trans_mx_ex___m_eq1___w_eq1]:goto
        def ij2v(irow, icolumn, /):
            return 1
    elif m >= 2 and w == 1:
        # [:inv_st_trans_mx_ex___m_ge2___w_eq1]:goto
        def ij2v(irow, icolumn, /):
            return (1 if irow == m-1 else -1) if icolumn == m-2 else (irow == (icolumn+1)%m)
    elif m == 1 and w >= 2:
        # [:inv_st_trans_mx_ex___m_eq1___w_ge2]:goto
        def ij2v(irow, icolumn, /):
            return (1 if irow == 0 else -1) if icolumn == w-1 else (irow == icolumn+1)
    elif m >= 2 and w >= 2:
        # [:inv_st_trans_mx_ex___m_ge2___w_ge2]:goto
        def ij2v(irow, icolumn, /):
            if icolumn == L-1:
                return -1 if irow >= m else (irow == m-1)
            elif icolumn == m-1:
                return -1 if irow == m-1 else (irow in (0,m))
            elif icolumn == m-2:
                return -1 if irow <= m-2 else (irow == m-1)
            else:
                return (irow == icolumn+1)
    else:
        raise 000
    ij2v
    inv_st_trans_mx_ex = _ops4mx.mk_matrix__ij2v(L, L, ij2v, convertor=_fr)
    return inv_st_trans_mx_ex

class ValidateFail__inv_st_trans_mx_ex(ValidateFail):pass
class ValidateFail__data4inv_st_trans_mx_ex(ValidateFail):pass
class ValidateFail__data4st_trans_mx_ex(ValidateFail):pass
def validate__inv_st_trans_mx_ex_(m, w, /):
    L = _mk_L_ex_(m, w)
    st_trans_mx_ex = mk__st_trans_mx_ex_(m, w)
    inv_st_trans_mx_ex = mk__inv_st_trans_mx_ex_(m, w)
    assert (L,L) == _ops4mx.get_matrix_shape(st_trans_mx_ex)
    assert (L,L) == _ops4mx.get_matrix_shape(inv_st_trans_mx_ex)
    ######################
    result_mx = _ops4mx.mul__matrix(_ops4ring, st_trans_mx_ex, inv_st_trans_mx_ex)
    echo_mx = _ops4mx.mk_matrix__echo(L, L, _ops4ring)
    if not _ops4mx.eq__matrix(_ops4ring, echo_mx, result_mx): raise ValidateFail__inv_st_trans_mx_ex(m, w)


def _data4test__st_trans_mx_ex():
    mw2seq4mx = (
    {(1,1): [1]
    ,(2,2):
    [0,1,1
    ,1,1,1
    ,1,1,0
    ]
    ,(1,2):
    [1,1
    ,1,0
    ]
    ,(2,1):
    [0,1
    ,1,1
    ]
    ,(3,3):
    [0,1,1,1,0
    ,0,0,1,1,0
    ,1,0,1,1,0
    ,1,0,1,0,1
    ,1,0,1,0,0
    ]
    ,(2,3):
    [0,1,1,0
    ,1,1,1,0
    ,1,1,0,1
    ,1,1,0,0
    ]
    ,(1,3):
    [1,1,0
    ,1,0,1
    ,1,0,0
    ]
    ,(3,2):
    [0,1,1,1
    ,0,0,1,1
    ,1,0,1,1
    ,1,0,1,0
    ]
    ,(3,1):
    [0,1,1
    ,0,0,1
    ,1,0,1
    ]
    })
    mw2seq4inv_mx = (
    {(3,3):
    [ 0,-1, 1, 0, 0
    , 1,-1, 0, 0, 0
    , 0, 1,-1, 0, 1
    , 0, 0, 1, 0,-1
    , 0, 0, 0, 1,-1
    ]
    ,(4,4):
    [ 0, 0,-1, 1, 0, 0, 0
    , 1, 0,-1, 0, 0, 0, 0
    , 0, 1,-1, 0, 0, 0, 0
    , 0, 0, 1,-1, 0, 0, 1
    , 0, 0, 0, 1, 0, 0,-1
    , 0, 0, 0, 0, 1, 0,-1
    , 0, 0, 0, 0, 0, 1,-1
    ]
    ,(2,4):
    [-1, 1, 0, 0, 0
    , 1,-1, 0, 0, 1
    , 0, 1, 0, 0,-1
    , 0, 0, 1, 0,-1
    , 0, 0, 0, 1,-1
    ]
    })
    def f(mw, seq, /):
        m, w = mw
        L = _mk_L_ex_(m, w)
        assert L**2 == len(seq)
        mx = _ops4mx.mk_matrix__seq(L, L, seq, convertor=_fr)
        return mx
    mw2mx = fmap4dict_value_with_key(f, mw2seq4mx)
    mw2inv_mx = fmap4dict_value_with_key(f, mw2seq4inv_mx)
    return (mw2mx, mw2inv_mx)


def _test__data4st_trans_mx_ex():
    (mw2mx, mw2inv_mx) = _data4test__st_trans_mx_ex()
    ######################
    for (m, w), mx in mw2mx.items():
        L = _mk_L_ex_(m, w)
        st_trans_mx_ex = mk__st_trans_mx_ex_(m, w)
        if not _ops4mx.eq__matrix(_ops4ring, mx, st_trans_mx_ex): raise ValidateFail__data4st_trans_mx_ex(m, w)

    ######################
    for (m, w), inv_mx in mw2inv_mx.items():
        L = _mk_L_ex_(m, w)
        inv_st_trans_mx_ex = mk__inv_st_trans_mx_ex_(m, w)
        if not _ops4mx.eq__matrix(_ops4ring, inv_mx, inv_st_trans_mx_ex): raise ValidateFail__data4inv_st_trans_mx_ex(m, w)
    ######################

def _test__inv_st_trans_mx_ex(max1_m, max1_w, /):
    for m in range(1, max1_m):
        for w in range(1, max1_w):
            validate__inv_st_trans_mx_ex_(m, w)

def _test__st_trans_mx_ex(max1_m, max1_w, /):
    _test__data4st_trans_mx_ex()
    _test__inv_st_trans_mx_ex(max1_m, max1_w)
_test__st_trans_mx_ex(7, 7)

#def solid_counting__multi_word_delimiter_token__layout_with_std_both_marker_(num_bits9word, len4both_marker, /):
#def solid_counting__multi_word_delimiter_token__layout_with_std_both_marker_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, /):
def check_args4multi_cell_delimiter_token__layout_with_std_both_marker(len4begin_marker, len4end_marker, sz4alphabet9cell4begin_marker, sz4alphabet9cell4end_marker, sz4alphabet9cell4extra, /):
    check_int_ge(0, sz4alphabet9cell4extra)
    check_int_ge(1, sz4alphabet9cell4begin_marker)
    check_int_ge(1, sz4alphabet9cell4end_marker)
    check_int_ge(1, len4begin_marker)
    check_int_ge(1, len4end_marker)
    if not min(len4begin_marker, len4end_marker) >= 1 + (sz4alphabet9cell4extra == 0): raise ValueError
    ######################
    m = len4begin_marker
    w = len4end_marker
    ######################
if 0:
  class SolidCounting__multi_cell_delimiter_token__layout_with_std_both_marker:
    def __init__(sf, len4begin_marker, len4end_marker, sz4alphabet9cell4begin_marker, sz4alphabet9cell4end_marker, sz4alphabet9cell4extra, /):
        check_args4multi_cell_delimiter_token__layout_with_std_both_marker(len4begin_marker, len4end_marker, sz4alphabet9cell4begin_marker, sz4alphabet9cell4end_marker, sz4alphabet9cell4extra)
        sf._args = (len4begin_marker, len4end_marker, sz4alphabet9cell4begin_marker, sz4alphabet9cell4end_marker, sz4alphabet9cell4extra)
        m = len4begin_marker
        w = len4end_marker
        L = _mk_L_ex_(m, w)
        st_trans_mx_ex = mk__st_trans_mx_ex_(m, w)
        inv_st_trans_mx_ex = mk__inv_st_trans_mx_ex_(m, w)
        row0__prefix_sz_eq_m = _ops4mx.mk_matrix__ij2v(1, L, lambda irow, icolumn: _fr(icolumn==m-2))

        sf._data = (L, st_trans_mx_ex, inv_st_trans_mx_ex, row0__prefix_sz_eq_m)
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args)
    def iter_len_count_pairs(sf, /):
        '-> (len, count)'
        (len4begin_marker, len4end_marker, sz4alphabet9cell4begin_marker, sz4alphabet9cell4end_marker, sz4alphabet9cell4extra) = sf._args
        (L, st_trans_mx_ex, inv_st_trans_mx_ex, row0__prefix_sz_eq_m) = sf._data
        m = len4begin_marker
        w = len4end_marker
        for sz in range(m+1):
            yield sz, 0
        row = row0__prefix_sz_eq_m
        assert row[0][-1] == 0
        for sz in count_(m+1):
            count = row[0][-1]
            ...
            ...
            不行
            yield sz, count
            row = _ops4mx.mul__matrix(_ops4ring, row, st_trans_mx_ex)

    def solid_counting(sf, /):
        (len4begin_marker, len4end_marker, sz4alphabet9cell4begin_marker, sz4alphabet9cell4end_marker, sz4alphabet9cell4extra) = sf._args
        ...


def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
__all__


from seed.seq_tools.avoid_substrs__multi_word_delimiter_token__layout_with_std_both_marker__solid_counting import *
