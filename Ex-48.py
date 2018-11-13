'''
Exercise 48: Chinese Zodiac

The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is shown in the table below.
The pattern repeats from there, with 2012 being another year of the dragon, and 1999 being another year of the hare.
Year	Animal
2000	Dragon
2001	Snake
2002	Horse
2003	Sheep
2004	Monkey
2005	Rooster
2006	Dog
2007	Pig
2008	Rat
2009	Ox
2010	Tiger
2011	Hare
Write a program that reads a year from the user and displays the animal associated with that year.
Your program should work correctly for any year greater than or equal to zero, not just the ones listed in the table.
'''

if __name__ == "__main__":
    _ChineseZodiac = {0:'Monkey',1:'Rooster',2:'Dog',3:'Pig',4:'Rat',5:'Ox',6:'Tiger',7:'Hare',8:'Dragon',9:'Snake',10:'Horse',11:'Sheep'}
    try:
        _year = int(raw_input("Enter the year you were born:"))
        if _year<=0:
            print "Please enter the correct year and try again."
        else:
            print 'Your Chinese zodiac animal is ', _ChineseZodiac[_year%12], '.'
    except Exception as X:
        print "Exception raised : ",str(X)