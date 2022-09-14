a = [1,2,3,4,5,6]
ta = tuple(a)

for l in ta:
    a= list(ta)
    a.remove(l)
    print(a)
    # print(ta, a)
    