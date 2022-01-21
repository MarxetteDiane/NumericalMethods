import math

def truncate(num):
    num = str(num)
    state = False
    new = ""
    j = 0

    for char in num:
        if char == 'e':
            return float(num)

    for digit in num:
        if j == 5:
            return float(new)
        if state:
            j += 1
            new += digit
        else:
            new += digit
        if digit == '.':
            state = True

    return float(new)

def createFunction(vector):
    matrix = vector.split()
    j = 1
    terms = len(matrix)
    function = ""

    for i in range(terms-1, 1, -1):
        exponent = terms - j
        exponent = str(exponent)
        if i == terms - 1:
            if int(matrix[i]) == 1:
                function = "x^" + exponent
            elif int(matrix[i]) == -1:
                function = "-x^" + exponent
            else:
                function = matrix[i] + "x^" + exponent

        else:
            if int(matrix[i]) == 1:
                function += "+x^" + exponent
            elif int(matrix[i]) == -1:
                function += "-x^" + exponent
            elif int(matrix[i]) > 1:
                function += "+" + matrix[i] + "x^" + exponent
            elif int(matrix[i]) < -1:
                function += "-" + matrix[i] + "x^" + exponent
            else:
                function += matrix[i] + "x^" + exponent
        j += 1

    # for 2nd to last term
    if int(matrix[1]) == 1:
        function += "+x"
    elif int(matrix[1]) == -1:
        function += "-x"
    elif int(matrix[1]) > 1:
        function += "+" + str(matrix[1]) + "x"
    elif int(matrix[1]) < -1:
        function += str(matrix[1]) + "x"

    # for last term
    if int(matrix[0]) > 0:
        function += "+" + str(matrix[0])
    else:
        function += str(matrix[0])

    print function
    return function

def substitute(function,num):
    exp = False
    fx = ""
    char = ""

    for temp in function:
        if temp == '^':
            exp = True
        elif temp == 'x':
            if char.isdigit():
                fx += '*'
            char = temp
            fx += temp
        elif temp.isdigit():
            if exp == False:
                fx += temp
            if exp == True:
                e = "*"+char
                exp = False
                for i in range(int(temp)-1):
                    fx += e
            char = temp
        else:
            fx += temp
            char = temp
    sub = fx.replace('x', num)
    return eval(sub)
