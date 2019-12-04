def calculateFuelRecurse(mass):
    fuelReq = (mass // 3) - 2
    if fuelReq <= 0:
        return 0
    return fuelReq + calculateFuelRecurse(fuelReq)

def calculateFuel():
    res = 0
    with open("day1.txt") as f:
        for line in f:
            res += calculateFuelRecurse(int(line))
    return res

print(calculateFuel())
