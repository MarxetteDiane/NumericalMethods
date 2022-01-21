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
        print "y" + str(i + 1) + " = " + str(truncate(y0)) + " + (1/2 (" + str(k1) + ")+(1/2 (" + str(k2) + ")(" + str(h) + ")"
        print "y"+str(i+1)+" = " + str(y1) + " ~ y(" + str(x1) + ")\n"

        data = [str(i), str(x0), str(y0), str(y1), str(x1)]
        array.add_row(data)
        x0 = x1
        y0 = y1

print "\n---TABLE---"
print array
