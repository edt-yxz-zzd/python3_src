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





[[[
@20250107:search e4p s.t. p**e4p near 10**e4b enough #threshold4relative_error
===
main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_
vs:
    view ../../python3_src/seed/int_tools/digits/generic_base85.py
        # for n in range(2,48):print((n, (256**(n-1))**(1/n)))

===

py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   ,10:main4iter_continued_fraction_of_irrational_log_Fraction_ --cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs=1  =2  =3
Fraction(1, 1)
Fraction(2, 1)
Fraction(3, 2)
Fraction(8, 5)
Fraction(19, 12)
Fraction(65, 41)
Fraction(84, 53)
Fraction(485, 306)
Fraction(1054, 665)
Fraction(24727, 15601)
py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   @list.10:main4iter_continued_fraction_of_irrational_log_Fraction_ --cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs=0  =10  =3
[0, 2, 10, 2, 2, 1, 13, 1, 7, 18]
py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   ,10:main4iter_continued_fraction_of_irrational_log_Fraction_ --cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs=2  =10  =3
(0, 1)
(1, 2)
(10, 21)
(21, 44)
(52, 109)
(73, 153)
(1001, 2098)
(1074, 2251)
(8519, 17855)
(154416, 323641)

echo $[3**21]
10460353203
echo $[3**44]
7093466277004997233#bug:truncated:modulo 2**64
echo $[3**109]
6548406049418485331#bug:truncated:modulo 2**64
>>> 3**21
10460353203
>>> 3**44
984770902183611232881
>>> 3**109
10144175740568179028790664417176723510595582355545683
>>> 3**44%2**64
7093466277004997233
>>> 3**109%2**64
6548406049418485331


[4813 in cf_log_(10;7)[:10]]
    [is_prime(4813)]
py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   ,main4batch4iter_continued_fraction_of_irrational_log_Fraction_ --cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs=0 --size=10  =10  ='[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]'
(10, 2, [0, 3, 3, 9, 2, 2, 4, 6, 2, 1])
(10, 3, [0, 2, 10, 2, 2, 1, 13, 1, 7, 18])
(10, 5, [0, 1, 2, 3, 9, 2, 2, 4, 6, 2])
(10, 7, [0, 1, 5, 2, 5, 6, 1, 4813, 1, 1])
(10, 11, [1, 24, 6, 3, 2, 1, 1, 3, 1, 1])
(10, 13, [1, 8, 1, 3, 2, 7, 1, 6, 16, 1])
(10, 17, [1, 4, 2, 1, 17, 1, 3, 1, 1, 3])
(10, 19, [1, 3, 1, 1, 2, 2, 1, 3, 2, 2])
(10, 23, [1, 2, 1, 3, 4, 17, 2, 1, 2, 66])
(10, 29, [1, 2, 6, 6, 1, 2, 1, 2, 2, 2])
(10, 31, [1, 2, 28, 2, 3, 1, 2, 1, 1, 1])
(10, 37, [1, 1, 1, 3, 6, 25, 1, 3, 1, 2])
(10, 41, [1, 1, 1, 1, 1, 2, 1, 1, 8, 7])
(10, 43, [1, 1, 1, 1, 2, 1, 2, 7, 1, 5])
(10, 47, [1, 1, 2, 20, 8, 42, 11, 5, 1, 1])
(10, 53, [1, 1, 2, 1, 1, 1, 2, 8, 4, 6])
py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   ,main4batch4iter_continued_fraction_of_irrational_log_Fraction_ --cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs=2 --size=10  =10  ='[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]'
(10, 2, [(0, 1), (1, 3), (3, 10), (28, 93), (59, 196), (146, 485), (643, 2136), (4004, 13301), (8651, 28738), (12655, 42039)])
(10, 3, [(0, 1), (1, 2), (10, 21), (21, 44), (52, 109), (73, 153), (1001, 2098), (1074, 2251), (8519, 17855), (154416, 323641)])
(10, 5, [(0, 1), (1, 1), (2, 3), (7, 10), (65, 93), (137, 196), (339, 485), (1493, 2136), (9297, 13301), (20087, 28738)])
(10, 7, [(0, 1), (1, 1), (5, 6), (11, 13), (60, 71), (371, 439), (431, 510), (2074774, 2455069), (2075205, 2455579), (4149979, 4910648)])
(10, 11, [(1, 1), (25, 24), (151, 145), (478, 459), (1107, 1063), (1585, 1522), (2692, 2585), (9661, 9277), (12353, 11862), (22014, 21139)])
(10, 13, [(1, 1), (9, 8), (10, 9), (39, 35), (88, 79), (655, 588), (743, 667), (5113, 4590), (82551, 74107), (87664, 78697)])
(10, 17, [(1, 1), (5, 4), (11, 9), (16, 13), (283, 230), (299, 243), (1180, 959), (1479, 1202), (2659, 2161), (9456, 7685)])
(10, 19, [(1, 1), (4, 3), (5, 4), (9, 7), (23, 18), (55, 43), (78, 61), (289, 226), (656, 513), (1601, 1252)])
(10, 23, [(1, 1), (3, 2), (4, 3), (15, 11), (64, 47), (1103, 810), (2270, 1667), (3373, 2477), (9016, 6621), (598429, 439463)])
(10, 29, [(1, 1), (3, 2), (19, 13), (117, 80), (136, 93), (389, 266), (525, 359), (1439, 984), (3403, 2327), (8245, 5638)])
(10, 31, [(1, 1), (3, 2), (85, 57), (173, 116), (604, 405), (777, 521), (2158, 1447), (2935, 1968), (5093, 3415), (8028, 5383)])
(10, 37, [(1, 1), (2, 1), (3, 2), (11, 7), (69, 44), (1736, 1107), (1805, 1151), (7151, 4560), (8956, 5711), (25063, 15982)])
(10, 41, [(1, 1), (2, 1), (3, 2), (5, 3), (8, 5), (21, 13), (29, 18), (50, 31), (429, 266), (3053, 1893)])
(10, 43, [(1, 1), (2, 1), (3, 2), (5, 3), (13, 8), (18, 11), (49, 30), (361, 221), (410, 251), (2411, 1476)])
(10, 47, [(1, 1), (2, 1), (5, 3), (102, 61), (821, 491), (34584, 20683), (381245, 228004), (1940809, 1160703), (2322054, 1388707), (4262863, 2549410)])
(10, 53, [(1, 1), (2, 1), (5, 3), (7, 4), (12, 7), (19, 11), (50, 29), (419, 243), (1726, 1001), (10775, 6249)])

py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   ,main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_ =10  =10  ='[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]'
    #(params, idx6cf, approx_ND4logb_y)
((10, 10, 2), 2, (3, 10))
((10, 10, 3), 1, (1, 2))
((10, 10, 5), 3, (7, 10))
((10, 10, 7), 3, (11, 13))
((10, 10, 11), 0, (1, 1))
((10, 10, 13), 2, (10, 9))
((10, 10, 17), 3, (16, 13))
((10, 10, 19), 4, (23, 18))
((10, 10, 23), 3, (15, 11))
((10, 10, 29), 2, (19, 13))
((10, 10, 31), 1, (3, 2))
((10, 10, 37), 3, (11, 7))
((10, 10, 41), 5, (21, 13))
((10, 10, 43), 5, (18, 11))
((10, 10, 47), 2, (5, 3))
((10, 10, 53), 5, (19, 11))
py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   @list.main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_ =10  =10  ='[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]' --with_params__vs__without_params__vs__idx_only__vs__ND_only__vs__N_only__vs__D_only=2 #idx_only
    #cf_log_(b;y)[:1+idx6cf]
[2, 1, 3, 3, 0, 2, 3, 4, 3, 2, 1, 3, 5, 5, 2, 5]
py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   @list.main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_ =10  =10  ='[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]' --with_params__vs__without_params__vs__idx_only__vs__ND_only__vs__N_only__vs__D_only=5 #D_only
    #y**D#p**D
    #view others/数学/有递增趋势的非递增序列.txt
[10, 2, 10, 13, 1, 9, 13, 18, 11, 13, 2, 7, 13, 11, 3, 11]
py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   @list.main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_ =10  =10  ='[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]' --with_params__vs__without_params__vs__idx_only__vs__ND_only__vs__N_only__vs__D_only=4 #N_only
    #b**N#10**N
[3, 1, 7, 11, 1, 10, 16, 23, 15, 19, 3, 11, 21, 18, 5, 19]

1/threshold4relative_error:10-->100
py_adhoc_call   seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_   @list.main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_ =100  =10  ='[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]' --with_params__vs__without_params__vs__idx_only__vs__ND_only__vs__N_only__vs__D_only=3 #ND_only
    #b**N#10**N
    #y**D#p**D
[(28, 93), (73, 153), (65, 93), (60, 71), (151, 145), (88, 79), (16, 13), (78, 61), (64, 47), (136, 93), (173, 116), (69, 44), (50, 31), (49, 30), (102, 61), (50, 29)]

>>> 2**93
9903520314283042199192993792
>>> 10**28
10000000000000000000000000000
>>> 3**153
9989689095948428268966921126195809393034773710522520293009978943147202723
>>> 5**93
100974195868289511092701256356196637398170423693954944610595703125
>>> 17**13
9904578032905937
>>> 10**16
10000000000000000
>>> 41**31
99151561540870339022484588445237129558214701225241
>>> 43**30
10093776109231555797740541116805209814919811290249

===
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
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(3,2,27,8)] #2 cancelled by k=2**num_bits4k, this test is useless
[3]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(7,3,7**3,3**3)]
[3]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(7,3,7**3,3**3, to_detect_rational_result_when_troubleshooting=False)]
Traceback (most recent call last):
    ...
seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_.Error__continued_fraction_of_log__result_is_probably_rational: (7, 3, 343, 27)
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(12**6,7**6,12**10,7**10)]
[1, 1, 2]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(27*12**6,27*7**6,27*12**10,27*7**10)]
[1, 1, 2]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(4,2,8,1)]
[3]

######################
test rational result:gcd on exp
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(17*625**13,17*81**13,19*625**21,19*81**21)]
[1, 1, 1, 1, 1, 2]

######################
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(4,4,2,1)]
[]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(4,4,1,1)]
[]
>>> [*iter_continued_fraction_of_irrational_log_Fraction_(5,4,1,1)]
[0]

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
>>> [*iter_continued_fraction_of_irrational_ln_Fraction_(2, 1, iter_num_bits4k=[64])]
[0, 1, 2, 3, 1, 6, 3, 1, 1, 2, 1, 1, 1, 1, 3, 10, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 3, 1]

[[
view ../../python3_src/nn_ns/math_nn/numbers/A016730-continued_fraction_for_ln_2__fst_20000.txt

1 0
2 1
3 2
4 3
5 1
6 6
7 3
8 1
9 1
10 2
11 1
12 1
13 1
14 1
15 3
16 10
17 1
18 1
19 1
20 2
21 1
22 1
23 1
24 1
25 3
26 2
27 3
28 1
29 13
]]


######################
>>> (ln2 := cf_ln_(2))
ContinuedFraction(LazyList([<...>]))
>>> ln2[:30]
(0, 1, 2, 3, 1, 6, 3, 1, 1, 2, 1, 1, 1, 1, 3, 10, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 3, 1, 13, 7)
>>> ln2
ContinuedFraction(LazyList([0, 1, 2, 3, 1, 6, 3, 1, 1, 2, 1, 1, 1, 1, 3, 10, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 3, 1, 13, 7, <...>]))
>>> (ln_inv2 := cf_ln_((1,2)))
ContinuedFraction(LazyList([-1, 3, <...>]))
>>> ln_inv2[:30]
(-1, 3, 3, 1, 6, 3, 1, 1, 2, 1, 1, 1, 1, 3, 10, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 3, 1, 13, 7, 4)
>>> (cf := cf_log_((1,4), (9*8, 9)))
ContinuedFraction(LazyList([-2, 1, 1, <...>]))
>>> cf[:10]
(-2, 1, 1)
>>> cf
ContinuedFraction(LazyList([-2, 1, 1]))

######################
######################
######################
#]]]'''
__all__ = r'''

iter_continued_fraction_of_log_Fraction__truncated_
    iter_continued_fraction_of_log__truncated_
    iter_continued_fraction_of_irrational_log_Fraction_
        default_upperbound4num_bits4k
        default_upperbound4failure_num_bits4k
        mk_default_iter_num_bits4k
            default_num_bits4k
            default_grow_rateND4num_bits4k

iter_xbound_continued_fraction_of_log_
    dfloor_log_ex_
    ufloor_log_ex_

detect_rational_log__pint_
    detect_rational_log__Fraction_

BaseError__continued_fraction_of_log
    Error__log__base_eq_1
    Error__continued_fraction_of_log__result_is_probably_rational
    Error__continued_fraction_of_log__num_bits4k_too_big



iter_continued_fraction_of_log_Fraction_interval__truncated_
    iter_continued_fraction_of_irrational_log_cf_
        iter_continued_fraction_of_irrational_ln_cf_
            iter_continued_fraction_of_irrational_ln_Fraction_


cf_log_
    convert_to_ContinuedFraction_
    cf_ln_
    cf_log2_


main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_
    main4until4iter_continued_fraction_of_irrational_log_Fraction_
main4batch4iter_continued_fraction_of_irrational_log_Fraction_
    main4iter_continued_fraction_of_irrational_log_Fraction_
    mk_ND5or_rational_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.math.floor_ceil import perfect_div, perfect_kth_root_, NotPerfectError__kth_root
from seed.math.floor_ceil import floor_div, ceil_div
from seed.math.floor_ceil import floor_log2, ceil_log2
from seed.math.continued_fraction.continued_fraction5ND import iter_continued_fraction_digits5ND_
from seed.math.gcd import gcd_ex, gcd
from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
from seed.tiny_.iter_stop_with_ import iter_stop_with_, GetStopIterationValue
from seed.math.continued_fraction.continued_fraction_fold import iter_approximate_fraction_NDs5continued_fraction_
from seed.types.LazyList import LazyList
from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import raw_iter_cf_digits4e_the_natural_logarithm_base_
from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import ContinuedFraction, cf_0, cf_1, cf_neg1
from seed.tiny import is_iterator

from itertools import islice
from numbers import Rational

___end_mark_of_excluded_global_names__0___ = ...

def __():
    # API:here
    ######################
    iter_continued_fraction_of_log_Fraction__truncated_
        # input: fraction/(N,D)
        # output: finite truncated correct cf_digits
    iter_continued_fraction_of_log__truncated_
        # input: int
        # others see:above
    iter_continued_fraction_of_log_Fraction_interval__truncated_
        # input: fraction_interval/(N4min,D4min,N4max,D4max)
        # others see:above
    ######################

    detect_rational_log__pint_
    detect_rational_log__Fraction_


    ######################
    iter_continued_fraction_of_irrational_log_Fraction_
        # input: fraction/(N,D)
        # output: infinite non-truncated correct cf_digits
        #       # (if `kw:iter_num_bits4k` infinite and result is irrational)
        # but when use bigger k to avoid truncate, it will regenerate all output, time consuming
        #
    iter_continued_fraction_of_irrational_log_cf_
        # input: continued_fraction/Iter int{>=1}
        # others see:above
    iter_continued_fraction_of_irrational_ln_cf_
        # input: continued_fraction/Iter int{>=1}
        # base is e--the_natural_logarithm_base
        # others see:above
    iter_continued_fraction_of_irrational_ln_Fraction_
        # input: fraction/(N,D)
        # base is e--the_natural_logarithm_base
        # others see:above
    ######################
    cf_log_
        # input: cf_like/(Rational|(N,D)|[int]|(Iterator int)|(LazyList int)|ContinuedFraction)
        # output: ContinuedFraction
        # diff iter_continued_fraction_of_irrational_log_cf_: allow:[0<base<1][0<y<1] but forbid:[base==1]
        # others see:iter_continued_fraction_of_irrational_log_cf_
    cf_ln_
        # base is e--the_natural_logarithm_base
        # others see:above
    cf_log2_
        # base is 2
        # others see:above

    def iter_continued_fraction_of_log_Fraction__truncated_(param4memory_consume, N4base, D4base, N4y, D4y, /):
        r'''[[[
    param4memory_consume -> N4base/int{>=1} -> D4base/int{>=1,<=N4base} -> N4y/int{>=1} -> D4y/int{>=1,<=N4y} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [base == N4base/D4base]
    [y == N4y/D4y]

    [[base==1] -> [cf == []/+oo]]
    StopIteration((emay_sign, emay lcf_digit, emay gcf_digit))
        if emay_sign == 0:
            [lcf == cf == gcf]

    [emay_sign == ...|sign_of(len lcf - len gcf)]
    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    def iter_continued_fraction_of_log__truncated_(param4memory_consume, base, y, /):
        r'''[[[
    param4memory_consume -> base/int{>=1} -> y/int{>=1} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [[base==1] -> [cf == []/+oo]]
    StopIteration((emay_sign, emay lcf_digit, emay gcf_digit))
        if emay_sign == 0:
            [lcf == cf == gcf]

    [emay_sign == ...|sign_of(len lcf - len gcf)]
    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    def iter_continued_fraction_of_irrational_log_Fraction_(N4base, D4base, N4y, D4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False):
        r'''[[[
    N4base/int{>=1} -> D4base/int{>=1,<=N4base} -> N4y/int{>=1} -> D4y/int{>=1,<=N4y} -> (iter_num_bits4k/(Iter param4memory_consume)=None) -> cf/iter continued_fraction_of_log_(base; y)[:?depends on iter_num_bits4k?]

    [base == N4base/D4base]
    [y == N4y/D4y]

    [[base==1] -> [cf == []/+oo]]
    StopIteration(emay (emay_sign, emay lcf_digit, emay gcf_digit))
        ... if no k
        if emay_sign == 0:
            [lcf == cf == gcf]

    [emay_sign == ...|sign_of(len lcf - len gcf)]
    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''

    ######################

    def iter_continued_fraction_of_log_Fraction_interval__truncated_(param4memory_consume, N4min_base, D4min_base, N4max_base, D4max_base, N4min_y, D4min_y, N4max_y, D4max_y, /):
        r'''[[[
        param4memory_consume -> N4min_base/int{>=1} -> D4min_base/int{>=1,<=N4min_base} -> N4max_base/int{>=1} -> D4max_base/int{>=1,<=N4max_base} -> N4min_y/int{>=1} -> D4min_y/int{>=1,<=N4min_y} -> N4max_y/int{>=1} -> D4max_y/int{>=1,<=N4max_y} -> cf/iter continued_fraction_of_log_(base; y)[:?]

        [N4min_base/D4min_base == min_base <= base <= max_base == N4max_base/D4max_base]
        [N4min_y/D4min_y == min_y <= y <= max_y == N4max_y/D4max_y]

        [[base==1] -> [cf == []/+oo]]
        StopIteration((emay_sign, emay lcf_digit, emay gcf_digit))
            if emay_sign == 0:
                [lcf == cf == gcf]

        [emay_sign == ...|sign_of(len lcf - len gcf)]
        [lcf <= cf <= gcf]
        [cf == log_(base;y)]

        #]]]'''#'''

    ######################
    def detect_rational_log__pint_(n0, n1, /):
        '-> ...|(g,en,ed) |^Error__log__base_eq_1 # [n0**(en/ed) == n1][g**ed == n0][g**en == n1][gcd(en,ed) == 1]'
    def detect_rational_log__Fraction_(n0, d0, n1, d1, /):
        '-> ...|(g0,g1,gn,gd,en,ed) |^Error__log__base_eq_1 # [(n0/d0)**(en/ed) == (n1/d1)][(gn/gd)**ed == n0/d0][(gn/gd)**en == n1/d1][gcd(en,ed) == 1][gcd(gn,gd) >= 1][gn**ed *g0 == n0][gd**ed *g0 == d0][gn**en *g1 == n1][gd**en *g1 == d1]'
    ######################
    def iter_continued_fraction_of_irrational_log_cf_(cf_digits4base, cf_digits4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False, upperbound4num_bits4k=default_upperbound4num_bits4k, upperbound4failure_num_bits4k=default_upperbound4failure_num_bits4k):
        r'''[[[
        cf_digits4base/Iter int{>=1} -> cf_digits4y/Iter int{>=1} -> (iter_num_bits4k/(Iter param4memory_consume)=None) -> cf/iter continued_fraction_of_log_(base; y)[:?depends on iter_num_bits4k?]

        [base == cf_(cf_digits4base)]
        [y == cf_(cf_digits4y)]

        [base >= 1]
        [y >= 1]

        [[base==1] -> [cf == []/+oo]]
        StopIteration(emay (emay_sign, emay lcf_digit, emay gcf_digit))
            ... if no k
            if emay_sign == 0:
                [lcf == cf == gcf]

        [emay_sign == ...|sign_of(len lcf - len gcf)]
        [lcf <= cf <= gcf]
        [cf == log_(base;y)]

        #]]]'''#'''
    def iter_continued_fraction_of_irrational_ln_cf_(cf_digits4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False, upperbound4num_bits4k=default_upperbound4num_bits4k, upperbound4failure_num_bits4k=default_upperbound4failure_num_bits4k):
        'see:iter_continued_fraction_of_irrational_log_cf_<base=the_natural_logarithm_base>'
    def iter_continued_fraction_of_irrational_ln_Fraction_(N4y, D4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False, upperbound4num_bits4k=default_upperbound4num_bits4k, upperbound4failure_num_bits4k=default_upperbound4failure_num_bits4k):
        'see:iter_continued_fraction_of_irrational_log_cf_<base=the_natural_logarithm_base;y=(N4y/D4y)>'



    ######################
    def convert_to_ContinuedFraction_(rational_or_pair_or_list_or_iterator, /):
        'cf_like/(Rational|(N,D)|[int]|(Iterator int)|(LazyList int)|ContinuedFraction) -> cf/ContinuedFraction'
    def cf_log_(base, y, /, **kwds):
        r'''[[[
        :: base/cf_like -> y/cf_like -> cf/ContinuedFraction


        [cf_like = (Rational|(N,D)|[int]|(Iterator int)|(LazyList int)|ContinuedFraction)]
        [base > 0]
        [base =!= 1]
        [y > 0]
        [cf == log_(base;y)]
        #ContinuedFraction no support: xxx: [[base==1] -> [cf == []/+oo]]
        # diff iter_continued_fraction_of_irrational_log_cf_: allow:[0<base<1][0<y<1] but forbid:[base==1]
        # others see:iter_continued_fraction_of_irrational_log_cf_

        #]]]'''#'''
    def cf_ln_(y, /, **kwds):
        'see:cf_log_'
    def cf_log2_(y, /, **kwds):
        'see:cf_log_'

    ######################
#end-API

def __():
    i = 100000
    def _raise_():
        nonlocal i
        i -= 1
        if i <= 0:
            raise 000
    return _raise_
if 0b00:
    _raise_ = __()
else:
    def _raise_():
        pass


def _mk__may_num_bits4k_(k, /):
    flb_k = floor_log2(k)
    if k == (1<<flb_k):
        num_bits4k = flb_k
        may_num_bits4k = num_bits4k
    else:
        may_num_bits4k = None
    return may_num_bits4k

def _mk__mul_k_(k, kb, ky, may_num_bits4k, /):
    #assert type(k_or_num_bits4k) is int
    #assert type(mul_vs_lshift) is bool
    mul_vs_lshift = not may_num_bits4k is None
    if mul_vs_lshift is True:
        #lshift
        #num_bits4k = k_or_num_bits4k
        #k = 1 << num_bits4k
        num_bits4k = may_num_bits4k
        assert k == 1 << num_bits4k
        #assert 0 <= num_bits4k
        #assert num_bits4k < ceil_log2(kb)
        #assert num_bits4k <= floor_log2(ky)
        # [1 == 2**0 <= 2**num_bits4k]
        # [2**num_bits4k <= 2**(ceil_log2(kb)-1) < kb <= 2**ceil_log2(kb)]
        # [2**num_bits4k <= 2**floor_log2(ky) <= ky < 2**(floor_log2(ky)+1)]
        # [k := 2**num_bits4k]
        # [1 <= k]
        # [k < kb]
        # [k <= ky]
        if 0:
            def mul_k_(x, /):
                return x << num_bits4k
        mul_k_ = num_bits4k.__rlshift__
    else:
        #mul
        #k = k_or_num_bits4k
        k
        #assert 1 <= k
        #assert k < kb
        #assert k <= ky
        # [1 <= k]
        # [k < kb]
        # [k <= ky]
        if 0:
            def mul_k_(x, /):
                return k*x
        mul_k_ = k.__mul__
    assert 1 <= k
    assert k < kb
    assert k <= ky
    # [1 <= k]
    # [k < kb]
    # [k <= ky]
    return k, mul_k_
def dfloor_log_ex_(k, kb, ky, /, *, may_num_bits4k):
    k, mul_k_ = _mk__mul_k_(k, kb, ky, may_num_bits4k)
    # [1 <= k]
    # [k < kb]
    # [k <= ky]
    e = 0
    while not ky < kb:
        _raise_()
        # [k < kb <= ky]
        # [k < k*kb <= k*ky]
        # [k <= k*ky/kb]
        # [k <= k*ky//kb]
        new_ky = floor_div(mul_k_(ky), kb)
        #new_ky = (k*ky)//kb
        assert k <= new_ky < ky, (k, new_ky, ky, kb)
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


def ufloor_log_ex_(k, kb, ky, /, *, may_num_bits4k):
    k, mul_k_ = _mk__mul_k_(k, kb, ky, may_num_bits4k)
    # [1 <= k]
    # [k < kb]
    # [k <= ky]
    e = 0
    while not ky < kb:
        _raise_()
        # [k < kb <= ky]
        # [k < k*kb <= k*ky]
        # [k <= k*ky/kb]
        # [k <= ceil(k*ky/kb) == (k*ky-1)//kb +1]
        new_ky = ceil_div(mul_k_(ky), kb)
        #new_ky = (k*ky-1)//kb +1
        assert k <= new_ky < ky, (k, new_ky, ky, kb)
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
    may_num_bits4k = _mk__may_num_bits4k_(k)
    fs = _fs
    while k < kb:
        _raise_()
        _kb, cf_digit = fs[lower_vs_upper](k, kb, ky, may_num_bits4k=may_num_bits4k)
        yield cf_digit
        kb, ky = _kb, kb
        lower_vs_upper = not lower_vs_upper
def iter_continued_fraction_of_log__truncated_(param4memory_consume, base, y, /, *, to_detect_rational_result=False):
    r'''[[[
    param4memory_consume -> base/int{>=1} -> y/int{>=1} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [[base==1] -> [cf == []/+oo]]
    StopIteration((emay_sign, emay lcf_digit, emay gcf_digit))
        if emay_sign == 0:
            [lcf == cf == gcf]

    [emay_sign == ...|sign_of(len lcf - len gcf)]
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
        return iter_continued_fraction_of_log_Fraction__truncated_(param4memory_consume, base, 1, y, 1, to_detect_rational_result=to_detect_rational_result)
    else:
        detect_rational_log__pint_

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
                return (0, a, b) # len lcf == len gcf
            return (-1, a, b) # len lcf < len gcf
        if b is ...:
            return (+1, a, b) # len lcf > len gcf

        if a == b:
            yield a
        else:
            #truncate
            return (..., a, b)
                #^StopIteration
            return ...
            break

_null_iter = iter('')


def iter_continued_fraction_of_log_Fraction__truncated_(param4memory_consume, N4base, D4base, N4y, D4y, /, *, to_detect_rational_result=False):
    r'''[[[
    param4memory_consume -> N4base/int{>=1} -> D4base/int{>=1,<=N4base} -> N4y/int{>=1} -> D4y/int{>=1,<=N4y} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [base == N4base/D4base]
    [y == N4y/D4y]

    [[base==1] -> [cf == []/+oo]]
    StopIteration((emay_sign, emay lcf_digit, emay gcf_digit))
        if emay_sign == 0:
            [lcf == cf == gcf]

    [emay_sign == ...|sign_of(len lcf - len gcf)]
    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    assert 1 <= param4memory_consume
    assert 1 <= D4base <= N4base
    assert 1 <= D4y <= N4y
    if N4base == D4base:
        # [[base == 1] -> [cf==[]]] #+oo
        return iter_stop_with_((0, ..., ...), _null_iter)
    if N4y == D4y:
        # [[base =!= 1] -> [y == 1] -> [cf==[0]]] #0
        return iter_stop_with_((0, ..., ...), [0])
    if to_detect_rational_result:
        m = detect_rational_log__Fraction_(N4base, D4base, N4y, D4y)
            # ^Error__log__base_eq_1
        if not m is ...:
            it = iter_continued_fraction_digits5ND_(*m[-2:])
            #bug:return it
            #    # StopIteration(???)!!!
            return iter_stop_with_((0, ..., ...), it)

    if 1:
        return iter_continued_fraction_of_log_Fraction_interval__truncated_(param4memory_consume, N4base, D4base, N4base, D4base, N4y, D4y, N4y, D4y)
    else:
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



#upper bound
#lower bound
#interval = [=min, max=]
def _le_ND_(n0, d0, n1, d1, /):
    '[n0, d0, n1, d1 >= 1]'
    if d0 >= d1:
        #bug:return n0 <= n1
        if n0 <= n1:
            return True
    else:
        # [d0 < d1]
        if n0 >= n1:
            return False
    return n0*d1 <= n1*d0
def iter_continued_fraction_of_log_Fraction_interval__truncated_(param4memory_consume, N4min_base, D4min_base, N4max_base, D4max_base, N4min_y, D4min_y, N4max_y, D4max_y, /):
    r'''[[[
    param4memory_consume -> N4min_base/int{>=1} -> D4min_base/int{>=1,<=N4min_base} -> N4max_base/int{>=1} -> D4max_base/int{>=1,<=N4max_base} -> N4min_y/int{>=1} -> D4min_y/int{>=1,<=N4min_y} -> N4max_y/int{>=1} -> D4max_y/int{>=1,<=N4max_y} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [N4min_base/D4min_base == min_base <= base <= max_base == N4max_base/D4max_base]
    [N4min_y/D4min_y == min_y <= y <= max_y == N4max_y/D4max_y]

    [[base==1] -> [cf == []/+oo]]
    StopIteration((emay_sign, emay lcf_digit, emay gcf_digit))
        if emay_sign == 0:
            [lcf == cf == gcf]

    [emay_sign == ...|sign_of(len lcf - len gcf)]
    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    assert 1 <= param4memory_consume
    assert 1 <= D4min_base <= N4min_base
    assert 1 <= D4max_base <= N4max_base
    assert 1 <= D4min_y <= N4min_y
    assert 1 <= D4max_y <= N4max_y

    # (N4min_base, D4min_base)
    # (N4max_base, D4max_base)
    # (N4min_y, D4min_y)
    # (N4max_y, D4max_y)

    assert _le_ND_(N4min_base, D4min_base, N4max_base, D4max_base), (N4min_base, D4min_base, N4max_base, D4max_base)
    assert _le_ND_(N4min_y, D4min_y, N4max_y, D4max_y)


    k = param4memory_consume
    gkb = floor_div(k*N4min_base, D4min_base)
    lkb = ceil_div(k*N4max_base, D4max_base)

    lky = floor_div(k*N4min_y, D4min_y)
    gky = ceil_div(k*N4max_y, D4max_y)

    assert 1 <= k
    assert k <= gkb <= lkb
    assert k <= lky <= gky

    lcf = iter_xbound_continued_fraction_of_log_(False, k, lkb, lky)
    gcf = iter_xbound_continued_fraction_of_log_(True, k, gkb, gky)
    return _zip(lcf, gcf)



default_upperbound4failure_num_bits4k = (1<<8)+1
default_upperbound4num_bits4k = (1<<16) +1
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
class BaseError__continued_fraction_of_log(Exception):pass
class Error__log__base_eq_1(BaseError__continued_fraction_of_log):pass
class Error__continued_fraction_of_log__num_bits4k_too_big(BaseError__continued_fraction_of_log):pass
class Error__continued_fraction_of_log__result_is_probably_rational(BaseError__continued_fraction_of_log):
    r'''[[[
    [log_(7**2;7**3) == 3/2]
    but since input are are both rational, if log_(b;y) is rational too, then (b;y) must share same prime factors!
    #]]]'''#'''

def detect_rational_log__pint_(n0, n1, /):
    '-> ...|(g,en,ed) |^Error__log__base_eq_1 # [n0**(en/ed) == n1][g**ed == n0][g**en == n1][gcd(en,ed) == 1]'
    m = _detect_rational_log__pint_(n0, n1)
    if m is ...:
        return ...
    (swap_01, g, en, ed) = m
    if swap_01:
        ed, en = en, ed
    #danger:assert n0**en == n1**ed
    if not gcd(ed, en) == 1: raise 000
    assert n0 == g**ed
    assert n1 == g**en
    return (g,en,ed)
def _detect_rational_log__pint_(n0, n1, /):
    '-> ...|(swap_01, g,en,ed) # [n0**(en/ed) == n1][g**ed == n0][g**en == n1][gcd(en,ed) == 1]'
    assert n0 >= 1
    assert n1 >= 1
    swap_01 = False
    if n0 == 1: raise Error__log__base_eq_1
    # [n0 =!= 1]

    if n1 == 1:
        (g,en,ed) = (n0, 0, 1)
        return (swap_01, g,en,ed)
    # [n1 =!= 1]

    if n0 == n1:
        (g,en,ed) = (n0, 1, 1)
        return (swap_01, g,en,ed)
    # [n0 =!= n1]

    if n0 > n1:
        n0, n1 = n1, n0
        swap_01 = not swap_01
    # [n0 < n1]

    # [2 <= n0 < n1]
    #
    # [n0**(en/ed) == n1]:
    #   [n0**en == n1**ed]
    #   xxx [n0**(1/ed) == n1**(1/en) == gcd(n0,n1) >= 2]
    #       [gcd(2**6,2**10) == 2**6]
    #       [(2**6)**5 == (2**10)**3]
    # !!!gcd on exp!!!
    # [2 <= n0 < n1]
    n = n1
    d = n0
    qs = []
    # [n > d >= 2]
    while 1:
        # !!!gcd on exp!!!
        # [n > d >= 2]
        e8q, unfactored_part = factor_pint_out_power_of_base_(d, n)
        # [n == d**e8q * unfactored_part]
        # [n == g**e4n][d == g**e4d]:
        #   [unfactored_part == g**(e4n-e8q*e4d) == g**(e4n%e4d)]
        if not unfactored_part < d:
            return ...
        # [1 <= unfactored_part < d]
        qs.append(e8q)
        if unfactored_part == 1:
            g = d
            # !! [n > d >= 2]
            # [g >= 2]
            break
        # [2 <= unfactored_part < d]
        n, d = d, unfactored_part
        # [2 <= d < n]
    # [g >= 2]
    if 0:
        ed, unfactored_part = factor_pint_out_power_of_base_(g, n0)
        if not unfactored_part == 1:
            raise 000
        # [g**ed == n0]

        en, unfactored_part = factor_pint_out_power_of_base_(g, n1)
        if not unfactored_part == 1:
            raise 000
        # [g**en == n1]
    else:
        NDs = [*iter_approximate_fraction_NDs5continued_fraction_(qs)]
        (en, ed) = NDs[-1]
        assert en >= ed
        # [g**en == n1]
        # [g**ed == n0]

    # [gcd(ed, en) == 1]
    # [g**ed == n0]
    # [g**en == n1]
    # [n0**en == n1**ed]
    # [n0**(en/ed) == n1]
    # [(en/ed) == log_(n0;n1)]
    #assert save == n0, n1
    return (swap_01, g,en,ed)
#end-def detect_rational_log__pint_(n0, n1, /):

def detect_rational_log__Fraction_(n0, d0, n1, d1, /):
    '-> ...|(g0,g1,gn,gd,en,ed) |^Error__log__base_eq_1 # [(n0/d0)**(en/ed) == (n1/d1)][(gn/gd)**ed == n0/d0][(gn/gd)**en == n1/d1][gcd(en,ed) == 1][gcd(gn,gd) >= 1][gn**ed *g0 == n0][gd**ed *g0 == d0][gn**en *g1 == n1][gd**en *g1 == d1]'
    assert n0 >= 1
    assert d0 >= 1
    assert n1 >= 1
    assert d1 >= 1
    m = _detect_rational_log_(n0, d0, n1, d1)
    if m is ...:
        return ...
    (swap_01, swap_nd, g0,g1,gn,gd,en,ed) = m
    if swap_01:
        (g0,g1,en,ed) = (g1,g0,ed,en)
    if swap_nd:
        (gn,gd) = (gd,gn)
    #danger:assert n0**en * d1**ed == n1**ed * d0**en
    assert gcd(en,ed) == 1
    assert gn**ed *g0 == n0
    assert gd**ed *g0 == d0
    assert gn**en *g1 == n1
    assert gd**en *g1 == d1
    # [gcd(en,ed) == 1][gn**ed *g0 == n0][gd**ed *g0 == d0][gn**en *g1 == n1][gd**en *g1 == d1]
    # [gcd(gn,gd) >= 1]
    return (g0,g1,gn,gd,en,ed)

def _detect_rational_log_(n0, d0, n1, d1, /):
    '-> ...|(swap_01, swap_nd, g0,g1,gn,gd,en,ed)'
    swap_01 = False
    swap_nd = False
    if n0 == d0: raise Error__log__base_eq_1
    if n1 == d1:
        (g0,g1,gn,gd,en,ed) = (1,n1,n0,d0,0,1)
        return (swap_01, swap_nd, g0,g1,gn,gd,en,ed)
    # [n0 =!= d0]
    # [n1 =!= d1]
    if n0 < d0:
        (n0, d0, n1, d1) = (d0, n0, d1, n1)
        swap_nd = not swap_nd
    # [n0 > d0]
    if n1 < d1:
        return ...
    # [n0 > d0]
    # [n1 > d1]

    # [1 < 2 < 4 < 8]: [log_(4/2;8/1) == 3]
    if d0 == d1 and n0 == n1:
        (g0,g1,gn,gd,en,ed) = (1,1,n0,d0,1,1)
        return (swap_01, swap_nd, g0,g1,gn,gd,en,ed)
    n0, g0, d0 = gcd_ex(n0, d0)
    n1, g1, d1 = gcd_ex(n1, d1)
    # [gcd(n0, d0) == 1]
    # [gcd(n1, d1) == 1]
    if d0 == d1:
        if d0 == 1:
            (gn,en,ed) = detect_rational_log__pint_(n0, n1)
        elif n0 == n1:
            (gn,en,ed) = (n0, 1, 1)
        else:
            return ...
        gd = d0
        return (swap_01, swap_nd, g0,g1,gn,gd,en,ed)
    # [d0 =!= d1]
    if d0 == 1:
        return ...
    if d1 == 1:
        return ...
    if d0 > d1:
        n0, d0, n1, d1 = n1, d1, n0, d0
        swap_01 = not swap_01
    # [2 <= d0 < d1]
    # [n0 > d0]
    # [n1 > d1]
    # [gcd(n0, d0) == 1]
    # [gcd(n1, d1) == 1]
    if not n0 < n1:
        return ...
    # [n0 < n1]

    # [2 <= d0 < {n0,d1} < n1]
    m = detect_rational_log__pint_(d0, d1)
    if m is ...:
        return ...
    gd, en, ed = m
    # [gd**en == d1]
    # [gd**ed == d0]
    #
    # [d0**(en/ed) == d1]
    # [d0**en == d1**ed]
    if 0:
        m = detect_rational_log__pint_(n0, n1)
        if m is ...:
            return ...
        if not (en, ed) == m[-2:]:
            return ...
        gn, _en, _ed = m
    else:
        try:
            gn = perfect_kth_root_(ed, n0)
        except NotPerfectError__kth_root:
            return ...
        # [gn**ed == n0]
        if not gn**en == n1:
            return ...
        # [gn**en == n1]
    return (swap_01, swap_nd, g0,g1,gn,gd,en,ed)


def iter_continued_fraction_of_irrational_log_Fraction_(N4base, D4base, N4y, D4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False, to_detect_rational_result=False, to_detect_rational_result_when_troubleshooting=True, upperbound4num_bits4k=default_upperbound4num_bits4k, upperbound4failure_num_bits4k=default_upperbound4failure_num_bits4k):
    r'''[[[
    N4base/int{>=1} -> D4base/int{>=1,<=N4base} -> N4y/int{>=1} -> D4y/int{>=1,<=N4y} -> (iter_num_bits4k/(Iter param4memory_consume)=None) -> cf/iter continued_fraction_of_log_(base; y)[:?depends on iter_num_bits4k?]

    [base == N4base/D4base]
    [y == N4y/D4y]

    [[base==1] -> [cf == []/+oo]]
    StopIteration(emay (emay_sign, emay lcf_digit, emay gcf_digit))
        ... if no k
        if emay_sign == 0:
            [lcf == cf == gcf]

    [emay_sign == ...|sign_of(len lcf - len gcf)]
    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''
    assert 1 <= D4base <= N4base
    assert 1 <= D4y <= N4y
    #N4base, _, D4base = gcd_ex(N4base, D4base)
    #N4y, _, D4y = gcd_ex(N4y, D4y)

    def main():
        to_detect_rational_result
        detected = False
        st = (to_detect_rational_result, detected)
        return _iter_continued_fraction_of_irrational_log_Fraction_(st, args5num_bits4k_, troubleshoot_, iter_num_bits4k=iter_num_bits4k, force4using_big_num_bits4k=force4using_big_num_bits4k, upperbound4num_bits4k=upperbound4num_bits4k, upperbound4failure_num_bits4k=upperbound4failure_num_bits4k)

    def args5num_bits4k_(st, num_bits4k, /):
        (to_detect_rational_result, detected) = st
        case = 1
        args = (N4base, D4base, N4y, D4y, to_detect_rational_result)
        if to_detect_rational_result:
            to_detect_rational_result = False
            detected = True
            st = (to_detect_rational_result, detected)
        #bug:args = (N4base, D4base, N4y, D4y, to_detect_rational_result)
        #   should use old-to_detect_rational_result
        return st, case, args
    def troubleshoot_(st, case, args, num_bits4k, prev_num_bits4k_which_yield_cf_digit, upperbound4failure_num_bits4k, /):
        (to_detect_rational_result, detected) = st
        #(N4base, D4base, N4y, D4y, to_detect_rational_result) = args
        if not detected:
            if to_detect_rational_result_when_troubleshooting:
                to_detect_rational_result = True
                #detected = True
                st = (to_detect_rational_result, detected)
                ok = True
            else:
                #raise Error__continued_fraction_of_log__result_is_probably_rational(N4base, D4base, N4y, D4y)
                ok = False
        else:
                ok = True
        return st, ok
    return main()

def _iter_continued_fraction_of_irrational_log_Fraction_(st, args5num_bits4k_, troubleshoot_, /, *, iter_num_bits4k, force4using_big_num_bits4k, upperbound4num_bits4k, upperbound4failure_num_bits4k):
    if iter_num_bits4k is None:
        iter_num_bits4k = mk_default_iter_num_bits4k()
    iter_num_bits4k = iter(iter_num_bits4k)

    prev_total_cf_digits = 0
    prev_num_bits4k = -1
    prev_num_bits4k_which_yield_cf_digit = 0
    emay_t = ...
    for num_bits4k in iter_num_bits4k:
        _raise_()
        if not force4using_big_num_bits4k:
            if num_bits4k >= upperbound4num_bits4k: raise Error__continued_fraction_of_log__num_bits4k_too_big(num_bits4k)
        if not num_bits4k > prev_num_bits4k:raise ValueError
        prev_num_bits4k = num_bits4k

        k = 1<<num_bits4k

        st, case, args = args5num_bits4k_(st, num_bits4k)
        if case == 1:
            (N4base, D4base, N4y, D4y, to_detect_rational_result) = args
            it = iter_continued_fraction_of_log_Fraction__truncated_(k, N4base, D4base, N4y, D4y, to_detect_rational_result=to_detect_rational_result)
        elif case == 2:
            (N4min_base, D4min_base, N4max_base, D4max_base, N4min_y, D4min_y, N4max_y, D4max_y) = args
            it = iter_continued_fraction_of_log_Fraction_interval__truncated_(k, N4min_base, D4min_base, N4max_base, D4max_base, N4min_y, D4min_y, N4max_y, D4max_y)
        else:
            raise 000

        it = GetStopIterationValue(it)
        i = -1
        # [cf_digit == cf[i]]
        for i, cf_digit in enumerate(it):
            # [cf_digit == cf[i]]
            _raise_()
            if i == prev_total_cf_digits:
                # [cf_digit == cf[i]]
                yield cf_digit
                break
            else:
                # discard cf_digit since yielded before
                pass
        # [cf_digit == cf[i]]
        for i, cf_digit in enumerate(it, i+1):
            # [cf_digit == cf[i]]
            _raise_()
            yield cf_digit
        else:
            # [cf_digit == cf[i]]
            i += 1
            # [cf_digit == cf[i-1]]
        # [cf_digit == cf[i-1]]
        tm = it.get_tmay_value5StopIteration()
        if not tm: raise 000
        [emay_t] = tm
            #update emay_t
        if emay_t is None:raise 000
        emay_sign, emay_lcf_digit, emay_gcf_digit = emay_t

        # [cf_digit == cf[i-1]]
        total_cf_digits = i
        if total_cf_digits < prev_total_cf_digits:#raise 000
            raise Exception(total_cf_digits, prev_total_cf_digits)

        elif prev_total_cf_digits < total_cf_digits:
            prev_total_cf_digits = total_cf_digits
            prev_num_bits4k_which_yield_cf_digit = num_bits4k
        else:
            assert prev_total_cf_digits == total_cf_digits
            if num_bits4k -prev_num_bits4k_which_yield_cf_digit >= upperbound4failure_num_bits4k:
                # troubleshooting
                st, ok = troubleshoot_(st, case, args, num_bits4k, prev_num_bits4k_which_yield_cf_digit, upperbound4failure_num_bits4k)
                if not ok:
                    raise Error__continued_fraction_of_log__result_is_probably_rational(N4base, D4base, N4y, D4y)

        if emay_sign is ...:
            # [lcf_digit =!= gcf_digit]
            pass
        elif emay_sign == 0:
            # [lcf == cf == gcf]
            # [cf is not irrational]
            break
        # [lcf =!= gcf]
        # refine
        continue
        ...
    return emay_t # (...|(emay_sign,emay_lcf_digit,emay_gcf_digit))
        # ... if no k
        # ^StopIteration



def iter_continued_fraction_of_irrational_ln_Fraction_(N4y, D4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False, upperbound4num_bits4k=default_upperbound4num_bits4k, upperbound4failure_num_bits4k=default_upperbound4failure_num_bits4k):
    'see:iter_continued_fraction_of_irrational_log_cf_<base=the_natural_logarithm_base;y=(N4y/D4y)>'
    assert 1 <= D4y <= N4y
    cf_digits4y = iter_continued_fraction_digits5ND_(N4y, D4y)
    return iter_continued_fraction_of_irrational_ln_cf_(cf_digits4y, iter_num_bits4k=iter_num_bits4k, force4using_big_num_bits4k=force4using_big_num_bits4k, upperbound4num_bits4k=upperbound4num_bits4k, upperbound4failure_num_bits4k=upperbound4failure_num_bits4k)
def iter_continued_fraction_of_irrational_ln_cf_(cf_digits4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False, upperbound4num_bits4k=default_upperbound4num_bits4k, upperbound4failure_num_bits4k=default_upperbound4failure_num_bits4k):
    'see:iter_continued_fraction_of_irrational_log_cf_<base=the_natural_logarithm_base>'
    cf_digits4e = raw_iter_cf_digits4e_the_natural_logarithm_base_()
    return iter_continued_fraction_of_irrational_log_cf_(cf_digits4e, cf_digits4y, iter_num_bits4k=iter_num_bits4k, force4using_big_num_bits4k=force4using_big_num_bits4k, upperbound4num_bits4k=upperbound4num_bits4k, upperbound4failure_num_bits4k=upperbound4failure_num_bits4k)
def iter_continued_fraction_of_irrational_log_cf_(cf_digits4base, cf_digits4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False, upperbound4num_bits4k=default_upperbound4num_bits4k, upperbound4failure_num_bits4k=default_upperbound4failure_num_bits4k):
    r'''[[[
    cf_digits4base/Iter int{>=1} -> cf_digits4y/Iter int{>=1} -> (iter_num_bits4k/(Iter param4memory_consume)=None) -> cf/iter continued_fraction_of_log_(base; y)[:?depends on iter_num_bits4k?]

    [base == cf_(cf_digits4base)]
    [y == cf_(cf_digits4y)]

    [base >= 1]
    [y >= 1]

    [[base==1] -> [cf == []/+oo]]
    StopIteration(emay (emay_sign, emay lcf_digit, emay gcf_digit))
        ... if no k
        if emay_sign == 0:
            [lcf == cf == gcf]

    [emay_sign == ...|sign_of(len lcf - len gcf)]
    [lcf <= cf <= gcf]
    [cf == log_(base;y)]

    #]]]'''#'''

    cf_digits4base = iter(cf_digits4base)
    cf_digits4y = iter(cf_digits4y)

    def main():
        NDs4base, base_eq1 = _mk_NDs5cf__ex_(cf_digits4base)
        NDs4y, y_eq1 = _mk_NDs5cf__ex_(cf_digits4y)
        if base_eq1:
            # [[base == 1] -> [cf==[]]] #+oo
            return iter_stop_with_((0, ..., ...), _null_iter)
        if y_eq1:
            # [[base =!= 1] -> [y == 1] -> [cf==[0]]] #0
            return iter_stop_with_((0, ..., ...), [0])

        st = (0, NDs4base, 0, NDs4y)
        return _iter_continued_fraction_of_irrational_log_Fraction_(st, args5num_bits4k_, troubleshoot_, iter_num_bits4k=iter_num_bits4k, force4using_big_num_bits4k=force4using_big_num_bits4k, upperbound4num_bits4k=upperbound4num_bits4k, upperbound4failure_num_bits4k=upperbound4failure_num_bits4k)

    def _icheck_(cf_digits, /):
        for d in cf_digits:
            assert d >= 1
            yield d
    def _mk_NDs5cf__ex_(cf_digits, /):
        cf_digits = _icheck_(cf_digits)
        NDs = iter_approximate_fraction_NDs5continued_fraction_(cf_digits)

        NDs = LazyList(NDs)
        ls = NDs.extract_prefix__le(2, relax=False)
        if not ls:
            # +oo?
            raise Exception('??[cf == +oo]??')
        is_one = ls == [(1, 1)]
        return NDs, is_one

    def _search_ND_(i, NDs, num_bits4k, /):
        ls = NDs.extract_prefix__le(2, relax=False)
        if not ls:
            # +oo?
            raise Exception('??[cf == +oo]??')
        while 1:
            if len(ls) == 1:
                break
            [(N0,D0), (N1,D1)] = ls
            if floor_log2(D0)+floor_log2(D1) >= num_bits4k:
                break
            NDs = NDs.extract_tail_or_raise()
            i += 1
            ls = NDs.extract_prefix__le(2, relax=False)
        (N0,D0) = ls[0]
        (N1,D1) = ls[-1]
        if i&1:
            (N0, D0), (N1, D1) = (N1, D1), (N0, D0)
        # [N0/D0 <= N1/D1]
        return i, NDs, (N0, D0, N1, D1)

    def args5num_bits4k_(st, num_bits4k, /):
        (idx4base, NDs4base, idx4y, NDs4y) = st
        idx4base, NDs4base, (N4min_base, D4min_base, N4max_base, D4max_base) = _search_ND_(idx4base, NDs4base, num_bits4k)
        idx4y, NDs4y, (N4min_y, D4min_y, N4max_y, D4max_y) = _search_ND_(idx4y, NDs4y, num_bits4k)

        st = (idx4base, NDs4base, idx4y, NDs4y)
        case = 2
        args = (N4min_base, D4min_base, N4max_base, D4max_base, N4min_y, D4min_y, N4max_y, D4max_y)
        return st, case, args
    def troubleshoot_(st, case, args, num_bits4k, prev_num_bits4k_which_yield_cf_digit, upperbound4failure_num_bits4k, /):
        #(N4min_base, D4min_base, N4max_base, D4max_base, N4min_y, D4min_y, N4max_y, D4max_y) = args
        ok = False
        return st, ok
    return main()



def convert_to_ContinuedFraction_(rational_or_pair_or_list_or_iterator, /):
    'cf_like/(Rational|(N,D)|[int]|(Iterator int)|(LazyList int)|ContinuedFraction) -> cf/ContinuedFraction'
    #see:mk_ND5or_rational_
    x = rational_or_pair_or_list_or_iterator
    cls = type(x)
    if cls is LazyList or cls is ContinuedFraction:
        cf_digits = x
    if cls is list:
        cf_digits = iter(cf_digits)
    elif cls is tuple:
        pair = x
        if not len(pair) == 2: raise TypeError
        N, D = pair
        cf_digits = iter_continued_fraction_digits5ND_(N, D)
    elif cls is int or isinstance(x, Rational):
        N, D = x.as_integer_ratio()
        cf_digits = iter_continued_fraction_digits5ND_(N, D)
    elif is_iterator(x):
        cf_digits = x
    else:
        raise TypeError(cls)
    #cf_digits = LazyList(cf_digits)
    cf = ContinuedFraction(cf_digits)
    return cf
def cf_log_(base, y, /, **kwds):
    r'''[[[
    :: base/cf_like -> y/cf_like -> cf/ContinuedFraction


    [cf_like = (Rational|(N,D)|[int]|(Iterator int)|(LazyList int)|ContinuedFraction)]
    [base > 0]
    [base =!= 1]
    [y > 0]
    [cf == log_(base;y)]
    #ContinuedFraction no support: xxx: [[base==1] -> [cf == []/+oo]]
    # diff iter_continued_fraction_of_irrational_log_cf_: allow:[0<base<1][0<y<1] but forbid:[base==1]
    # others see:iter_continued_fraction_of_irrational_log_cf_

    #]]]'''#'''
    cf4base = convert_to_ContinuedFraction_(base)
    cf4y = convert_to_ContinuedFraction_(y)
    if not cf4base > cf_0: raise TypeError
    if not cf4y > cf_0: raise TypeError
    to_neg = False
    if cf4base <= cf_1:
        if cf4base == cf_1: raise TypeError
        cf4base = cf4base.inv_()
        to_neg = not to_neg

    if cf4y <= cf_1:
        if cf4y == cf_1:
            return cf_0
        cf4y = cf4y.inv_()
        to_neg = not to_neg

    cf_digits4base = iter(cf4base)
    cf_digits4y = iter(cf4y)
    cf_digits4log_base_y = iter_continued_fraction_of_irrational_log_cf_(cf_digits4base, cf_digits4y, **kwds)
    cf4log_base_y = ContinuedFraction(cf_digits4log_base_y)

    if to_neg:
        cf4log_base_y = -cf4log_base_y
    return cf4log_base_y
def cf_ln_(y, /, **kwds):
    'see:cf_log_'
    cf_digits4e = raw_iter_cf_digits4e_the_natural_logarithm_base_()
    return cf_log_(cf_digits4e, y, **kwds)
def cf_log2_(y, /, **kwds):
    'see:cf_log_'
    return cf_log_(2, y, **kwds)
ContinuedFraction


######################
#main{iter_continued_fraction_of_irrational_log_Fraction_}
######################
def mk_ND5or_rational_(rational_or_ND, /):
    '((N,D)|Rational) -> (N,D)'
    #see:convert_to_ContinuedFraction_
    from fractions import Fraction
    cls = type(rational_or_ND)
    if cls is tuple:
        ND = rational_or_ND
        N, D = ND
    elif cls is int or isinstance(rational_or_ND, Rational):
        rational = rational_or_ND
        ND = rational.as_integer_ratio()
    else:
        raise TypeError(cls)
    ND = Fraction(*ND).as_integer_ratio()
        #std...
    #mk_tuple
    return ND
def _prepare4main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_(with_params__vs__without_params__vs__idx_only__vs__ND_only__vs__N_only__vs__D_only, /):
    from seed.tiny_.check import check_uint_lt
    check_uint_lt(6, with_params__vs__without_params__vs__idx_only__vs__ND_only__vs__N_only__vs__D_only)
    match with_params__vs__without_params__vs__idx_only__vs__ND_only__vs__N_only__vs__D_only:
        case 0:
            # with_params
            def f(params, idx6cf, approx_ND4logb_y, /):
                return (params, idx6cf, approx_ND4logb_y)
        case 1:
            # without_params
            def f(params, idx6cf, approx_ND4logb_y, /):
                return (idx6cf, approx_ND4logb_y)
        case 2:
            # idx_only
            def f(params, idx6cf, approx_ND4logb_y, /):
                return idx6cf
        case 3:
            # ND_only
            def f(params, idx6cf, approx_ND4logb_y, /):
                return approx_ND4logb_y
        case 4:
            # N_only
            def f(params, idx6cf, approx_ND4logb_y, /):
                (N, D) = approx_ND4logb_y
                return N
        case 5:
            # D_only
            def f(params, idx6cf, approx_ND4logb_y, /):
                (N, D) = approx_ND4logb_y
                return D
        case _:
            raise 000
    f
    return f
def main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_(ND4inv_threshold4relative_error, ND4base, NDs4ys, /, *, with_params__vs__without_params__vs__idx_only__vs__ND_only__vs__N_only__vs__D_only=0):
    f = _prepare4main4batch4until4iter_continued_fraction_of_irrational_log_Fraction_(with_params__vs__without_params__vs__idx_only__vs__ND_only__vs__N_only__vs__D_only)
    for ND4y in NDs4ys:
        params = (ND4inv_threshold4relative_error, ND4base, ND4y)
        (idx6cf, approx_ND4logb_y) = main4until4iter_continued_fraction_of_irrational_log_Fraction_(*params)
        yield f(params, idx6cf, approx_ND4logb_y)

def main4until4iter_continued_fraction_of_irrational_log_Fraction_(ND4inv_threshold4relative_error, ND4base, ND4y, /):
    r'''[[[
    -> (idx6cf, approx_ND4logb_y)
    until:ND4inv_threshold4relative_error
    #for N, D in it__NDs4logb_y:
        # [log_(b; y) ~= N/D]
        # [y ~= b**(N/D)]
        # [y**D ~= b**N]
        # [y**D/b**N ~= 1]
        # [abs(y**D-b**N)/b**N ~= 0]
        # [until:abs(y**D-b**N)/b**N <= threshold4relative_error == err == N4err/D4err]
        # [until:abs(yD-bN) <= err*bN]
        # [until:-err*bN <= (yD-bN) <= +err*bN]
        # [until:(1-err)*bN <= yD <= (1+err)*bN]
        # [until:(1-N4err/D4err)*bN <= yD <= (1+N4err/D4err)*bN]
        # until:[(D4err-N4err)*b**N <= D4err*y**D <= (D4err+N4err)*b**N]
    #]]]'''#'''
    from seed.tiny_.check import check_type_is, check_int_ge
    from fractions import Fraction

    it__NDs4logb_y = main4iter_continued_fraction_of_irrational_log_Fraction_(ND4base, ND4y, cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs=2)
    base = Fraction(*mk_ND5or_rational_(ND4base))
    y = Fraction(*mk_ND5or_rational_(ND4y))
    ND4threshold4relative_error = mk_ND5or_rational_(ND4inv_threshold4relative_error)[::-1]
    #threshold4relative_error = Fraction(*ND4threshold4relative_error)
    #assert threshold4relative_error > 0
    (N4err, D4err) = ND4threshold4relative_error
    #check_int_ge(0, N4err)
    check_int_ge(1, N4err) # MUST
    #check_int_ge(1, D4err)
    check_int_ge(N4err, D4err)

    DsubN4err = D4err -N4err
    DaddN4err = D4err +N4err
    for j, (N, D) in enumerate(it__NDs4logb_y):
        bN = base**N
        yD = y**D
        if DsubN4err*bN <= D4err*yD <= DaddN4err*bN:
            break
        del bN, yD
    else:
        raise 000
    j
    N, D
    bN, yD
    return (idx6cf:=j, approx_ND4logb_y:=(N, D))
def main4batch4iter_continued_fraction_of_irrational_log_Fraction_(ND4base, NDs4ys, /, *, size, cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs=0):
    from seed.tiny_.check import check_type_is, check_int_ge
    check_int_ge(0, size)
    kwds = dict(cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs=cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs, may_size=size, to_list=True)
    for ND4y in NDs4ys:
        ls = main4iter_continued_fraction_of_irrational_log_Fraction_(ND4base, ND4y, **kwds)
        yield (ND4base, ND4y, ls)
def main4iter_continued_fraction_of_irrational_log_Fraction_(ND4base, ND4y, /, *, cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs=0, may_size=None, to_list=False):
    #def iter_continued_fraction_of_irrational_log_Fraction_(N4base, D4base, N4y, D4y, /, *, iter_num_bits4k=None, force4using_big_num_bits4k=False, to_detect_rational_result=False, to_detect_rational_result_when_troubleshooting=True, upperbound4num_bits4k=default_upperbound4num_bits4k, upperbound4failure_num_bits4k=default_upperbound4failure_num_bits4k):
    from seed.tiny_.check import check_uint_lt
    check_uint_lt(3, cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs)
    if 0 == cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs:
        from seed.tiny import echo
    elif 1 <= cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs <= 2:
        from seed.math.continued_fraction.continued_fraction_fold import iter_approximate_fractions5continued_fraction_, iter_approximate_fraction_NDs5continued_fraction_


    ND4base = mk_ND5or_rational_(ND4base)
    ND4y = mk_ND5or_rational_(ND4y)
    cf_digits = iter_continued_fraction_of_irrational_log_Fraction_(*ND4base, *ND4y)
    match cf_digits__vs__approximate_fractions__vs__approximate_fraction_NDs:
        case 0:
            f = echo
        case 1:
            f = iter_approximate_fractions5continued_fraction_
        case 2:
            f = iter_approximate_fraction_NDs5continued_fraction_
    f
    it = f(cf_digits)
    if not may_size is None:
        sz = may_size
        it = islice(it, sz)
    if may_size is None and to_list:raise TypeError
    return it if may_size is None or not to_list else [*it]



__all__


from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import dfloor_log_ex_, ufloor_log_ex_, iter_xbound_continued_fraction_of_log_, iter_continued_fraction_of_log__truncated_

from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import iter_continued_fraction_of_log__truncated_
from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import iter_continued_fraction_of_irrational_log_Fraction_
from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import iter_continued_fraction_of_log_Fraction__truncated_

from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import *
