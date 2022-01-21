print "Newton's Divided Difference"

xAll = raw_input("Enter x separated by space: ")
yAll = raw_input("Enter f(x) separated by space: ")
x = xAll.split()
y = yAll.split()

String = ""

givenX = float(input("Find f(x) at x = "))

X0 = 0
Y0 = 0
X1 = 0
Y1 = 0
X2 = 0
Y2 = 0
X3 = 0
Y3 = 0

for i in range(len(x)):
    if float(x[i]) > givenX:
        X3 = float(x[i + 1])
        Y3 = float(y[i + 1])
        break
    else:
        X0 = float(X1)
        Y0 = float(Y1)
        X1 = float(x[i])
        Y1 = float(y[i])
        X2 = float(x[i + 1])
        Y2 = float(y[i + 1])

print str(X0) + " " + str(Y0)
print str(X1) + " " + str(Y1)
print str(X2) + " " + str(Y2)
print str(X3) + " " + str(Y3)

b0 = Y0
b01 = Y1
b02 = Y2
b03 = Y3

b1 = (b01-b0)/(X1-X0)
b11 = (b02-b01)/(X2-X1)
b12 = (b03-b02)/(X3-X2)

b2 = (b11-b1)/(X2-X0)
b21 = (b12-b11)/(X3-X1)

b3 = (b21-b2)/(X3-X0)

print "\n" + str(b0) + "  " + str(b1) + "  " + str(b2) + "  " + str(b3)
print str(b01) + "  " + str(b11) + "  " + str(b21)
print str(b02) + "  " + str(b12)
print str(b03)

if b1 > 0:
    b1 = "+(" + str(b1) + "*(" + str(givenX) + "-" + str(X0) + "))"
else:
    b1 = "-(" + str(b1) + "*(" + str(givenX) + "-" + str(X0) + "))"

if b2 > 0:
    b2 = "+(" + str(b2) + "*(" + str(givenX) + "-" + str(X0) + ")*(" + str(givenX) + "-" + str(X1) + "))"
else:
    b2 = "-(" + str(b2) + "*(" + str(givenX) + "-" + str(X0) + ")*(" + str(givenX) + "-" + str(X1) + "))"

if b3 > 0:
    b3 = "+(" + str(b3) + "*(" + str(givenX) + "-" + str(X0) + ")*(" + str(givenX) + "-" + str(X1) + ")*(" + str(givenX)\
         + "-" + str(X2) + "))"
else:
    b3 = "-(" + str(b3) + "*(" + str(givenX) + "-" + str(X0) + ")*(" + str(givenX) + "-" + str(X1) + ")*(" + str(givenX)\
         + "-" + str(X2) + "))"

string = str(b0) + b1 + b2 + b3

print "\n" + string
print "\nf(" + str(givenX) + ") = " + str(eval(string))

# 10 15 20 22.5
# 227.04 362.78 517.35 602.97

# 0 2 5 8 12 15 20 25
# -5 7 70 187 427 670 1195 1870