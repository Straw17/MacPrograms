def factorNum(num):
    factorList = []
    num = int(num)
    if num == 0:
        print('This number has no factors.')
        return
    if num < 0:
        neg = True
        num = num * -1
    else:
        neg = False
    for i in range(num):
        num2 = i + 1
        num3 = num/num2
        if neg == True:
            if num3 == int(num3):
                if num2 * -1 not in factorList:
                    factorList.append(num2 * -1)
                    factorList.append(int(num3))
        elif num2 not in factorList:
            if num3 == int(num3):
                factorList.append(num2)
                factorList.append(int(num3))

    for i in range(len(factorList)):
        if i/2 == int(i/2):
            print('(' + str(factorList[i]) + ', ' + str(factorList[i+1]) + ')')

def checkPrime(num):
    factorList = []
    num = int(num)
    for i in range(num):
        num2 = i + 1
        num3 = num/num2
        if num2 not in factorList:
            if num3 == int(num3):
                factorList.append(num2)
                factorList.append(int(num3))
    if num == 0:
        print('Not prime')
    elif num == 1:
        print('Not prime')
    elif len(factorList) == 2:
        print('Prime')
    else:
        print('Not prime')
