
def kol_povt(spis):
    a = {}
    for string in spis:
        if string in a:
            a[string] += 1
        else:
            a[string] = 1
    return list(a.values())

spis1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
spis2 = ['aaa', 'bbb', 'ccc']
spis3 = ['abc', 'abc', 'abc']


result1 = kol_povt(spis1)
print(*result1)
result2 = kol_povt(spis2)
print(*result2)
result3 = kol_povt(spis3)
print(*result3)