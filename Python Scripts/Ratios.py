import numpy as np
import pandas as pd
from random import randint
df = pd.read_csv('Gear.csv', delimiter =',', header=None)

df = df.iloc[:,0:2]
#print(df)

l = []
for x in range(1,10):
    l.append(randint(1,13725))

print(l)

b = []
arr = df.values
for i in l:
    speed = arr[i,0]
    if speed == 0:
        continue
    wheel_rpm = (speed * 100)/(3.14159 * .4876 * 6)
    engine_rpm = arr[i,1]
    print(wheel_rpm,"\t",engine_rpm)

    prop_rpm = wheel_rpm*4.388
    g_ratio = engine_rpm/prop_rpm

    b.append(g_ratio)
    b.sort()
print("\n",b)
