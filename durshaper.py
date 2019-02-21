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
    return [P[list].shuffle(),len(list)] # always return a list of durations with total duration equals target

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
    return [P[list].shuffle(),len(list)] # always return a list of durations with total duration equals target

# a variation with score-like durations
def DurShaperSc(target):
    from random import randint
    sr = random.SystemRandom()
    indexes = random.randint(1,target+4)
    standards = [0.25,0.375,0.75,0.5,1,2,3,4] # standard dur values found in scores
    dividers = [1,1,2] # skip 1/4 and 1/8 (comes after)
    list=[]
    for i in range(0,indexes):
        if target%2 == 0:
            a = random.randint(1,target/2)/sr.choice(dividers)
        else:
            a = random.randint(1,(target-1)/2)/sr.choice(dividers)
        if sum(list)+a < target/4:
            list.append(a)
        if sum(list)+a/2 < target/2:
            list.append(a/2)
        if sum(list)+a < target:
            list.append(a)
        if sum(list)+a/4 < target:
            list.append(a/4)
    if sum(list) < target:
        for i in range(0,len(standards)):
            if target-sum(list)%standards[i] != 0 and standards[i] < target-sum(list):
                list.append(standards[i])
        if sum(list) < target:
            list.append(target-sum(list))                                 
    return [P[list].shuffle(),len(list)] # always return a list of durations with total duration equals target

# I tried to implement rests in this but to no avail. To use a rest, the best available option would be to trigger a cut on the target note

# test it !
a = DurShaper(8)
b = DurShaperSm(4)
print(a[0],b[0])
Scale.default.set("minorPentatonic")
aa >> pluck(P[[0,3,4],[0,2,1],[0,5,6],[0,7,8],[0,4],[0,3]].every(8,"shuffle"),dur=Pvar([a[0],b[0],PDur(3,8)],[8,4,4]))
ab >> zap(aa.degree[1] + P[3,5], dur=PDur(5,8),drive=0.05)
ac >> prophet(aa.degree[0] + P(0,3,5),dur=4, oct=(5,5,4))
op >> play("<x o ><->")

# another example of setup using pattern methods :
a = DurShaperSc(4)
print(a[0])
Scale.default.set("mixolydian")
Root.default.set(-3)
aa >> pluck(PRand(5),dur= a[0] | a[0].every(6,"rotate",3) )    
ab >> zap(aa.degree[1] + P[3,5], dur=1/2,drive=0.05)
ac >> keys(aa.degree[0] + P(0,3,7),dur=2, oct=(6,5,5),formant=0.03)
op >> play("<x o ><->")
