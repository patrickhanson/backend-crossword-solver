#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

"""Crossword Solver Program"""

__author__ = "patrickhanson"


# YOUR HELPER FUNCTION GOES HERE
def find_words(user_input, dictionary):
    input_word = user_input.replace(' ', '.')
    regex_word = re.compile(input_word)
    for word in dictionary:
        if len(user_input) == len(word):
            if re.match(regex_word, word):
                print word


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input("""
        'Please enter a word to solve.
        Use spaces to signify unknown letters: """).lower()

    find_words(test_word, words)
    # YOUR ADDITIONAL CODE HERE
    # raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()
