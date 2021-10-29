import random
import math
from math import log2

#create an n-length array of integers between 0 and 100
def create_array(n):
    i = 1
    this_array = []
    while i <= n:
        this_array.append(random.randrange(100))
        i += 1
    return this_array


new_array = create_array(15)
print(new_array)

#Exercises
print("")
print("#1.1.1")
print( (0+15)/2 )
print((2.0 * math.e) - 6 * 100000000.1)
print(True and False or True and True)

print("")
print("#1.1.2")
print((1 + 2.236)/2)
print(type(1+2+3+4.0))
print("TypeError in Python")

print("")
print("#1.1.3")
def is_equal(a, b, c):
    if a == b and a == c:
        print("equal")
    else:
        print("unequal")

is_equal(11.0,11.00,11)

print("")
print("#1.1.4")
#java syntax questions..

print("")
print("#1.1.5")
def is_between(x, y):
    if x > 0 and x < 1 and y > 0 and y < 1:
        print("true")
    else:
        print("false")

is_between(.8472, 0.4)

print("")
print("#1.1.6")
f = 0;g = 1;i = 0
while i <= 15:
    print(f)
    f = f + g
    g = f - g
    i+=1

print("")
print("#1.1.7")
t = 9.0
while abs(t - 9.0/t) > .001:
    t = (9.0/t + t) / 2.0
print(t)

sum = 0; i = 1; j = 0
while i < 1000:
    while j < i:
        j+=1
        sum+=1
    i+=1
print(sum)

sum = 0; i = 1; j = 0
while i < 1000:
    while j < i:
        j+=1
        sum+=1
    i = i * 2
print(sum)

print("")
print("#1.1.8")
print("b")
print("b" + "c")
print("TypeError in Python")

print("")
print("#1.1.9")
#https://docs.python.org/3/reference/lexical_analysis.html#f-strings
n = 30
print(f'0b{n:08b}')

print("")
print("#1.1.10")
print("Java not instantiating a new array")

print("")
print("#1.1.11")
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
cols = len(max(T, key=len))
i = -1
while i < cols:
    if i == -1:
        print(" ",end="\t")
    else:
        print("c",i,end="\t")
    i+=1
print()

i = 1
for r in T:    
    print("r",i,end="\t")
    i+=1
    for c in r:
        print(c,end="\t")
    print()

print("")
print("#1.1.12")
a = [10]
i = 0
while i < 10:
    #a[i] = 9 - i 
    #this will break in Python, but doesn't matter for the exercise.
    i+=1
j = 0
while j < 10:
    #a[j] = a[a[j]]
    #same as above
    j+=1
k = 0
while k < 10:
    print(k) #hah. good one    
    k+=1

print("")
print("#1.1.13")
print(T)
z = zip(*T)
for row in z:
    print(row)
#todo: loses third because null in [1] - feex it

print("")
print("#1.1.14")

def lg(N):
    return int(log2(N))
    #todo: handle negatives, do not use math
print(lg(40))

print("")
print("#1.1.15")
A = [2,4,8,8,1,7,2,4,5]
def histogram(M,a):
    i = 0; arr = []
    while i < M:
        arr.append(a.count(i))
        i+=1
    return arr

print(histogram(10,A))

print("")
print("#1.1.16") #recursive methods
def exR1(n):
    if n<=0:
        return ""
    return str(exR1(n-3)) + str(n) + str(exR1(n-2)) + str(n)

print(exR1(6))

print("")
print("#1.1.17") 
#the return should be higher in the condition. this would overflow

print("")
print("#1.1.18") 

def mystery(a, b):
    if b==0: return 0;
    if b % 2 == 0: return mystery(a+a, int(b/2));
    return mystery(a+a, int(b/2)) +a;

def f(a, b):
    print("a+a: ", str(a+a),end='')
    print("b/2: ", str(int(b/2)),end='')

#f(2,25)
print(mystery(3,11))
#mystery multiplies the first parameter by the second

def mystery2(a, b):
    if b==0: return 1;
    if b % 2 == 0: return mystery(a*a, int(b/2));
    return mystery(a*a, int(b/2)) +a;

print(mystery2(1,3))

