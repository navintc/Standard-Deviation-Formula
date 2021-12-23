import math

x = list(map(float, input().rstrip().split()))
xbar = 0
third = []
fourth = []
sum = 0

svalue = 0.00


for i in x:
    xbar += i;
xbar = xbar / len(x)

for k in x:
    third.append(k-xbar)
    
for j in third:
    fourth.append(j*j)

for d in fourth:
    sum += d
    

svalue = math.sqrt(sum/(len(x) - 1))

    
print (str(round(svalue, 2)))


