def calc(list):
    tot=0
    if len(list)==0:
        return 0
    else:
        for i in list:
            exp= i*i
            tot = exp+tot
        return tot

list = [1, 3, 4, 2, 5]
x = calc(list)        
print(x)