from array import *
from Formulas import *
from terminaltables import AsciiTable

# Problem Set 2
# 2 4 -1 3
# 5 -1 1 -8
# 3 2 7 35

# Class Discussion Sample
# 25 5 1 106.8
# 64 8 1 177.2
# 144 12 1 279.2

print "Enter equation constants separated by space: " \
      "[Ax^2 + Bx + C = D] -> [A B C D]\n"
eq1 = raw_input("Enter vector 1: ")
eq2 = raw_input("Enter vector 2: ")
eq3 = raw_input("Enter vector 3: ")

eq1 = eq1.split()
eq2 = eq2.split()
eq3 = eq3.split()

eq1.insert(3, ":")
eq2.insert(3, ":")
eq3.insert(3, ":")
print "\n"

# initial matrix
matrix = [eq1, eq2, eq3]

table = AsciiTable(matrix)
table.inner_row_border = True
print(table.table)

# matrix 2
div = float(matrix[1][0])/float(matrix[0][0])
print "= " + str(div)
print "\n"

row = str(float(matrix[0][0]) * float(div)) + " " + \
      str(float(matrix[0][1]) * float(div)) + " " + \
       str(float(matrix[0][2]) * float(div)) + " : " + \
      str(float(matrix[0][4]) * float(div))
row = row.split()

eq2 = str(float(matrix[1][0]) - float(row[0])) + " " + \
      str(float(matrix[1][1]) - float(row[1])) + " " + \
       str(float(matrix[1][2]) - float(row[2])) + " : " + \
      str(float(matrix[1][4]) - float(row[4]))
eq2 = eq2.split()

matrix = [eq1, eq2, eq3]

table = AsciiTable(matrix)
table.inner_row_border = True
print(table.table)

# matrix 3
div = float(matrix[2][0])/float(matrix[0][0])
print "= " + str(div)
print "\n"

row = str(float(matrix[0][0]) * float(div)) + " " + \
      str(float(matrix[0][1]) * float(div)) + " " + \
       str(float(matrix[0][2]) * float(div)) + " : " + \
      str(float(matrix[0][4]) * float(div))
row = row.split()

eq3 = str(float(matrix[2][0]) - float(row[0])) + " " + \
      str(float(matrix[2][1]) - float(row[1])) + " " + \
       str(float(matrix[2][2]) - float(row[2])) + " : " + \
      str(float(matrix[2][4]) - float(row[4]))
eq3 = eq3.split()

matrix = [eq1, eq2, eq3]

table = AsciiTable(matrix)
table.inner_row_border = True
print(table.table)

# matrix 4
div = float(matrix[2][1])/float(matrix[1][1])
print "= " + str(div)
print "\n"

row = str(float(matrix[1][0]) * float(div)) + " " + \
      str(float(matrix[1][1]) * float(div)) + " " + \
       str(float(matrix[1][2]) * float(div)) + " : " + \
      str(float(matrix[1][4]) * float(div))
row = row.split()

eq3 = str(float(matrix[2][0]) - float(row[0])) + " " + \
      str(float(matrix[2][1]) - float(row[1])) + " " + \
       str(float(matrix[2][2]) - float(row[2])) + " : " + \
      str(float(matrix[2][4]) - float(row[4]))
eq3 = eq3.split()

matrix = [eq1, eq2, eq3]

table = AsciiTable(matrix)
table.inner_row_border = True
print(table.table)

# Back Substitution
a3 = float(matrix[2][4])/float(matrix[2][2])
a2 = (float(matrix[1][4])-(float(matrix[1][2])*float(a3)))/float(matrix[1][1])
a1 = (float(matrix[0][4])-(float(matrix[0][2])*float(a3))-(float(matrix[0][1])*float(a2)))/float(matrix[0][0])

print "\na1 = " + str(truncate(a1))
print "a2 = " + str(truncate(a2))
print "a3 = " + str(truncate(a3))
