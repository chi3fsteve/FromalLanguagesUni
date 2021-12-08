import time
import random

trafficVolumeA = float(input("Put traffic volume for road A (Value from 0 to 1): "))
trafficVolumeB = float(input("Put traffic volume for road B (Value from 0 to 1): "))

def isTraffic5s(x):
    if 1 in x:
        return True
    else:
        return False
def isWaiting(x):
    if x == [0]:
        return False
    if x == [1]:
        return True


while True:
    lightA = "RED"
    lightB = "RED"
    print("Road A: "+lightA+", Road B: "+lightB)
    time.sleep(3)
    lightA = "RED YELLOW"
    lightB = "RED"
    print("Road A: " + lightA + ", Road B: " + lightB)
    time.sleep(2)
    lightA = "GREEN"
    lightB = "RED"
    print("Road A: " + lightA + ", Road B: " + lightB)
    print("Cycle nr 1 on A")
    time.sleep(30)
    countCyclesOnA = 1
    if isTraffic5s(random.choices(population=[1, 0], weights=[trafficVolumeA, 1 - trafficVolumeA], k=5)) is True:
        print("Cycle nr "+str(countCyclesOnA+1)+" on A")
        time.sleep(30)
        countCyclesOnA += 1
    while True:
        if isWaiting(random.choices(population=[1, 0], weights=[trafficVolumeB+countCyclesOnA*trafficVolumeB, 1-(trafficVolumeB+countCyclesOnA*trafficVolumeB)])) is not True:
            print("Cycle nr " + str(countCyclesOnA + 1) + " on A")
            time.sleep(30)
            countCyclesOnA += 1
        else:
            break
    lightA = "YELLOW"
    lightB = "RED"
    print("Road A: " + lightA + ", Road B: " + lightB)
    time.sleep(2)
    lightA = "RED"
    lightB = "RED"
    print("Road A: " + lightA + ", Road B: " + lightB)
    time.sleep(3)
    lightA = "RED"
    lightB = "RED YELLOW"
    print("Road A: " + lightA + ", Road B: " + lightB)
    time.sleep(2)
    lightA = "RED"
    lightB = "GREEN"
    print("Road A: " + lightA + ", Road B: " + lightB)
    print("Cycle nr 1 on B")
    time.sleep(30)
    if isWaiting(random.choices(population=[1, 0],weights=[trafficVolumeA, 1-trafficVolumeA])) is not True:
        print("Cycle nr 2 on B")
        time.sleep(30)
    lightA = "RED"
    lightB = "YELLOW"
    print("Road A: " + lightA + ", Road B: " + lightB)
    time.sleep(2)

