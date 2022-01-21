from Formulas import *
from prettytable import PrettyTable

# -1 -1 6   <-- 6x^2-x-1
# 2
# 1
# 10
# 0.00001
# 0.005

# 6 -5 1   <-- x^2-5x+6
# 10
# 15
# 10
# 0.00001
# 0.005

print("SECANT Method")

vector = raw_input("Enter equation constants separated by space: ")
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
array.field_names = ["#", "x(i-1)", "xi", "x(i+1)", "f(xi-1)",
                     "f(xi)", "f(xi+1)", "|Ea|%"]

for i in range(1, iter+1):
    Xi1 = truncate(float(x1) - ((fx1 * (float(x1) - float(x0))) / (fx1 - fx0)))
    fxi1 = truncate(substitute(row, str(Xi1)))
    Ea = abs(truncate(((float(Xi1) - float(x1)) / float(Xi1)) * 100))

    data = [str(i), str(x0), str(x1), str(Xi1), str(fx0), str(fx1), str(fxi1), str(Ea) + '%']
    array.add_row(data)

    x0 = x1
    x1 = Xi1
    fx0 = truncate(substitute(row, str(x0)))
    fx1 = truncate(substitute(row, str(x1)))

    if Ea <= Error:
        print "\nStopping criteria is met. Ea is less than or equal to " \
              "the stopping error."
        break
    if fxi1 <= Fx:
        print "\nStopping criteria is met. f(xi+1) is less than or equal " \
              "to the stopping Fx."
        break

print array