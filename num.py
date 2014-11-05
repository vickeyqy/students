import random
def num():
    num = [15,25,35,45,55]
    i =  random.randint(0,4)
    print  num[i]
    del num[i]
    x = random.randint(0,3)
    print num[x]
    num.append(num[i])



if __name__ =="__name__":
    num()
