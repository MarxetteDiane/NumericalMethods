
print "Direct Interpolation"

xAll = raw_input("Enter x separated by space: ")
yAll = raw_input("Enter f(x) separated by space: ")
x = xAll.split()
y = yAll.split()
Done = "N"

givenX = float(input("Find f(x) at x = "))

choice = int(input("\n[1] Linear Interpolation\n"
                   "[2] Quadratic Interpolation\n"
                   "[3] Cubic Interpolation\n"
                   "Choice: "))

string = ""

if choice == 1:
    X1 = 0
    Y1 = 0
    X2 = 0
    Y2 = 0

    for i in range(len(x)):
        if float(x[i]) > givenX:
            X2 = x[i]
            Y2 = y[i]
            break
        else:
            X1 = x[i]
            Y1 = y[i]

    print "\nDo Simul Equation/Func in Calculator"
    print "a0 + a1("+X1+") = " + Y1
    print "a0 + a1("+X2+") = " + Y2

    a0 = float(input("\nEnter a0: "))
    a1 = float(input("Enter a1: "))

    if a1 > 0:
        string = str(a0) + "+(" + str(a1) + "*" + str(givenX) + ")"
    else:
        string = str(a0) + "-(" + str(a1) + "*" + str(givenX) + ")"

if choice == 2:
    X1 = 0
    Y1 = 0
    X2 = 0
    Y2 = 0
    X3 = 0
    Y3 = 0

    for i in range(len(x)):
        if float(x[i]) > givenX:
            X3 = float(x[i])
            Y3 = float(y[i])
            break
        else:
            X1 = float(X2)
            Y1 = float(Y2)
            X2 = float(x[i])
            Y2 = float(y[i])

# 1 3 5 8 15
# -18 -2 30 108 430

    print "\nDo Simul Equation/Func in Calculator"
    print "a0 + a1(" + str(X1) + ") + a2(" + str(X1*X1) + ") " + " = " + str(Y1)
    print "a0 + a1(" + str(X2) + ") + a2(" + str(X2*X2) + ") " + " = " + str(Y2)
    print "a0 + a1(" + str(X3) + ") + a2(" + str(X3*X3) + ") " + " = " + str(Y3)

    a0 = float(input("\nEnter a0: "))
    a1 = float(input("Enter a1: "))
    a2 = float(input("Enter a2: "))

    if a1 > 0:
        a1 = "+(" + str(a1) + "*" + str(givenX) + ")"
    else:
        a1 = "-(" + str(a1) + "*" + str(givenX) + ")"

    if a2 > 0:
        a2 = "+(" + str(a2) + "*" + str(givenX) + "*" + str(givenX) + ")"
    else:
        a2 = "-(" + str(a2) + "*" + str(givenX) + "*" + str(givenX) + ")"

    string = str(a0) + a1 + a2

if choice == 3:
    X1 = 0
    Y1 = 0
    X2 = 0
    Y2 = 0
    X3 = 0
    Y3 = 0
    X4 = 0
    Y4 = 0

    for i in range(len(x)):
        if float(x[i]) > givenX:
            X4 = float(x[i+1])
            Y4 = float(y[i+1])
            break
        else:
            X1 = float(X2)
            Y1 = float(Y2)
            X2 = float(x[i])
            Y2 = float(y[i])
            X3 = float(x[i+1])
            Y3 = float(y[i+1])

    print "\nDo Simul Equation/Func in Calculator"
    print "a0 + " + str(X1) + "a1 + " + str(X1*X1) + "a2 + " + str(X1*X1*X1) + "a3 = " + str(Y1)
    print "a0 + " + str(X2) + "a1 + " + str(X2*X2) + "a2 + " + str(X2*X2*X2) + "a3 = " + str(Y2)
    print "a0 + " + str(X3) + "a1 + " + str(X3*X3) + "a2 + " + str(X3*X3*X3) + "a3 = " + str(Y3)
    print "a0 + " + str(X4) + "a1 + " + str(X4*X4) + "a2 + " + str(X4*X4*X4) + "a3 = " + str(Y4)

    a0 = float(input("\nEnter a0: "))
    a1 = float(input("Enter a1: "))
    a2 = float(input("Enter a2: "))
    a3 = float(input("Enter a3: "))

    if a1 > 0:
        a1 = "+(" + str(a1) + "*" + str(givenX) + ")"
    else:
        a1 = "-(" + str(a1) + "*" + str(givenX) + ")"

    if a2 > 0:
        a2 = "+(" + str(a2) + "*" + str(givenX) + "*" + str(givenX) + ")"
    else:
        a2 = "-(" + str(a2) + "*" + str(givenX) + "*" + str(givenX) + ")"

    if a3 > 0:
        a3 = "+(" + str(a3) + "*" + str(givenX) + "*" + str(givenX) + "*" + str(givenX) + ")"
    else:
        a3 = "-(" + str(a3) + "*" + str(givenX) + "*" + str(givenX) + "*" + str(givenX) + ")"

    string = str(a0) + a1 + a2 + a3

print "\n" + string
print "f(" + str(givenX) + ") = " + str(eval(string))

# 0 10 15 20 22.5 30
# 0 227.04 362.78 517.35 602.97 901.67

# 0 2 5 8 12 15 20 25
# -5 7 70 187 427 670 1195 1870