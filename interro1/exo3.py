# Complexité

import time

k = 10000


# t1.append(v1)
t1 = list([1,2,3,4,7,3,8,0,5])
v1 = 9
# timer
t1_0 = time.perf_counter()
for i in range(k):
    t1.append(v1)
t1_1 = time.perf_counter()


# t2 = t2 + [v2]
t2 = list([1,2,3,4,7,3,8,0,5])
v2 = 9
# timer
t2_0 = time.perf_counter()
for i in range(k):
    t2 = t2 + [v2]
t2_1 = time.perf_counter()


# t3.extend([v3])
t3 = list([1,2,3,4,7,3,8,0,5])
v3 = 9
# timer
t3_0 = time.perf_counter()
for i in range(k):
    t3.extend([v3])
t3_1 = time.perf_counter()


# t4 += [v4]
t4 = list([1,2,3,4,7,3,8,0,5])
v4 = 9
# timer
t4_0 = time.perf_counter()
for i in range(k):
    t4 += [v4]
t4_1 = time.perf_counter()

print("le temps ecoulé pour t1.append(v1) = ", t1_1-t1_0)
print("le temps ecoulé pour t2 = t2 + [v2] = ", t2_1-t2_0)
print("le temps ecoulé pour t3.extend([v3]) = ", t3_1-t3_0)
print("le temps ecoulé pour t4 += [v4] = ", t4_1-t4_0)

# on conclue que l'operation t = t + [v] est la plus couteuse

# complexites :
# => t1.append(v1)
# => t2 = t2 + [v2] : O(n)
# => t3.extend([v3]) : 
# => t4 += [v4] : O(log(n))