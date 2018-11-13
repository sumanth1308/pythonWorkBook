'''
Exercise 60: Roulette Payouts
A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two are green. The green spaces are numbered 0 and 00.
The red spaces are numbered 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36.
The remaining integers between 1 and 36 are used to number the black spaces.
Many different bets can be placed in roulette. We will only consider the following subset of them in this exercise:
-	Single number (1 to 36, 0, or 00)
-	Red versus Black
-	Odd versus Even (Note that 0 and 00 do not pay out for even)
-	1 to 18 versus 19 to 36

Write a program that simulates a spin of a roulette wheel by using Python's random number generator.
Display the number that was selected and all of the bets that must be payed.
For example, if 13 is selected then your program should display
The spin resulted in 13... Pay 13
Pay Black Pay Odd Pay 1 to 18
If the simulation results in 0 or 00 then your program should display Pay 0 or
Pay 00 without any further output.
'''
import random

if __name__ == '__main__':
    _red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    _black = [i for i in range (1,37) if i not in _red]
    _green = ['0','00']
    _number =  random.choice(_red+_black+_green)
    print "the Number is ", _number
    if _number in _red:
        print "pay black ",
    elif _number in _black:
        print "pay red ",
    elif _number in _green:
        print "pay green ",
    else:
        pass
    
    if _number in range(1,19):
        print "pay 1 to 18 ",
    elif _number in range(19,37):
        print "pay 19 to 36 ",
    else:
        pass
    if str(_number) in '0'or str(_number) in '00':
        pass
    elif _number%2 == 0:
        print "pay Even ",
    elif _number%2 != 0:
        print "pay Odd "
    else:
        pass
        