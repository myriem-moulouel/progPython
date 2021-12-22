from functools import reduce

# def pgs(v, l):
#     f = lambda maxi, x: (lambda r: r+1 if x==v  else maxi)(0)



#     f = lambda maxi, x: maxi+1 if x==v else maxi
#     return reduce (f, l )

# l = pgs(3, [3,3,0,9,7,3,3,3,3,3])
# print(l)

def pgs(v,l):
    f = lambda c,x: (c[0], c[1]+1) if x==v else (max(c), 0)
    return max(reduce(f, l, (0,0)))

l = pgs(3, [3,3,0,9,7,3,3,3,3,3])
print(l)