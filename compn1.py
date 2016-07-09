import time
def n2(list1):
    start = time.time()
    for i in range(len(list1)):
        for j in range(len(list1)):
            if(list1[i]<=list1[j]):
                min_num = list1[i]
            else:
                min_num = list1[j]
    end = time.time()
    return end-start

def n1(list1):
    start = time.time()
    min2 = list1[1]
    for i in range(len(list1)):
        if(min2<=list1[i]):
            min2 = list1[i]
    end = time.time()
    return end-start

a = []
for i in range(10000):
    a.append(i)
print n1(a)
print n2(a)
