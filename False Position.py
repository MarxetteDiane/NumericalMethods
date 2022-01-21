from Formulas import *
from prettytable import PrettyTable

print("FALSE POSITION Method")

vector = raw_input("Enter equation constants separated by space: ")
row = createFunction(vector)

xl = raw_input("Enter initial xl: ")
xu = raw_input("Enter initial xu: ")

print "\n--Stopping Criteria--"
iter = int(input("Iterations: "))
Fx = float(input("|F(xr)|: "))
Error = float(input("|Ea|: "))

fxl = truncate(substitute(row, str(xl)))
fxu = truncate(substitute(row, str(xu)))
xr = truncate(((float(xu)*float(fxl))-(float(xl)*float(fxu)))/(float(fxl)-float(fxu)))
fxr = truncate(substitute(row, str(xr)))
Ea = 100
oldXr = 0

print "\nTABLE"
array = PrettyTable()
array.field_names = ["#", "xl", "xu", "xr", "f(xl)",
                     "f(xu)", "f(xr)", "|Ea|%"]

for i in range(1, iter+1):

    if Ea == 100:
        Ea = "--"
    else:
        Ea = abs(truncate(((float(xr) - float(oldXr)) / float(xr)) * 100))

    data = [str(i), str(xl), str(xu), str(xr), str(fxl), str(fxu), str(fxr), str(Ea) + '%']
    array.add_row(data)

    if fxl*fxr > 0:
        xl = xr

    if fxl*fxr < 0:
        xu = xr

    oldXr = xr
    fxl = truncate(substitute(row, str(xl)))
    fxu = truncate(substitute(row, str(xu)))
    xr = truncate(((float(xu)*float(fxl))-(float(xl)*float(fxu)))/(float(fxl)-float(fxu)))
    fxr = truncate(substitute(row, str(xr)))

    if Ea <= Error:
        print "\nStopping criteria is met. Ea is less than or equal to " \
              "the stopping error."
        break
    if abs(fxr) <= Fx:
        print "\nStopping criteria is met. f(xm) is less than or equal " \
              "to the stopping Fx."
        break

print array
