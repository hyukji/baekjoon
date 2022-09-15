a = [3,4,5,7,1,2]
v = [1,2,3,4,7,6]
a2 = [3,4,9]
v2 = [5,8,10]
dict1 = dict(zip(a,v))
dict2 = dict(zip(a2,v2))
print(dict1, dict2)
# f_dict = 
for x in dict1 & dict2:
    print(x)
    