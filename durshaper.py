def DurShaper(target):
    from random import randint
    sr = random.SystemRandom()
    indexes = random.randint(1,exp*2)
    dividers = [1,2,4,8]
    list=[]
    for i in range(0,indexes):
        a = random.randint(1,8)/sr.choice(dividers)
        if sum(list)+a < target:
            list.append(a)
    list.append(target-sum(list))                   
    return list # always return a list of durations with total duration equals target

a = DurShaper(4)
