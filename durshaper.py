def DurShaper(exp):
    from random import randint
    sr = random.SystemRandom()
    indexes = random.randint(1,exp*2)
    dividers = [1,2,4,8]
    list=[]
    for i in range(0,indexes):
        a = random.randint(1,8)/sr.choice(dividers)
        if sum(list)+a < exp:
            list.append(a)
    list.append(exp-sum(list))                   
    return [list,sum(list)]

a = DurShaper(4)
