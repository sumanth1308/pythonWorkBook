"""
Exercise 10:Arithmetic

Create a program that reads two integers, a and b, from the user.
Your program should compute and display:
- The sum of a and b
- The difference when b is subtracted from a
- The product of a and b
- The quotient when a is divided by b
- The remainder when a is divided by b
- The result of log10 a
- The result of a to the power b
Hint: You will probably find the log10 function in the math module helpful
"""
import math
if __name__ == '__main__':
    a = int(raw_input("Enter number:"))
    b = int(raw_input("Enter number:"))
    print "sum:", a+b
    print "difference:", a-b
    print "product:", a*b
    print "quotient:", a/b
    print "remainder:", a%b
    print "log10 of a:", math.log10(a)
    print "a to the power b:", a**b