"""
Exercise 7:Sum of the First n Positive Integers

Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using the formula:
sum = (n)(n + 1)/2
"""
if __name__ == '__main__':
    _n = int(raw_input("Enter a number:"))
    _sum = (_n * _n + 1)/2
    print "Sum: ",_sum