# aml type

def mseq(a):
    if len(a)<=1:
        return 0

    m, mi = e[0] # mi = 0
    M, Mi = e[0]

    t = True
    for i, e in enumerate(a):
        le = last(e)

        if e == le:
            continue

        if (t and e>le) or (!t and e<le):
            _m, _M = m, M
        elif:
            _m, _M = le, le

        m, mi = min(_m, e): i in a
        M, Mi = max(_M, e): i in a
