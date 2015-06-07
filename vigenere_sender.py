#!/usr/bin/python

import sys
import argparse
import random

# default values
PIPE = "buffer"
KEY = "hola"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
EXTRA_NUMBERS = "0123456789"
EXTRA_CAPITAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def key_generator(size):
    """ this function will generate a key of a given size

    args:
        size: size of the key"""
    

    
def add_more_characters(extra):
    """ this function will add more characters to the default alphabetic

    args:
        extra: these extra characters include numbers, capital letter,
               or other defined characters by the user"""
    global ALPHABET


    if extra == "capital":
        ALPHABET = ALPHABET + EXTRA_CAPITAL
    elif extra == "numbers":
        ALPHABET = ALPHABET + EXTRA_NUMBERS
    elif extra == "":
        ALPHABET = ALPHABET 
    else:
        ALPHABET = ALPHABET + extra

if __name__ ==  "__main__":
    parser = argparse.ArgumentParser(description="Encrypt text with Vigenere algorithm")
    parser.add_argument('--key', help='key help')
    args = parser.parse_args()


    add_more_characters("")
    
    print "ALPHABET: " + ALPHABET
    print "number of characters: " + str( len(ALPHABET) )
    print "KEY: " + KEY
    print "size of key: " + str( len(KEY) )

    with open(PIPE,"w",0) as f:
        
        for i in range(0,10):
            Xi_character = raw_input()
            Xi = ALPHABET.find( Xi_character )
            key_pos = i % 4
            Yi = ALPHABET.find( KEY[key_pos] )
            Zi = (Xi + Yi) % 26
            Zi_character = ALPHABET[Zi]
            f.write( Zi_character )


    
