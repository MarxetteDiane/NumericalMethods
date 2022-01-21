from Formulas import *
from prettytable import PrettyTable

# (((y)**2)/(x-1))-(2*x)-5

function = raw_input("Enter function: ")
finalX = float(input("Get the value of y when x = "))
h = float(input("Step size, h = "))
y0 = float(input("Initial value, y0 = "))
x0 = float(input("Initial value, x = "))
x1 = 0
i = 1

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
        print "y"+str(i+1)+" = " + str(y1) + " ~ y(" + str(x1) + ")\n"

        data = [str(i), str(x0), str(y0), str(y1), str(x1)]
        array.add_row(data)
        x0 = x1
        y0 = y1

print "\n---TABLE---"
print array