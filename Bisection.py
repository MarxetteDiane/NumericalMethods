from Formulas import *
from prettytable import PrettyTable

print("BISECTION Method")

vector = raw_input("Enter equation constants separated by space: ")
row = createFunction(vector)

xl = raw_input("Enter initial xl: ")
xu = raw_input("Enter initial xu: ")

print "\n--Stopping Criteria--"
iter = int(input("Iterations: "))
Fx = float(input("|F(xm)|: "))
Error = float(input("|Ea|: "))

xm = truncate((float(xl)+float(xu))/2)
fxl = truncate(substitute(row, str(xl)))
fxu = truncate(substitute(row, str(xu)))
fxm = truncate(substitute(row, str(xm)))
Ea = 100
oldXm = 0

print "\nTABLE"
array = PrettyTable()
array.field_names = ["#", "xl", "xu", "xm", "f(xl)",
                     "f(xu)", "f(xm)", "|Ea|%"]

for i in range(1, iter+1):

    if Ea == 100:
        Ea = "--"
    else:
        Ea = abs(truncate(((float(xm) - float(oldXm)) / float(xm)) * 100))

    data = [str(i), str(xl), str(xu), str(xm), str(fxl), str(fxu), str(fxm), str(Ea) + '%']
    array.add_row(data)

    if fxl*fxm > 0:
        xl = xm

    if fxl*fxm < 0:
        xu = xm

    oldXm = xm
    xm = truncate((float(xl) + float(xu)) / 2)
    fxl = truncate(substitute(row, str(xl)))
    fxu = truncate(substitute(row, str(xu)))
    fxm = truncate(substitute(row, str(xm)))

    if Ea <= Error:
        print "\nStopping criteria is met. Ea is less than or equal to " \
              "the stopping error."
        break
    if abs(fxm) <= Fx:
        print "\nStopping criteria is met. f(xm) is less than or equal " \
              "to the stopping Fx."
        break

print array
