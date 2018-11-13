"""
Exercise 41:Note To Frequency

The following table lists an octave of music notes, beginning with middle C, along with their frequencies.

Note	Frequency (Hz)
C4	    261.63
D4	    293.66
E4	    329.63
F4	    349.23
G4	    392.00
A4	    440.00
B4	    493.88

Begin by writing a program that reads the name of a note from the user and displays the note's frequency.
Your program should support all of the notes listed previously.
Once you have your program working correctly for the notes listed previously you should add support for all of the notes from C0 to C8.
While this could be done by adding many additional cases to your if statement, such a solution is cumbersome, inelegant and unacceptable for the purposes of this exercise.
Instead, you should exploit the relationship between notes in adjacent octaves.
In particular, the frequency of any note in octave n is half the frequency of the corresponding note in octave n 1.
By using this relationship, you should be able to add support for the additional notes without adding additional cases to your if statement
"""

if __name__ == '__main__':
    _name = raw_input("Enter the Note:")
    _noteToFreq = {'C':261.63, 'D':293.66, 'E':329.63, 'F':349.23,'G':392.00, 'A':440.00,'B':493.88}
    _note = _name[0].upper()
    _octave = int(_name[1])
    _freq = _noteToFreq[_note]/2 ** (4 - _octave)
    print "The frequency is:", _freq