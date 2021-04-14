# %%
import random as rd
import math as m

inside = 0
total = 0
for _ in range(0, 100000000):
    x = rd.random()
    y = rd.random()
    dist = m.sqrt((x*x) + (y*y))
    if dist<1:
        inside = inside + 1
    total = total + 1
    
print((inside/total)*4)