def ensemble(l):
    return lambda x : x in l


import time
ens1=ensemble(set(range(50000)))
t=time.clock_gettime(0)
for x in range(300000):
    ens1(x)
print(time.clock_gettime(0)-t)

print(set([1, 3, 4]))