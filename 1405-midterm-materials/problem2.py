""" Analyzing sequences of odd numbers program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

def analyze(filename):
    """ Finds the longest sequence of odd numbers in a file """
    full_file = open("/workspaces/midterm_COMP1405/1405-midterm-materials/"
          + filename, "r", encoding="utf8")

    longest_sequence = 0
    current_sequence = 0
    for number in full_file:
        # Removes the new line at the end of the string
        number = int(number[:len(number) - 1])

        # If the number is odd then add to the sequence
        # If is is even then end the sequence
        if number % 2 != 0:
            current_sequence += 1
        else:
            current_sequence = 0

        # If the current sequence is bigger than the longest then it will replace it
        # Even if the current sequence is not completed yet
        if longest_sequence < current_sequence:
            longest_sequence = current_sequence
    return longest_sequence
