import random

trafficVolumeA = 0.4
s = random.choices(population=[1,0],weights=[trafficVolumeA,1-trafficVolumeA],k=5)
print(s)