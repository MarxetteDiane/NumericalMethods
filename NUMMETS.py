from Algorithms import *

print "\nNumerical Methods Algorithms\n"
choice = int(input("[1] Secant\n"
                   "[2] Euler\n"
                   "[3] Heun\n"
                   "[4] Midpoint\n"
                   "[5] Ralston\n"
                   "Choice: "))

print "\n"
if choice == 1:
    Secant()
else:
    function = raw_input("\nEnter function: ")
    finalX = float(input("Get the value of y when x = "))
    h = float(input("Step size, h = "))
    y0 = float(input("Initial value, y0 = "))
    x0 = float(input("Initial value, x = "))

    yn = 'Y'
    while yn == 'Y':
        if choice == 2:
            Euler(function, finalX, h, y0, x0)

        elif choice == 3:
            Heun(function, finalX, h, y0, x0)

        elif choice == 4:
            Midpoint(function, finalX, h, y0, x0)

        elif choice == 5:
            Ralston(function, finalX, h, y0, x0)

        yn = raw_input("\n[Y/N] Solve given with different algorithm? ")
        if yn == 'Y':
            choice = int(input("[2] Euler\n"
                               "[3] Heun\n"
                               "[4] Midpoint\n"
                               "[5] Ralston\n"
                               "Choice: "))

