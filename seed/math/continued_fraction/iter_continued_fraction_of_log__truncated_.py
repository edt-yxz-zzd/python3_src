#__all__:goto
# API:goto
r'''[[[
e ../../python3_src/seed/math/continued_fraction/iter_continued_fraction_of_log__truncated_.py
[[
copy from:
e script/log_b_y.py
view others/数学/continued-fraction/continued_fraction_of_logB_Y.txt

.+1,$s/\<script\>.\<log_b_y\>/seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_/g
    except:
view  /sdcard/0my_files/tmp/out4py/script.log_b_y..1p10000-2-3.out.txt
]]

seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_
py -m nn_ns.app.debug_cmd   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ -x
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_:__doc__ -ff -v




[[[
result is exact, though truncated
===
我的算法，对原论文算法进行修改:连分数 奇偶位 切换 floor/ceil，得到 真正的上下限，可以确定 哪些是有效位，而原文只是 估计...
===
see:
    dfloor_log_ex_
    ufloor_log_ex_
    lcf  # 原连分数cf的下限
    gcf  # 原连分数cf的上限
    [lcf <= cf <= gcf]
===
[1 < b < y]:
    [x == log_(b;y)]
    [b**x == y]
    [1 < b < b**x]
    [cf := cf_(x)]
    [x == t0 == cf0 + t1]
    [b**cf0 <= b**(cf0+t1) < b**(cf0+1)]
    [1 <= b**t1 == y/b**cf0 < b]
    [1 == b**t1 < b]:
        #stop
        [x == cf0]
    [1 < b**t1 < b]:
        #recur
        [1 < b < b**(1/t1)]
        [t1 == 1/(cf1+t2)]
        [1 < b < b**(cf1+t2)]

===

[1 < b < y]:
    [y[0] := y]
    [b[0] := b]
    [1 < b[0] < y[0]]
    [cf[i] := floor_log_(b[i];y[i])]
    [b[i]**cf[i] <= y[i] < b[i]**(cf[i]+1)]
    * [b[i]**cf[i] == y[i]]:
        #stop
        [cf[i+1:] = [+oo]*inf]
    * [b[i]**cf[i] < y[i]]:
        #recur
        [b[i]**cf[i] < y[i] < b[i]**(cf[i]+1)]
        [1 < y[i]/b[i]**cf[i] < b[i]]
        [b[i+1] := y[i]/b[i]**cf[i]]
        [y[i+1] := b[i]]

===
[1 < b < y]:
    [y[0] := y]
    [b[0] := b]
    [1 < b[0] < y[0]]
    [1 <= b[i] < y[i]]
    * [b[i] == 1]:
        #stop
        [cf[i:] = [+oo]*inf]
    * [b[i] > 1]:
        [cf[i] := floor_log_(b[i];y[i])]
        [b[i]**cf[i] <= y[i] < b[i]**(cf[i]+1)]
        [1 <= y[i]/b[i]**cf[i] < b[i]]
        [b[i+1] := y[i]/b[i]**cf[i]]
        [y[i+1] := b[i]]
        [1 <= b[i+1] < y[i+1]]


===

######################
######################
######################
[b > 1][y >= 1]:
    [floor_log_(b;y) =[def]= if y < b then 0 else 1+floor_log_(b;y/b)]
    [floor_log_ex_(b;y) =[def]= if y < b then (y,0) else fmap (1+) floor_log_ex_(b;y/b)]
[kb > k][ky >= k][k >= 1]:
    [dfloor_log_(k;kb;ky) =[def]= if ky < kb then 0 else 1+dfloor_log_(k;kb;floor(k*ky/kb))]
    [ufloor_log_(k;kb;ky) =[def]= if ky < kb then 0 else 1+ufloor_log_(k;kb;ceil(k*ky/kb))]

    [dfloor_log_ex_(k;kb;ky) =[def]= if ky < kb then (ky,0) else fmap (1+) dfloor_log_ex_(k;kb;floor(k*ky/kb))]
    [ufloor_log_ex_(k;kb;ky) =[def]= if ky < kb then (ky,0) else fmap (1+) ufloor_log_ex_(k;kb;ceil(k*ky/kb))]
######################
proof_termination_of_dfloor_log_
proof termination of dfloor_log_
    [k >= 1]
    [kb > k]
    [ky >= k]
    * [1 <= k <= ky < kb]:
        stop
    * [1 <= k < kb <= ky][new_ky := floor(k*ky/kb)]:
        [kb <= ky]
        [k*kb <= k*ky]
        [k <= k*ky/kb]
        [k <= floor(k*ky/kb) == new_ky]
        [1 <= k <= new_ky]
        ####################
        [old_ky := ky]
        [old_ky >= kb > k >= 1]
        [old_ky >= 2]
        !! [k < kb]
        [k/kb < 1]
        [old_ky*(k/kb) < old_ky]
        [new_ky <= k*old_ky/kb < old_ky]
        !! [1 <= k <= new_ky]
        !! [new_ky < old_ky]
        !! [new_ky, old_ky :: int]
        [will terminate]
        ######################

######################
proof_termination_of_ufloor_log_
proof termination of ufloor_log_
    [k >= 1]
    [kb > k]
    [ky >= k]
    * [1 <= k <= ky < kb]:
        stop
    * [1 <= k < kb <= ky][new_ky := ceil(k*ky/kb)]:
        [kb <= ky]
        [k*kb <= k*ky]
        [k <= k*ky/kb]
        [k <= ceil(k*ky/kb) == new_ky]
        [1 <= k <= new_ky]
        ####################
        [old_ky := ky]
        [old_ky >= kb > k >= 1]
        !! [new_ky := ceil(k*ky/kb)]
        [new_ky == ceil(k*old_ky/kb) == floor((k*old_ky-1)/kb) +1]
        [new_ky >= old_ky]:
            [floor((k*old_ky-1)/kb) +1 >= old_ky]
            [(k*old_ky-1)/kb >= old_ky-1]
            [(k*old_ky-1) >= old_ky*kb -kb]
            [(kb-1) >= old_ky*(kb-k) >= old_ky*1]
            [kb > old_ky]
            !! [old_ky >= kb]
            _L
        [new_ky < old_ky]

        !! [1 <= k <= new_ky]
        !! [new_ky < old_ky]
        !! [new_ky, old_ky :: int]
        [will terminate]
        ####################
######################
######################
######################
# vs:
#   floor_log_(b;y)
#   dfloor_log_(k;k*b;k*y)
#   ufloor_log_(k;k*b;k*y)
######################
[floor_log_(b;y) <= floor_log_(b;y+1)]
[dfloor_log_(k;kb;ky) <= dfloor_log_(k;kb;ky+1)]
[ufloor_log_(k;kb;ky) <= ufloor_log_(k;kb;ky+1)]
######################
[floor_log_(b+1;y) <= floor_log_(b;y)]
[dfloor_log_(k;kb+1;ky) <= dfloor_log_(k;kb;ky)]
[ufloor_log_(k;kb+1;ky) <= ufloor_log_(k;kb;ky)]
######################
[dfloor_log_(k;k*b;k*y) <= floor_log_(b;y)]
    # induction:
    [dfloor_log_(k;k*b;floor(k*k*y/kb)) <= floor_log_(b;floor(k*k*y/kb)/k) <= floor_log_(b;(k*k*y/kb)/k) == floor_log_(b;y/b)]
######################
[ufloor_log_(k;k*b;k*y) >= floor_log_(b;y)]
    # induction:
    [ufloor_log_(k;k*b;ceil(k*k*y/kb)) >= floor_log_(b;ceil(k*k*y/kb)/k) >= floor_log_(b;(k*k*y/kb)/k) == floor_log_(b;y/b)]
######################
######################
######################
[snd floor_log_ex_(b;y) == floor_log_(b;y)]
[snd dfloor_log_ex_(k;kb;ky) == dfloor_log_(k;kb;ky)]
[snd ufloor_log_ex_(k;kb;ky) == ufloor_log_(k;kb;ky)]
######################
[1 <= fst floor_log_ex_(b;y) < b]
    『1 <= ...』<<==:
    [y >= b]:
        [(y/b) >= 1]
[k <= fst dfloor_log_ex_(k;kb;ky) < kb]
[k <= fst ufloor_log_ex_(k;kb;ky) < kb]
    『k <= ...』<<==:
    [ky >= kb]:
        [floor(k*ky/kb) >= floor(k*kb/kb) == k]
        [ceil(k*ky/kb) >= ceil(k*kb/kb) == k]
######################
######################
[[kb >= k*b] -> [ky <= k*y] -> [dfloor_log_(k;kb;ky) <= floor_log_(b;y)]]
    !! [dfloor_log_(k;kb+1;ky) <= dfloor_log_(k;kb;ky)]
    !! [dfloor_log_(k;kb;ky) <= dfloor_log_(k;kb;ky+1)]
    !! [dfloor_log_(k;k*b;k*y) <= floor_log_(b;y)]
######################
[[kb <= k*b] -> [ky >= k*y] -> [ufloor_log_(k;kb;ky) >= floor_log_(b;y)]]
    !! [ufloor_log_(k;kb+1;ky) <= ufloor_log_(k;kb;ky)]
    !! [ufloor_log_(k;kb;ky) <= ufloor_log_(k;kb;ky+1)]
    !! [ufloor_log_(k;k*b;k*y) >= floor_log_(b;y)]
######################
[[(lb_,le) := dfloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb >= k*b] -> [ky <= k*y] -> [le <= e]]
    !!v[[kb >= k*b] -> [ky <= k*y] -> [dfloor_log_(k;kb;ky) <= floor_log_(b;y)]]
######################
[[(gb_,ge) := ufloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb <= k*b] -> [ky >= k*y] -> [ge >= e]]
    !! [[kb <= k*b] -> [ky >= k*y] -> [ufloor_log_(k;kb;ky) >= floor_log_(b;y)]]
######################
[[(lb_,le) := dfloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb >= k*b] -> [ky <= k*y] -> [le == e] -> [lb_ <= k*b_]]
    [[proof:
    !! [floor_log_ex_(b;y) =[def]= if y < b then (y,0) else fmap (1+) floor_log_ex_(b;y/b)]
    !! [dfloor_log_ex_(k;kb;ky) =[def]= if ky < kb then (ky,0) else fmap (1+) dfloor_log_ex_(k;kb;floor(k*ky/kb))]
    #induction:
    * [le == e == 0]:
        [lb_ == ky <= k*y == k*b_]
    * [le == e >= 1]:
        [y >= b]
        [ky >= kb]
        !! [kb >= k*b][ky <= k*y]
        [ky*k*b <= k*y*kb]
        [ky/kb <= y/b]
        [(k*ky/kb) <= k*(y/b)]
        [floor(k*ky/kb) <= k*(y/b)]
        ...recur apply induction...
    DONE
    ]]

######################
[[(gb_,ge) := ufloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb <= k*b] -> [ky >= k*y] -> [ge == e] -> [gb_ >= k*b_]]
    [[proof:
    !! [floor_log_ex_(b;y) =[def]= if y < b then (y,0) else fmap (1+) floor_log_ex_(b;y/b)]
    !! [ufloor_log_ex_(k;kb;ky) =[def]= if ky < kb then (ky,0) else fmap (1+) ufloor_log_ex_(k;kb;ceil(k*ky/kb))]
    #induction:
    * [ge == e == 0]:
        [gb_ == ky >= k*y == k*b_]
    * [ge == e >= 1]:
        [y >= b]
        [ky >= kb]
        !! [kb <= k*b][ky >= k*y]
        [ky*k*b >= k*y*kb]
        [ky/kb >= y/b]
        [(k*ky/kb) >= k*(y/b)]
        [ceil(k*ky/kb) >= k*(y/b)]
        ...recur apply induction...
    DONE
    ]]

######################
######################
######################
######################

===

[1 < b < y]:
    [y[0] := y]
    [b[0] := b]
    [1 < b[0] < y[0]]
    [1 <= b[i] < y[i]]
    * [b[i] == 1]:
        #stop
        [cf[i:] = [+oo]*inf]
    * [b[i] > 1]:
        [(b[i+1], cf[i]) := floor_log_ex_(b[i];y[i])]
        [1 <= b[i+1] < b[i]]
        [y[i+1] := b[i]]
        [1 <= b[i+1] < y[i+1]]


===


[1 < b < y][k >= 1]:
    ############
    [y[0] := y]
    [b[0] := b]
    [1 < b[0] < y[0]]
    [1 <= b[2*i] < y[2*i]]

    ############
    #le
    [lky[0] := k*y]
    [lkb[0] := k*b]
    [lkb[0] >= k*b[0]]
    [lky[0] <= k*y[0]]
    [k < lkb[0] < lky[0]]
    [k <= lkb[2*i] < lky[2*i]]

    ############
    #ge
    [gky[0] := k*y]
    [gkb[0] := k*b]
    [gkb[0] <= k*b[0]]
    [gky[0] >= k*y[0]]
    [k < gkb[0] < gky[0]]
    [k <= gkb[2*i] < gky[2*i]]










    ############
    ############
    [lcf[2*i] := dfloor_log_(k;lkb[2*i];lky[2*i])]
    [gcf[2*i] := ufloor_log_(k;gkb[2*i];gky[2*i])]

    # swith d/u --> u/d
    [lcf[2*i+1] := ufloor_log_(k;lkb[2*i+1];lky[2*i+1])]
    [gcf[2*i+1] := dfloor_log_(k;gkb[2*i+1];gky[2*i+1])]



    ############
    ############
    [1 <= b[2*i] < y[2*i]]
    * [b[2*i] == 1]:
        #stop
        [cf[2*i:] = [+oo]*inf]
    * [b[2*i] > 1]:
        [(b[2*i+1], cf[2*i]) := floor_log_ex_(b[2*i];y[2*i])]
        [1 <= b[2*i+1] < b[2*i]]
        [y[2*i+1] := b[2*i]]
        [1 <= b[2*i+1] < y[2*i+1]]

    ############
    [k <= lkb[2*i] < lky[2*i]]
    * [lkb[2*i] == k]:
        #stop
        [lcf[2*i:] = [+oo]*inf]
    * [lkb[2*i] > k]:
        [(lkb[2*i+1], lcf[2*i]) := dfloor_log_ex_(k;lkb[2*i];lky[2*i])]
        [k <= lkb[2*i+1] < lkb[2*i]]
        [lky[2*i+1] := lkb[2*i]]
        [k <= lkb[2*i+1] < lky[2*i+1]]

    ############
    [k <= gkb[2*i] < gky[2*i]]
    * [gkb[2*i] == k]:
        #stop
        [gcf[2*i:] = [+oo]*inf]
    * [gkb[2*i] > k]:
        [(gkb[2*i+1], gcf[2*i]) := ufloor_log_ex_(k;gkb[2*i];gky[2*i])]
        [k <= gkb[2*i+1] < gkb[2*i]]
        [gky[2*i+1] := gkb[2*i]]
        [k <= gkb[2*i+1] < gky[2*i+1]]





    ############
    ############
    [1 <= b[2*i+1] < y[2*i+1]]
    * [b[2*i+1] == 1]:
        #stop
        [cf[2*i+1:] = [+oo]*inf]
    * [b[2*i+1] > 1]:
        [(b[2*(i+1)], cf[2*i+1]) := floor_log_ex_(b[2*i+1];y[2*i+1])]
        [1 <= b[2*(i+1)] < b[2*i+1]]
        [y[2*(i+1)] := b[2*i+1]]
        [1 <= b[2*(i+1)] < y[2*(i+1)]]

    ############
    [k <= lkb[2*i+1] < lky[2*i+1]]
    * [lkb[2*i+1] == k]:
        #stop
        [lcf[2*i+1:] = [+oo]*inf]
    * [lkb[2*i+1] > k]:
        [(lkb[2*(i+1)], lcf[2*i+1]) := ufloor_log_ex_(k;lkb[2*i+1];lky[2*i+1])]
            # d --> u
        [k <= lkb[2*(i+1)] < lkb[2*i+1]]
        [lky[2*(i+1)] := lkb[2*i+1]]
        [k <= lkb[2*(i+1)] < lky[2*(i+1)]]

    ############
    [k <= gkb[2*i+1] < gky[2*i+1]]
    * [gkb[2*i+1] == k]:
        #stop
        [gcf[2*i+1:] = [+oo]*inf]
    * [gkb[2*i+1] > k]:
        [(gkb[2*(i+1)], gcf[2*i+1]) := dfloor_log_ex_(k;gkb[2*i+1];gky[2*i+1])]
            # u --> d
        [k <= gkb[2*(i+1)] < gkb[2*i+1]]
        [gky[2*(i+1)] := gkb[2*i+1]]
        [k <= gkb[2*(i+1)] < gky[2*(i+1)]]


    ############
    ############
===
#vs: cf, lcf, gcf

[[lcf[:2*i] == cf[:2*i]] -> [[lkb[2*i] >= k*b[2*i]][lky[2*i] <= k*y[2*i]][lcf[2*i] <= cf[2*i]]]]
[[lcf[:2*i+1] == cf[:2*i+1]] -> [[lkb[2*i+1] <= k*b[2*i+1]][lky[2*i+1] >= k*y[2*i+1]][lcf[2*i+1] >= cf[2*i+1]]]]
    [[proof:the above 2:
    by induction:
    ######################
    * [n==2*i][i==0]:
        [lkb[0] >= k*b[0]]
        [lky[0] <= k*y[0]]
        !! [dfloor_log_(k;kb;ky) <= dfloor_log_(k;kb;ky+1)]
        !! [dfloor_log_(k;kb+1;ky) <= dfloor_log_(k;kb;ky)]
        [dfloor_log_(k;lkb[0];lky[0]) <= dfloor_log_(k;k*b[0];k*y[0])]

        !! [dfloor_log_(k;k*b;k*y) <= floor_log_(b;y)]
        [dfloor_log_(k;lkb[0];lky[0]) <= dfloor_log_(k;k*b[0];k*y[0]) <= floor_log_(b[0];y[0])]

        !! [(b[2*i+1], cf[2*i]) := floor_log_ex_(b[2*i];y[2*i])]
        !! [(lkb[2*i+1], lcf[2*i]) := dfloor_log_ex_(k;lkb[2*i];lky[2*i])]
        [lcf[0] <= cf[0]]

        ==>> [[lkb[0] >= k*b[0]][lky[0] <= k*y[0]][lcf[0] <= cf[0]]]
        ==>> [[lkb[2*i] >= k*b[2*i]][lky[2*i] <= k*y[2*i]][lcf[2*i] <= cf[2*i]]]

    ######################
    ######################
    * [n==2*i+1][i>=0][[lkb[2*i] >= k*b[2*i]][lky[2*i] <= k*y[2*i]][lcf[2*i] <= cf[2*i]]][lcf[:2*i+1] == cf[:2*i+1]]:
        !! [lcf[:2*i+1] == cf[:2*i+1]]
        [lcf[2*i] == cf[2*i]]

        !! [[(lb_,le) := dfloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb >= k*b] -> [ky <= k*y] -> [le == e] -> [lb_ <= k*b_]]
        !! [(b[2*i+1], cf[2*i]) := floor_log_ex_(b[2*i];y[2*i])]
        !! [(lkb[2*i+1], lcf[2*i]) := dfloor_log_ex_(k;lkb[2*i];lky[2*i])]
        !! [lkb[2*i] >= k*b[2*i]]
        !! [lky[2*i] <= k*y[2*i]]
        !! [lcf[2*i] == cf[2*i]]
        [lkb[2*i+1] <= k*b[2*i+1]]



        !! [lkb[2*i] >= k*b[2*i]]
        !! [y[2*i+1] := b[2*i]]
        !! [lky[2*i+1] := lkb[2*i]]
        [lky[2*i+1] >= k*y[2*i+1]]



        !! [[(gb_,ge) := ufloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb <= k*b] -> [ky >= k*y] -> [ge >= e]]
        !! [(b[2*(i+1)], cf[2*i+1]) := floor_log_ex_(b[2*i+1];y[2*i+1])]
        !! [(lkb[2*(i+1)], lcf[2*i+1]) := ufloor_log_ex_(k;lkb[2*i+1];lky[2*i+1])]
        !! [lkb[2*i+1] <= k*b[2*i+1]]
        !! [lky[2*i+1] >= k*y[2*i+1]]
        [lcf[2*i+1] >= cf[2*i+1]]


        ==>> [[lkb[2*i+1] <= k*b[2*i+1]][lky[2*i+1] >= k*y[2*i+1]][lcf[2*i+1] >= cf[2*i+1]]]

    ######################
    ######################
    * [n==2*(i+1)][i>=0][[lkb[2*i+1] <= k*b[2*i+1]][lky[2*i+1] >= k*y[2*i+1]][lcf[2*i+1] >= cf[2*i+1]]][lcf[:2*(i+1)] == cf[:2*(i+1)]]:
        !! [lcf[:2*(i+1)] == cf[:2*(i+1)]]
        [lcf[:2*i+1] == cf[:2*i+1]]

        !! [[(gb_,ge) := ufloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb <= k*b] -> [ky >= k*y] -> [ge == e] -> [gb_ >= k*b_]]
        !! [(b[2*(i+1)], cf[2*i+1]) := floor_log_ex_(b[2*i+1];y[2*i+1])]
        !! [(lkb[2*(i+1)], lcf[2*i+1]) := ufloor_log_ex_(k;lkb[2*i+1];lky[2*i+1])]
        !! [lkb[2*i+1] <= k*b[2*i+1]]
        !! [lky[2*i+1] >= k*y[2*i+1]]
        [lkb[2*(i+1)] >= k*b[2*(i+1)]]


        !! [lkb[2*i+1] <= k*b[2*i+1]]
        !! [y[2*(i+1)] := b[2*i+1]]
        !! [lky[2*(i+1)] := lkb[2*i+1]]
        [lky[2*(i+1)] <= y[2*(i+1)]]



        !! [[(lb_,le) := dfloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb >= k*b] -> [ky <= k*y] -> [le <= e]]
        !! [(b[2*i+1], cf[2*i]) := floor_log_ex_(b[2*i];y[2*i])]
        !! [(lkb[2*i+1], lcf[2*i]) := dfloor_log_ex_(k;lkb[2*i];lky[2*i])]
        !! [lkb[2*(i+1)] >= k*b[2*(i+1)]]
        !! [lky[2*(i+1)] <= k*y[2*(i+1)]]
        [lcf[2*(i+1)] <= cf[2*(i+1)]]


        ==>> [[lkb[2*(i+1)] >= k*b[2*(i+1)]][lky[2*(i+1)] <= k*y[2*(i+1)]][lcf[2*(i+1)] <= cf[2*(i+1)]]]
        ==>> [[lkb[2*i] >= k*b[2*i]][lky[2*i] <= k*y[2*i]][lcf[2*i] <= cf[2*i]]]
    ######################
    ######################

    DONE
    ]]
==>>:
[[lcf[:2*i] == cf[:2*i]] -> [lcf[2*i] <= cf[2*i]]]
[[lcf[:2*i+1] == cf[:2*i+1]] -> [lcf[2*i+1] >= cf[2*i+1]]]


===

[[gcf[:2*i] == cf[:2*i]] -> [[gkb[2*i] <= k*b[2*i]][gky[2*i] >= k*y[2*i]][gcf[2*i] >= cf[2*i]]]]
[[gcf[:2*i+1] == cf[:2*i+1]] -> [[gkb[2*i+1] >= k*b[2*i+1]][gky[2*i+1] <= k*y[2*i+1]][gcf[2*i+1] <= cf[2*i+1]]]]
    proof:vivi-above
==>>:
[[gcf[:2*i] == cf[:2*i]] -> [gcf[2*i] >= cf[2*i]]]
[[gcf[:2*i+1] == cf[:2*i+1]] -> [gcf[2*i+1] <= cf[2*i+1]]]

===
===
[lcf <= cf]
    !! [[lcf[:2*i] == cf[:2*i]] -> [lcf[2*i] <= cf[2*i]]]
    !! [[lcf[:2*i+1] == cf[:2*i+1]] -> [lcf[2*i+1] >= cf[2*i+1]]]
===
[gcf >= cf]
    !! [[gcf[:2*i] == cf[:2*i]] -> [gcf[2*i] >= cf[2*i]]]
    !! [[gcf[:2*i+1] == cf[:2*i+1]] -> [gcf[2*i+1] <= cf[2*i+1]]]
===
[lcf <= cf <= gcf]
    !! [lcf <= cf]
    !! [gcf >= cf]
===
]]]

[[[
view others/数学/continued-fraction/continued_fraction_of_log2_X.txt

/sdcard/0my_files/book/math/continued_fraction/On Shanks algorithm for computing the continued fraction of log_b_a(2002)(Terence).pdf
===
https://cs.uwaterloo.ca/journals/JIS/VOL5/Jackson/matthews3.html
  wget_U 'https://cs.uwaterloo.ca/journals/JIS/VOL5/Jackson/matthews3.pdf' -O 'On Shanks algorithm for computing the continued fraction of log_b_a(2002)(Terence).pdf'
  Abstract: We give a more practical variant of Shanks' 1954 algorithm for computing the continued fraction of log_b a, for integers a > b > 1, using the floor and ceiling functions and an integer parameter c > 1. The variant, when repeated for a few values of c = 10^r, enables one to guess if log_b a is rational and to find approximately r partial quotients.


]]]












py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   ,iter_continued_fraction_of_log__truncated_ =100  =2  =3



py_adhoc_call   script.log_b_y   ,iter_continued_fraction_of_log__truncated_ ='1<<10000'  =2  =3 > /sdcard/0my_files/tmp/out4py/script.log_b_y..1p10000-2-3.out.txt
view  /sdcard/0my_files/tmp/out4py/script.log_b_y..1p10000-2-3.out.txt
[[total 2943:cf_log_(2;3)[2938-1]==19
1
1
1
2
2
3
1
5
2
23
2
2
1
1
55
1
... ...
... ...
3
3
25
1
19
1
2
1
2
1
]]



######################
######################
######################
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 3)]
[1, 1, 1, 2, 2]
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 5)]
[2, 3]
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 7)]
[2, 1, 4]
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 11)]
[3, 2, 5, 1]
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 13)]
[3, 1, 2]
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 17)]
[4, 11, 2]
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 19)]
[4, 4]
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 23)]
[4, 1, 1]
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 29)]
[4, 1, 6]
>>> [*iter_continued_fraction_of_log__truncated_(1<<10, 2, 31)]
[4, 1]




######################
######################
######################
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 3)]
[1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1, 15, 1, 9, 2, 5, 7, 1, 1, 4]
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 5)]
[2, 3, 9, 2, 2, 4, 6, 2, 1, 1, 3, 1, 18, 1, 6, 1, 2, 1, 1, 4, 1, 42, 6, 1, 4, 2, 3, 1, 2, 6, 1]
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 7)]
[2, 1, 4, 5, 4, 5, 4, 1, 29, 1, 4, 8, 1, 1, 2, 1, 31, 10, 1, 2, 2, 6, 2, 3, 1, 1]
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 11)]
[3, 2, 5, 1, 1, 1, 25, 1, 1, 2, 3, 25, 3, 1, 6, 7, 1, 1, 1, 11, 9, 8, 2, 1, 2, 3, 3, 4, 2, 1, 1]
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 13)]
[3, 1, 2, 2, 1, 22, 23, 1, 9, 149, 1, 2, 1, 9, 1, 91, 3, 3, 10, 2, 1, 1, 5, 4]
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 17)]
[4, 11, 2, 3, 3, 1, 11, 8, 1, 215, 4, 2, 7, 1, 4, 3, 16, 1, 25, 1, 1, 4, 1, 14]
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 19)]
[4, 4, 29, 1, 9, 1, 3, 15, 1, 1, 45, 1, 1, 1, 9, 4, 2, 4, 1, 1, 1, 1, 71, 1, 6]
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 23)]
[4, 1, 1, 10, 9, 15, 1, 1, 2, 2, 10, 2, 1, 32, 1, 9, 1, 2, 10, 1, 1, 1, 1, 8, 1, 5, 1, 6]
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 29)]
[4, 1, 6, 24, 4, 1, 5, 3, 3, 1, 4, 1, 2, 3, 180, 1, 83, 5, 1, 9, 12, 1]
>>> [*iter_continued_fraction_of_log__truncated_(1<<100, 2, 31)]
[4, 1, 20, 1, 4, 1, 26, 9, 7, 3, 2, 1, 1, 1, 1, 5, 4, 3, 1, 1, 1, 2, 1, 5, 1, 1, 1, 1, 1, 3, 11, 4, 1, 1]


######################
######################
######################
>>> sz_ = lambda nbits, b, y, /: len([*iter_continued_fraction_of_log__truncated_(1<<nbits, b, y)])
>>> szs_ = lambda max_nbits, b, y, /: [sz_(nbits, b, y) for nbits in range(max_nbits+1)]

>>> szs_(100, 2, 3) #doctest: +SKIP
[0, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11, 11, 11, 12, 12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14, 14, 14, 14, 16, 16, 16, 16, 17, 17, 17, 18, 18, 18, 18, 20, 20, 20, 20, 20, 20, 20, 20, 22, 22, 22, 22, 22, 23, 23, 23, 24, 24, 24, 24, 24, 25, 25, 25, 25, 26, 26, 26, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29]
>>> from collections import Counter
>>> cszs_ = lambda max_nbits, b, y, /: (sorted((d:=Counter(szs_(max_nbits, b,y))).items()), Counter(d.values()).most_common())
>>> mcszs_ = lambda max_nbits, b, y, /: cszs_(max_nbits, b,y)[-1]
>>> mcszs_(100, 2, 3) #doctest: +SKIP
[(3, 7), (6, 5), (5, 3), (4, 3), (1, 2), (2, 2), (9, 1), (8, 1)]

>>> mcszs_(500, 2, 3) #doctest: +SKIP
[(3, 26), (5, 21), (4, 21), (1, 18), (6, 16), (2, 11), (7, 7), (8, 5), (9, 1)]
>>> mcszs_(500, 2, 7) #doctest: +SKIP
[(4, 23), (3, 20), (5, 14), (2, 12), (6, 11), (8, 8), (1, 7), (7, 5), (10, 5), (11, 3)]
>>> mcszs_(500, 2, 31) #doctest: +SKIP
[(3, 28), (4, 20), (2, 18), (5, 13), (8, 9), (6, 9), (1, 8), (7, 6), (9, 3), (10, 2), (13, 1)]
>>> mcszs_(500, 53, 101) #doctest: +SKIP
[(5, 20), (3, 16), (4, 16), (6, 14), (2, 14), (7, 10), (1, 7), (8, 6), (10, 3), (11, 2)]
>>> mcszs_(500, 2**19-1, 2**89-1) #doctest: +SKIP
[(3, 17), (6, 14), (4, 14), (5, 12), (2, 8), (1, 7), (7, 6), (8, 6), (9, 6), (10, 3), (15, 1), (13, 1), (14, 1), (11, 1)]

==>>:
most_common: 3bits per cf_digit


######################
######################
######################

py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   ,iter_continued_fraction_of_irrational_log_Fraction_  =3  =2  =27  =8
KeyboardInterrupt
==>>upperbound4failure_num_bits4k
==>>Error__continued_fraction_of_log__result_is_probably_rational
found bug:『default_num_bits4k = 1<<32』huge!!

######################
test rational result
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(3,2,27,8)]
[3]

######################
test iter_num_bits4k: no duplicate output between switch k
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(3,2,27,9, iter_num_bits4k=[10])]
[2, 1, 2, 2]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(3,2,27,9, iter_num_bits4k=[20])]
[2, 1, 2, 2, 3, 1, 5]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(3,2,27,9, iter_num_bits4k=[10, 20])]
[2, 1, 2, 2, 3, 1, 5]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(3,2,27,9, iter_num_bits4k=range(25)[::3])]
[2, 1, 2, 2, 3, 1, 5, 2]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(3,2,27,9, iter_num_bits4k=[24])]
[2, 1, 2, 2, 3, 1, 5, 2]


######################
test default_num_bits4k : expect 10 cf_digit
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(3,2,27,9, iter_num_bits4k=[default_num_bits4k])]
[2, 1, 2, 2, 3, 1, 5, 2, 23, 2]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(3,2,257,9, iter_num_bits4k=[default_num_bits4k])]
[8, 3, 1, 2, 1, 271, 1, 2, 1]

######################
######################
######################
######################
#]]]'''
__all__ = r'''

iter_continued_fraction_of_log_Fraction__truncated_
    iter_continued_fraction_of_log__truncated_
    iter_continued_fraction_of_irrational_log_Fraction_
        upperbound4num_bits4k
        upperbound4failure_num_bits4k
        mk_default_iter_num_bits4k
            default_num_bits4k
            default_grow_rateND4num_bits4k

iter_xbound_continued_fraction_of_log_
    dfloor_log_ex_
    ufloor_log_ex_

BaseError__continued_fraction_of_log
    Error__continued_fraction_of_log__result_is_probably_rational
    Error__continued_fraction_of_log__num_bits4k_too_big

'''.split()#'''


def __():
    # API:here
    iter_continued_fraction_of_log_Fraction__truncated_
        # finite truncated correct cf_digits
        # input are Fraction
    iter_continued_fraction_of_log__truncated_
        # finite truncated correct cf_digits
        # input are ints
    iter_continued_fraction_of_irrational_log_Fraction_
        # infinite non-truncated correct cf_digits
        #       # (if `kw:iter_num_bits4k` infinite and result is irrational)
        # input are Fraction
        # but when use bigger k to avoid truncate, it will regenerate all output, time consuming
        #
    def iter_continued_fraction_of_log_Fraction__truncated_(param4memory_consume, N4base, D4base, N4y, D4y, /):
        r'''[[[
    param4memory_consume -> N4base/int{>=1} -> D4base/int{>=1,<=N4base} -> N4y/int{>=1} -> D4y/int{>=1,<=N4y} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [base == N4base/D4base]
    [y == N4y/D4y]

    [[base==1] -> [cf == []/+oo]]
    StopIteration(sign_of(len lcf - len gcf))
        if StopIteration.value == 0:
            [lcf == cf == gcf]

    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    def iter_continued_fraction_of_log__truncated_(param4memory_consume, base, y, /):
        r'''[[[
    param4memory_consume -> base/int{>=1} -> y/int{>=1} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [[base==1] -> [cf == []/+oo]]
    StopIteration(sign_of(len lcf - len gcf))
        if StopIteration.value == 0:
            [lcf == cf == gcf]

    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    def iter_continued_fraction_of_irrational_log_Fraction_(N4base, D4base, N4y, D4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False):
        r'''[[[
    N4base/int{>=1} -> D4base/int{>=1,<=N4base} -> N4y/int{>=1} -> D4y/int{>=1,<=N4y} -> (iter_num_bits4k/(Iter param4memory_consume)=None) -> cf/iter continued_fraction_of_log_(base; y)[:?depends on iter_num_bits4k?]

    [base == N4base/D4base]
    [y == N4y/D4y]

    [[base==1] -> [cf == []/+oo]]
    StopIteration(may sign_of(len lcf - len gcf)) #(None|+1|-1|0)
        # None if no k
        if StopIteration.value == 0:
            [lcf == cf == gcf]


    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''


def __():
    i = 100000
    def _raise_():
        nonlocal i
        i -= 1
        if i <= 0:
            raise 000
    return _raise_
if 0b00:
    _raise_ = _()
else:
    def _raise_():
        pass


def dfloor_log_ex_(k, kb, ky, /):
    assert 1 <= k
    assert k < kb
    assert k <= ky
    # [k < kb]
    # [k <= ky]
    e = 0
    while not ky < kb:
        _raise_()
        # [k < kb <= ky]
        # [k < k*kb <= k*ky]
        # [k <= k*ky/kb]
        # [k <= k*ky//kb]
        new_ky = (k*ky)//kb
        assert new_ky < ky, (new_ky, ky, kb)
        ky = new_ky
        # [k <= ky]
        ######################
        # proof_termination_of_dfloor_log_
        # [old_ky >= kb > k >= 1]
        # [old_ky >= 2]
        # !! [k < kb]
        # [k/kb < 1]
        # [old_ky*(k/kb) < old_ky]
        # [new_ky <= k*old_ky/kb < old_ky] --> [not dead loop]
        # termination
        ######################
        e += 1
    # [k <= ky < kb]
    assert k <= ky < kb
    return ky, e


def ufloor_log_ex_(k, kb, ky, /):
    assert 1 <= k
    assert k < kb
    assert k <= ky
    # [k < kb]
    # [k <= ky]
    e = 0
    while not ky < kb:
        _raise_()
        # [k < kb <= ky]
        # [k < k*kb <= k*ky]
        # [k <= k*ky/kb]
        # [k <= ceil(k*ky/kb) == (k*ky-1)//kb +1]
        new_ky = (k*ky-1)//kb +1
        assert new_ky < ky, (new_ky, ky, kb)
        ky = new_ky
        # [k <= ky]
        ######################
        # proof_termination_of_ufloor_log_
        # [old_ky >= kb > k >= 1]
        # !! [new_ky := ceil(k*ky/kb)]
        # [new_ky == ceil(k*old_ky/kb) == floor((k*old_ky-1)/kb) +1]
        # [new_ky >= old_ky]:
        #   [floor((k*old_ky-1)/kb) +1 >= old_ky]
        #   [(k*old_ky-1)/kb >= old_ky-1]
        #   [(k*old_ky-1) >= old_ky*kb -kb]
        #   [(kb-1) >= old_ky*(kb-k) >= old_ky*1]
        #   [kb > old_ky]
        #   !! [old_ky >= kb]
        #   _L
        # [new_ky < old_ky]
        # [new_ky < old_ky] --> [not dead loop]
        # termination
        ######################
        e += 1
    # [k <= ky < kb]
    assert k <= ky < kb
    return ky, e

_fs = dfloor_log_ex_, ufloor_log_ex_
def iter_xbound_continued_fraction_of_log_(lower_vs_upper, k, kb, ky, /):
    assert type(lower_vs_upper) is bool
    assert 1 <= k
    assert k <= kb
    assert k <= ky
    fs = _fs
    while k < kb:
        _raise_()
        _kb, cf_digit = fs[lower_vs_upper](k, kb, ky)
        yield cf_digit
        kb, ky = _kb, kb
        lower_vs_upper = not lower_vs_upper
def iter_continued_fraction_of_log__truncated_(param4memory_consume, base, y, /):
    r'''[[[
    param4memory_consume -> base/int{>=1} -> y/int{>=1} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [[base==1] -> [cf == []/+oo]]
    StopIteration(sign_of(len lcf - len gcf))
        if StopIteration.value == 0:
            [lcf == cf == gcf]

    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    assert 1 <= param4memory_consume
    assert 1 <= base
    assert 1 <= y

    k = param4memory_consume
    kb = k*base
    ky = k*y
    assert 1 <= k
    assert k <= kb
    assert k <= ky
    if 1:
        return iter_continued_fraction_of_log_Fraction__truncated_(param4memory_consume, base, 1, y, 1)
    else:

        lcf = iter_xbound_continued_fraction_of_log_(False, k, kb, ky)
        gcf = iter_xbound_continued_fraction_of_log_(True, k, kb, ky)
        return _zip(lcf, gcf)

def _zip(lcf, gcf, /):
    #for a, b in zip(lcf, gcf):
    while 1:
        _raise_()
        a = next(lcf, ...)
        b = next(gcf, ...)
        if a is ...:
            if b is ...:
                # [lcf == cf == gcf]
                return 0 # len lcf == len gcf
            return -1 # len lcf < len gcf
        if b is ...:
            return +1 # len lcf > len gcf

        if a == b:
            yield a
        else:
            #truncate
            break

#null_iter = iter('')



def iter_continued_fraction_of_log_Fraction__truncated_(param4memory_consume, N4base, D4base, N4y, D4y, /):
    r'''[[[
    param4memory_consume -> N4base/int{>=1} -> D4base/int{>=1,<=N4base} -> N4y/int{>=1} -> D4y/int{>=1,<=N4y} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [base == N4base/D4base]
    [y == N4y/D4y]

    [[base==1] -> [cf == []/+oo]]
    StopIteration(sign_of(len lcf - len gcf))
        if StopIteration.value == 0:
            [lcf == cf == gcf]

    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    assert 1 <= param4memory_consume
    assert 1 <= D4base <= N4base
    assert 1 <= D4y <= N4y

    k = param4memory_consume
    gkb, r = divmod(k*N4base, D4base)
    lkb = gkb +(not r==0)

    lky, r = divmod(k*N4y, D4y)
    gky = lky +(not r==0)
    assert 1 <= k
    assert k <= gkb <= lkb
    assert k <= lky <= gky

    lcf = iter_xbound_continued_fraction_of_log_(False, k, lkb, lky)
    gcf = iter_xbound_continued_fraction_of_log_(True, k, gkb, gky)
    return _zip(lcf, gcf)



upperbound4num_bits4k = (1<<16) +1
#bug:default_num_bits4k = 1<<32
default_num_bits4k = 32
    #expect yield 10 cf_digit
    # most_common: 3bits per cf_digit
default_grow_rateND4num_bits4k = 3,2
def mk_default_iter_num_bits4k():
    nbits = default_num_bits4k
    N, D = default_grow_rateND4num_bits4k
    assert N > D
    while 1:
        _raise_()
        yield nbits
        nbits = (nbits*N-1)//D+1 #ceil
upperbound4failure_num_bits4k = (1<<8)+1
class BaseError__continued_fraction_of_log(Exception):pass
class Error__continued_fraction_of_log__result_is_probably_rational(BaseError__continued_fraction_of_log):pass
class Error__continued_fraction_of_log__num_bits4k_too_big(BaseError__continued_fraction_of_log):pass
def iter_continued_fraction_of_irrational_log_Fraction_(N4base, D4base, N4y, D4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False):
    r'''[[[
    N4base/int{>=1} -> D4base/int{>=1,<=N4base} -> N4y/int{>=1} -> D4y/int{>=1,<=N4y} -> (iter_num_bits4k/(Iter param4memory_consume)=None) -> cf/iter continued_fraction_of_log_(base; y)[:?depends on iter_num_bits4k?]

    [base == N4base/D4base]
    [y == N4y/D4y]

    [[base==1] -> [cf == []/+oo]]
    StopIteration(may sign_of(len lcf - len gcf)) #(None|+1|-1|0)
        # None if no k
        if StopIteration.value == 0:
            [lcf == cf == gcf]


    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    assert 1 <= D4base <= N4base
    assert 1 <= D4y <= N4y
    if iter_num_bits4k is None:
        iter_num_bits4k = mk_default_iter_num_bits4k()

    prev_total_cf_digits = 0
    prev_num_bits4k = -1
    prev_num_bits4k_which_yield_cf_digit = 0
    r = None
    for num_bits4k in iter_num_bits4k:
        _raise_()
        if not force4using_big_num_bits4k:
            if num_bits4k >= upperbound4num_bits4k: raise Error__continued_fraction_of_log__num_bits4k_too_big(num_bits4k)
        if not num_bits4k > prev_num_bits4k:raise ValueError
        prev_num_bits4k = num_bits4k

        k = 1<<num_bits4k
        it = iter_continued_fraction_of_log_Fraction__truncated_(k, N4base, D4base, N4y, D4y)
        try:
            i = 0
            while 1:
                _raise_()
                # [cf_digit == cf[i-1]]
                cf_digit = next(it)
                    # ^StopIteration
                    # [cf_digit == cf[i-1]]
                # [cf_digit == cf[i]]
                if i == prev_total_cf_digits:
                    # [cf_digit == cf[i]]
                    break
                # discard cf_digit since yielded before
                i += 1
                # [cf_digit == cf[i-1]]
            # [cf_digit == cf[i]]
            while 1:
                _raise_()
                # [cf_digit == cf[i]]
                yield cf_digit
                i += 1
                # [cf_digit == cf[i-1]]
                cf_digit = next(it)
                    # ^StopIteration
                    # [cf_digit == cf[i-1]]
                # [cf_digit == cf[i]]
        except StopIteration as e:
            # [cf_digit == cf[i-1]]
            r = e.value
        # [cf_digit == cf[i-1]]
        total_cf_digits = i
        if total_cf_digits < prev_total_cf_digits: raise 000

        elif prev_total_cf_digits < total_cf_digits:
            prev_total_cf_digits = total_cf_digits
            prev_num_bits4k_which_yield_cf_digit = num_bits4k
        else:
            if num_bits4k -prev_num_bits4k_which_yield_cf_digit >= upperbound4failure_num_bits4k: raise Error__continued_fraction_of_log__result_is_probably_rational(N4base, D4base, N4y, D4y)

        if r == 0:
            # [lcf == cf == gcf]
            # [cf is not irrational]
            break
            return 0
        # [lcf =!= gcf]
        # refine
        continue
        ...
    return r # (None|+1|-1|0)
        # None if no k






__all__


from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import dfloor_log_ex_, ufloor_log_ex_, iter_xbound_continued_fraction_of_log_, iter_continued_fraction_of_log__truncated_

from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import iter_continued_fraction_of_log__truncated_
from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import iter_continued_fraction_of_irrational_log_Fraction_
from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import iter_continued_fraction_of_log_Fraction__truncated_

from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import *
