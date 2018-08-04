
#from jidianzhengmaciku2zmls import zmls


def gen_dicts(zmls):
    
    zm2chars = dict(zmls)
    zm2hzs = dict()

    hz2zms = dict()
    hz2pre = dict()
    for zm, chars in zmls:
        assert zm not in zm2hzs
        zm2hzs[zm] = set()
        
        for hz, pre in chars:
            assert hz not in zm2hzs[zm]
            zm2hzs[zm].add(hz)
            
            if hz not in hz2pre:
                hz2pre[hz] = pre
            else:
                #assert hz2pre[hz] == pre
                if hz2pre[hz] != pre:
                    #print(hz, hz2pre[hz], pre)
                    pass

            if hz not in hz2zms:
                hz2zms[hz] = set()

            hz2zms[hz].add(zm)

    not1 = 0
    notPre = 0
    for hz, zms in hz2zms.items():
        if len(zms) > 1:
            for zm in zms:
                #assert len(zm2chars[zm]) == 1
                if len(zm2hzs[zm]) != 1:
                    for hz in zm2hzs[zm]:
                        #assert hz2zms[hz] == zms
                        if not hz2zms[hz] == zms:
                            break
                    else:
                        continue
                    not1 += 1./len(zm2hzs[zm])
                    break
                    print(hz, zms, zm2hzs[zm])
                    raise
            zms = list(zms)
            zms.sort()
            for a, b in zip(zms[:-1], zms[1:]):
                #assert b.startswith(a)
                if not b.startswith(a):
                    notPre += 1
                    break
                    print(hz, zms, a, b)
                    raise
            

    print('not1, notPre', not1, notPre)
    return zm2hzs, hz2zms, hz2pre

