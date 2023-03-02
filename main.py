def array_from_file(path):
    array = []
    with open(path) as file:
        for line in file:
            for x in line.split(','):
                array.append(int(x))
    file.close()
    return array

def reBuild(alist):
    convertator = alist.copy()
    convertator.sort()
    sequenceLength = 0
    maxLength = 0
    sequenceStart = 0
    result = []
    for i in range(len(convertator) - 1, 0, -1):
        if convertator[i] - convertator[i - 1] == 1:
            sequenceLength += 1
        else:
            sequenceLength = 1
        if sequenceLength >= maxLength:
            maxLength = sequenceLength
            sequenceStart = i + maxLength - 2

    for i in range(sequenceStart, sequenceStart - maxLength, -1):
        result.append(convertator[i])

    result.reverse()

    return result


list1 = array_from_file('input.txt')
file1 = open('output.txt', 'wt')
file1.write(str(reBuild(list1)))
file1.close()
