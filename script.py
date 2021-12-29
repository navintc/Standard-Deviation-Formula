import math

x = list(map(float, input().rstrip().split()))
xbar = 0
third = []
fourth = []

svalue = 0.00

xbar = sum(x) / len(x)

print(f"xbar = {xbar}")

third = [(k-xbar) for k in x]
    
for j in third:
    fourth.append(j*j)

svalue = math.sqrt(sum(fourth)/(len(x) - 1))

print (str(round(svalue, 2)))
