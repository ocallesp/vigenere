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

ALPHABET_SIZE = 26
KEY_SIZE = 4
END_STREAMING = '?'

def key_generator(size):
    """ this function will generate a key of a given size

    args:
        size: size of the key"""
    global KEY_SIZE    

    tmp_key = ""

    for i in range(0,size-1):
        pos = random.randint(0, ALPHABET_SIZE)
        tmp_key += ALPHABET[pos]

    KEY = tmp_key

    
def add_more_characters(extra):
    """ this function will add more characters to the default alphabetic

    args:
        extra: these extra characters include numbers, capital letter,
               or other defined characters by the user"""
    global ALPHABET

    if extra == "capital":
        ALPHABET += EXTRA_CAPITAL
    elif extra == "numbers":
        ALPHABET += EXTRA_NUMBERS
    else:
        ALPHABET += extra



if __name__ ==  "__main__":
    global ALPHABET_SIZE
    global KEY_SIZE

    parser = argparse.ArgumentParser(description="Encrypt plain text using Vigenere algorithm")
    parser.add_argument('-k', '--key', help='key used to encrypt the plain text')
    parser.add_argument('-ks','--key-size', help='size of the key to generate')
    parser.add_argument('-p','--pipe', help='name of pipe')
    parser.add_argument('-e','--expand-alphabet',help='add a defined list of characters to the alphabet.\
                  "numbers" - add numbers from 0 to 9, "capital" - add capital letters, or a list of strings')
    parser.add_argument('--eos', help="character to end streaming")

    args = parser.parse_args()

    # check if we need to increase the number of characters in the alphabet
    if args.expand_alphabet != None:
        add_more_characters(args.expand_alphabet)
    ALPHABET_SIZE = len( ALPHABET )


    # if a new key is given, then do not generate a new one
    if args.key != None:
        KEY = args.key
    else:
        if args.key_size != None:
            key_generator(key_size)

    KEY_SIZE = len(KEY)

    # enter the character used to finish communication
    if args.eos != None:
        END_STREAMING = args.eos

    # print some useful information to share with the receiver
    print "ALPHABET: " + ALPHABET
    print "number of characters: " + str( ALPHABET_SIZE )
    print "KEY: " + KEY
    print "size of key: " + str( KEY_SIZE )
    print ""
    print "pipe name : " + PIPE
    print "character to stop streaming: " + END_STREAMING

    # open the pipe and disable buffering
    with open(PIPE,"w",0) as f:
        i = 0
        Xi_character = ""
 
        while Xi_character != END_STREAMING:

            # get one character from console
            Xi_character = raw_input()
            if Xi_character == END_STREAMING:
                f.write( Xi_character )
                continue

            Xi = ALPHABET.find( Xi_character )

            if Xi == -1:
                print "Error -  character not found in alphabet"
                print ALPHABET
                continue

            # repeate the key - pattern
            key_pos = i % KEY_SIZE
            Yi = ALPHABET.find( KEY[key_pos] )

            # apply Vigenere equation
            Zi = (Xi + Yi) % ALPHABET_SIZE
            Zi_character = ALPHABET[Zi]
            # send the encrypted message
            f.write( Zi_character )
            i += 1

    
