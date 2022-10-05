"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for character in items:

        char = str(character)

        if char in frequencies:
            frequencies[char] = frequencies[char] + 1
        
        else:
            frequencies[char] = 1

    return frequencies