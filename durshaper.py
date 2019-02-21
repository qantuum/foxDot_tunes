def DurShaper(target):
    from random import randint
    sr = random.SystemRandom()
    indexes = random.randint(1,target+4)
    dividers = [1,1,1,2,2,2,2,4,8] # 1/4 and 1/8-typed notes get more scarce
    list=[]
    for i in range(0,indexes):
        a = random.randint(1,target)/sr.choice(dividers)
        if sum(list)+a < target:
            list.append(a)
    list.append(target-sum(list))                   
    return list # always return a list of durations with total duration equals target

a = DurShaper(4)
