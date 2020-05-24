def countRotation(s, current):
    char = list(current)
    count = 0

    while current:
        if char != list(s):
            char.append(char[0])
            char.pop(0)
            count += 1
        else:
            return count

def checkChar(s):
    return all(sorted(list(set(string)))==sorted(list(set(s[0]))) for string in s)


def TzWccCharRotation(n, arrayStringToRotate):
    counts = {}
    min_count = 0

    if checkChar(arrayStringToRotate) == True:
        for string in arrayStringToRotate:
            counts[string] = 0
            for i in range(n):
                if arrayStringToRotate[i] != string:
                    counts[string] += countRotation(string, arrayStringToRotate[i])
    
        min_count = min(value for value in counts.values())
    else:
        min_count = -1

    return min_count



