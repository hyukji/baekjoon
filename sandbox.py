d = [0]
while d:
    print(d)
    for dd in d:
        print(dd)
        if dd < 5:
            d.append(dd+1)

