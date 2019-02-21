def DurShaper(target):
    from random import randint
    sr = random.SystemRandom()
    indexes = random.randint(1,target+4)
    dividers = [1,1,1,2,2,2,2,4,8] # 1/4 and 1/8-typed notes get more scarce
    list=[]
    for i in range(0,indexes):
        if target%2 == 0:
            a = random.randint(1,target/2)/sr.choice(dividers)
        else:
            a = random.randint(1,(target-1)/2)/sr.choice(dividers)
        if sum(list)+a < target/2:
            list.append(a)
        if sum(list)+a < target:
            list.append(a)
    list.append(target-sum(list))                   
    return list # always return a list of durations with total duration equals target

# variation giving shorter durations
def DurShaperSm(target):
    from random import randint
    sr = random.SystemRandom()
    indexes = random.randint(1,target+4)
    dividers = [1,1,1,2,2,2,2,4,8] # 1/4 and 1/8-typed notes get more scarce
    list=[]
    for i in range(0,indexes):
        if target%2 == 0:
            a = random.randint(1,target/2)/sr.choice(dividers)
        else:
            a = random.randint(1,(target-1)/2)/sr.choice(dividers)
        if sum(list)+a < target/2:
            list.append(a)
        if sum(list)+a/2 < target:
            list.append(a/2)
    list.append(target-sum(list))                   
    return list # always return a list of durations with total duration equals target

# test it !
a = DurShaper(8)
b = DurShaperSm(4)
print(a,b)
Scale.default.set("minorPentatonic")
aa >> pluck(P[[0,3,4],[0,2,1],[0,5,6],[0,7,8],[0,4],[0,3]].every(8,"shuffle"),dur=Pvar([a,b,PDur(3,8)],[8,4,4]))
ab >> zap(ss.degree[1] + P[3,5], dur=PDur(5,8),drive=0.05)
ac >> prophet(ss.degree[0] + P(0,3,5),dur=4, oct=(5,5,4))
