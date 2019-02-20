from random import randint
def DurShaper(exp):
    list = []
    indexes = random.randint(1,9)
    dividers = [1,2,4,8]
    for i in range(1,indexes):
        list[i] = random.randint(1,8)
    return list
