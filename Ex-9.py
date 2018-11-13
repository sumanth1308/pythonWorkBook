"""
Exercise 9: Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent interest per year.
The interest that you earn is paid at the end of the year, and is added to the balance of the savings account.
Write a program that begins by reading the amount of money deposited into the account from the user.
Then your program should compute and display the amount in the savings account after 1, 2, and 3 years.
Display each amount so that it is rounded to 2 decimal places.
"""
if __name__ == '__main__':
    _amount = float(raw_input("Enter the amount you deposited:"))
    _oneYear = _amount * 1.04
    _twoYears = _oneYear * 1.04
    _threeYears = _twoYears * 1.04
    print "1: %.2f\n2: %.2f\n3: %.2f\n" % (_oneYear, _twoYears, _threeYears)
    