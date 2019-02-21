def DurShaper(exp):
    from random import randint
    sr = random.SystemRandom()
    indexes = random.randint(1,exp*2)
    dividers = [1,2,4,8]
    list=[]
    while sum(list) != exp:
        list = []
        for i in range(0,indexes):
            list.append(random.randint(1,8)/sr.choice(dividers))
    return [list,sum(list)]
