import time
print time
def sum_of_n(n):
    start = time.time()
    sum1 = 0
    for i in range(1,n+1):
        sum1 = sum1+i
    end = time.time()
    return sum1, end-start
a =10
while(a<1000000000):
    print "sum is %d required in %10.7f seconds"%sum_of_n(a)
    a = a*10
