def DurShaper(exp):
    from random import randint
    sr = random.SystemRandom()
    list = []
    indexes = random.randint(1,9)
    dividers = [1,2,4,8]
    for i in range(1,indexes):
        list.append(random.randint(1,8)/sr.choice(dividers))
    return list
