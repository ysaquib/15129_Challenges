# Enter your code here. Read input from STDIN. Print output to STDOUT

alphabetLowerCase = 'abcdefghijklmnopqrstuvwxyz'
alphabetUpperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
oddNumbers = '13579'
evenNumbers = '02468'

def getLowerCase(stringS):
    lowerCase = []
    for i in range(len(stringS)):
        if stringS[i] in alphabetLowerCase:
            lowerCase.append(stringS[i])
    return sorted(lowerCase)
            
def getUpperCase(stringS):
    upperCase = []
    for j in range(len(stringS)):
        if stringS[j] in alphabetUpperCase:
            upperCase.append(stringS[j])
    return sorted(upperCase)

def getOdd(stringS):
    oddNumberList = []
    for k in range(len(stringS)):
        if stringS[k] in oddNumbers:
            oddNumberList.append(stringS[k])
    return sorted(oddNumberList)

def getEven(stringS):
    evenNumberList = []
    for l in range(len(stringS)):
        if stringS[l] in evenNumbers:
            evenNumberList.append(stringS[l])
    return sorted(evenNumberList)

def sortAll(string):
    finalList = getLowerCase(string) + getUpperCase(string) + getOdd(string) + getEven(string)
    return "".join(finalList)

string = raw_input()
print sortAll(string)

