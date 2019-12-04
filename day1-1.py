

def calculateFuel():
    res = 0
    with open("day1.txt") as f:
        for line in f:
            res += ((int(line) // 3) - 2)
    return res

def main():
    print(calculateFuel())

if __name__ == '__main__':
    main()
