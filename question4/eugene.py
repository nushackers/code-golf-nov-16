def f(s,k):
    r = ''
    for i in range(k):
        r += s[i::k]
    return r

print(f('codegolf.stackexchange.com', 4))