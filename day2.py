def program(input):
    i = 0
    while i < len(input):
        if input[i] == 1:
            firstVal = input[input[i+1]]
            secondVal = input[input[i+2]]
            input[input[i+3]] = firstVal + secondVal
        elif input[i] == 2:
            firstVal = input[input[i+1]]
            secondVal = input[input[i+2]]
            input[input[i+3]] = firstVal * secondVal
        elif input[i] == 99:
            break
        else:
            print("INVALID OPCODE")
            break
        i += 4
    return input

def readInputandStart():
    with open("day2.txt") as f:
        contents = f.read()
        input = [int(x) for x in contents.split(",")]
    originalInput = input[:]

    for noun in range(100):
        for verb in range(100):
            input = originalInput[:]
            input[1] = noun
            input[2] = verb
            resultingInput = program(input)
            if resultingInput[0] == 19690720:
                print("NOUN", noun)
                print("VERB", verb)
                return


readInputandStart()
