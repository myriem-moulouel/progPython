# exercice 8 :
from turtle import *

def fibonaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
    

n = int(input("saisissez un entier n : "))

for i in range(n//4):
    fib = fibonaci(i)
    circle(fib*10,90)
