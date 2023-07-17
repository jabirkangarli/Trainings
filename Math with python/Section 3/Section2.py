from IPython.display import display, Math

# Addition, subtraction, multiplication, division exercises

print(5-(2 / 4)*(3 / 5))

print((4 - 5) / (3 + (5 * 6)))

# using variables in place of numbers
x = 7
y = -2
z = 5

print((3*x) * (4+y))
print(-y - ((x+3)/z))


# Printing out equations in notebook

display('4 + 3 = 7')
display('4 + 3 = ' + str(4 + 3)) or display('4 + 3 =', str(4 + 3))

display(Math('4+3=7'))

x = 4
y = 5

#strings should be used inside of display function
display(Math(str(x) + '+'+x)))