from Formulas import *
from prettytable import PrettyTable


def Secant():
    print("SECANT Method")

    vector = raw_input("Enter constants separated by space: ")
    row = createFunction(vector)

    x0 = raw_input("Enter initial guess 1 (x0): ")
    x1 = raw_input("Enter initial guess 2 (x1): ")

    print "\n--Stopping Criteria--"
    iter = int(input("Iterations: "))
    Fx = float(input("|Fx|: "))
    Error = float(input("|Ea|: "))

    fx0 = truncate(substitute(row, str(x0)))
    fx1 = truncate(substitute(row, str(x1)))
    fxi1 = 100
    Ea = 100
    i = 0

    print "\nTABLE"
    array = PrettyTable()
    array.field_names = ["#", "x(i-1)", "xi", "x(i+1)", "f(xi-1)", "f(xi)", "f(xi+1)", "|Ea|%"]

    for i in range(1, iter + 1):
        Xi1 = truncate(float(x1) - ((fx1 * (float(x1) - float(x0))) / (fx1 - fx0)))
        fxi1 = truncate(substitute(row, str(Xi1)))
        Ea = abs(truncate(((float(Xi1) - float(x1)) / float(Xi1)) * 100))

        data = [str(i), str(x0), str(x1), str(Xi1), str(fx0), str(fx1), str(fxi1), str(Ea) + '%']
        array.add_row(data)

        x0 = x1
        x1 = Xi1
        fx0 = truncate(substitute(row, str(x0)))
        fx1 = truncate(substitute(row, str(x1)))

        if Ea <= Error or fxi1 <= Fx:
            break

    Xi1 = truncate(float(x1) - ((fx1 * (float(x1) - float(x0))) / (fx1 - fx0)))
    fxi1 = truncate(substitute(row, str(Xi1)))
    Ea = abs(truncate(((float(Xi1) - float(x1)) / float(Xi1)) * 100))

    data = [str(i + 1), str(x0), str(x1), str(Xi1), str(fx0), str(fx1), str(fxi1), str(Ea) + '%']
    array.add_row(data)
    print array


def Euler(function, finalX, h, y0, x0):
    print "\nY(i+1) = Yi + f(Xi,Yi)h\n"

    array = PrettyTable()
    array.field_names = ["Step", "X", "Y", "Yi", "Xi"]

    for i in range(100):
        if x0 >= finalX:
            break
        else:
            Fx = function.replace('x', str(truncate(x0)))
            Fx = Fx.replace('y', str(truncate(y0)))
            Fx = truncate(eval(Fx))

            print "i = " + str(i)
            print "f(" + str(truncate(x0)) + "," + str(truncate(y0)) + ") = " + str(Fx)

            y1 = y0 + (Fx * h)
            x1 = x0 + h
            print "y" + str(i + 1) + " = " + str(y0) + " + (" + str(Fx) + ")(" + str(h) + ")"
            print "y" + str(i + 1) + " = " + str(y1) + " ~ y(" + str(x1) + ")\n"

            data = [str(i), str(x0), str(y0), str(y1), str(x1)]
            array.add_row(data)
            x0 = x1
            y0 = y1

    print "\n---TABLE---"
    print array


def Heun(function, finalX, h, y0, x0):
    print "\nFormulas:"
    print "k1 = f(xi,yi)"
    print "k2 = f(xi+h,yi+k1h)"
    print "Y(i+1) = Yi + (1/2 k1 + 1/2 k2)h\n"

    array = PrettyTable()
    array.field_names = ["Step", "X", "Y", "Yi", "Xi"]

    for i in range(100):
        if x0 >= finalX:
            break
        else:
            k1 = function.replace('x', str(truncate(x0)))
            k1 = k1.replace('y', str(truncate(y0)))
            k1 = truncate(eval(k1))

            k2 = function.replace('x', str(truncate(x0 + h)))
            k2 = k2.replace('y', str(truncate(y0 + (k1 * h))))
            k2 = truncate(eval(k2))

            print "i = " + str(i)
            print "k1 = f(" + str(x0) + "," + str(y0) + ") = " + str(k1)
            print "k2 = f(" + str(truncate(x0 + h)) + "," + str(truncate(y0 + (k1 * h))) + ") = " + str(k2)

            y1 = truncate(y0 + (((0.5 * k1) + (0.5 * k2)) * h))
            x1 = truncate(x0 + h)
            print "y" + str(i + 1) + " = " + str(truncate(y0)) + " + (1/2 (" + str(k1) + ")+(1/2 (" + str(
                k2) + ")(" + str(h) + ")"
            print "y" + str(i + 1) + " = " + str(y1) + " ~ y(" + str(x1) + ")\n"

            data = [str(i), str(x0), str(y0), str(y1), str(x1)]
            array.add_row(data)
            x0 = x1
            y0 = y1

    print "\n---TABLE---"
    print array


def Midpoint(function, finalX, h, y0, x0):
    print "(4*1.25)-((2.0*2.0)/1.25)"

    print "\nFormulas:"
    print "k1 = f(xi,yi)"
    print "k2 = f(xi+0.5h,yi+0.5k1h)"
    print "Y(i+1) = Yi + k2h\n"

    array = PrettyTable()
    array.field_names = ["Step", "X", "Y", "Yi", "Xi"]

    for i in range(100):
        if x0 >= finalX:
            break
        else:
            k1 = function.replace('x', str(truncate(x0)))
            k1 = k1.replace('y', str(truncate(y0)))
            k1 = truncate(eval(k1))

            k2 = function.replace('x', str(truncate(x0 + (0.5 * h))))
            k2 = k2.replace('y', str(truncate(y0 + (0.5 * k1 * h))))
            k2 = truncate(eval(k2))

            print "i = " + str(i)
            print "k1 = f(" + str(x0) + "," + str(y0) + ") = " + str(k1)
            print "k2 = f(" + str(truncate(x0 + (0.5 * h))) + "," + str(truncate(y0 + (0.5 * k1 * h))) + ") = " + str(
                k2)

            y1 = truncate(y0 + (k2 * h))
            x1 = truncate(x0 + h)
            print "y" + str(i + 1) + " = " + str(y0) + " + (" + str(truncate(k2)) + ")(" + str(h) + ")"
            print "y" + str(i + 1) + " = " + str(y1) + " ~ y(" + str(x1) + ")\n"

            data = [str(i), str(x0), str(y0), str(y1), str(x1)]
            array.add_row(data)
            x0 = x1
            y0 = y1

    print "\n---TABLE---"
    print array


def Ralston(function, finalX, h, y0, x0):
    print "\nFormulas:"
    print "k1 = f(xi,yi)"
    print "k2 = f(xi+(3/4)h,yi+(3/4)k1h)"
    print "Y(i+1) = Yi + ((1/3)k1 + (2/3)k2)h\n"

    array = PrettyTable()
    array.field_names = ["Step", "X", "Y", "Yi", "Xi"]

    for i in range(100):
        if x0 >= finalX:
            break
        else:
            k1 = function.replace('x', str(truncate(x0)))
            k1 = k1.replace('y', str(truncate(y0)))
            k1 = truncate(eval(k1))

            k2 = function.replace('x', str(truncate(x0 + (0.75 * h))))
            k2 = k2.replace('y', str(truncate(y0 + (0.75 * k1 * h))))
            k2 = truncate(eval(k2))

            print "i = " + str(i)
            print "k1 = f(" + str(x0) + "," + str(y0) + ") = " + str(k1)
            print "k2 = f(" + str(truncate(x0 + (0.75 * h))) + "," + str(truncate(y0 + (0.75 * k1 * h))) + ") = " + str(
                k2)

            y1 = truncate((y0 + ((((1.0 / 3) * k1) + ((2.0 / 3) * k2)) * h)))
            x1 = truncate(x0 + h)
            print "y" + str(i + 1) + " = " + str(truncate(y0)) + " + (1/3(" + str(truncate(k1)) + ") + 2/3(" + str(
                truncate(k2)) + "))(" + str(h) + ")"
            print "y" + str(i + 1) + " = " + str(y1) + " ~ y(" + str(x1) + ")\n"

            data = [str(i), str(x0), str(y0), str(y1), str(x1)]
            array.add_row(data)
            x0 = x1
            y0 = y1

    print "\n---TABLE---"
    print array


