




def union_states(fa, get_initial, get_default, get_transition_symbols, get_next, get_state, *, state_key=None):
    q0 = get_initial(fa)
    qs = {}
    to_process = {q0}

    def add_to_process(q):
        if q not in qs:
            to_process.add(q)
    while to_process:
        q = to_process.pop()
        #if q in qs: continue
        assert q not in qs
        qs[q] = None # fail and next_ can be q, too

        fail = get_default(fa, q)
        add_to_process(fail)

        goto = {}
        syms = get_transition_symbols(fa, q)
        for sym in syms:
            next_ = get_next(fa, q, sym)
            add_to_process(next_)
            
            if next_ != fail:
                goto[sym] = next_
        qs[q] = (fail, goto)


        
    q_ls = sorted(qs.keys(), key = state_key)
    q2idx = {q:i for i, q in enumerate(q_ls)}
    fail = tuple(q2idx[qs[q][0]] for q in q_ls)
    gotos = tuple(qs[q][1] for q in q_ls)
    for goto in gotos:
        for sym, q in goto.items():
            goto[sym] = q2idx[q]

    transitions = gotos
    defaults = fail
    state0 = q2idx[q0]
    state = q2idx[get_state(fa)]
    state2substates = q_ls
    substates2state = q2idx
    return transitions, defaults, state0, state, state2substates, substates2state








'''

def unionFAs(FA_ls):
    assert len(FA_ls) > 1
    q0 = tuple(fa.get_initial() for fa in FA_ls)
    qs = {}
    to_process = {q0}

    def add_to_process(q):
        if q not in qs:
            to_process.add(q)
    while to_process:
        q = to_process.pop()
        #if q in qs: continue
        assert q not in qs

        fail = tuple(fa.get_default(qx) for fa, qx in zip(FA_ls, q))
        add_to_process(fail)

        goto = {}
        syms = set.union(fa.get_transition(qx).keys() for fa, qx in zip(FA_ls, q))
        for sym in syms:
            next_ = tuple(fa.next(qx, sym) for fa, qx in zip(FA_ls, q))
            add_to_process(next_)
            
            if next_ != fail:
                goto[sym] = next_
        qs[q] = (fail, goto)

    q_ls = sorted(qs.keys())
    q2idx = {q:i for i, q in enumerate(q_ls)}
    fail = tuple(q2idx[qs[q][0]] for q in q_ls)
    gotos = tuple(qs[q][1] for q in q_ls)
    for goto in gotos:
        for sym, q in goto.items():
            goto[sym] = q2idx[q]

    transitions = gotos
    defaults = fail
    state0 = q2idx[q0]
    state2substates = q_ls
    substates2state = q2idx
    return transitions, defaults, state0, state2substates, substates2state

'''







