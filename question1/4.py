def a(s, c):
    l = len(s)
    n = l/c
    s += " "*(c-(l%c))
    a = ""
    for i in range(c):
        for j in range(n+1):
            a += s[i+j*c]
    return a
