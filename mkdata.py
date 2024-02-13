
import random

iland_n = int(input("number of iland is :"))
bridge_n = int(input("number of bridge is :"))

print(str(iland_n)+" "+str(bridge_n))

for i in range(bridge_n):
    to_iland = random.randrange(1,iland_n+1,1)
    by_iland = random.randrange(1,iland_n+1,1)
    cost = random.randrange(1,10,1)
    print(str(to_iland)+" "+str(by_iland)+" "+str(cost))
