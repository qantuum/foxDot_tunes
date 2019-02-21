def DurShaper(target):
    from random import randint
    sr = random.SystemRandom()
    indexes = random.randint(1,target*2)
    dividers = [1,1,2,2,2,4,8] # grab more chances to have 1 and 1/2 typed durations
    list=[]
    for i in range(0,indexes):
        a = random.randint(1,8)/sr.choice(dividers)
        if sum(list)+a < target:
            list.append(a)
    list.append(target-sum(list))                   
    return list # always return a list of durations with total duration equals target

a = DurShaper(4)
