#!/usr/bin/env python3
import re
import sys
import argparse
import string

# Checks that the input string (password) follows the following guidelines:
# 1. Password must be at least 14 characters in length
# 2. Password must contain at least one character from each of the following four character sets:
#    * Uppercase characters (string.ascii_uppercase)
#    * Lowercase characters (string.ascii_lowercase)
#    * Numerical Digits (string.digits)
#    * Special Characters (string.punctuation)
# 3. Password cannot contain more than three consecutive characters from the same character set.
# 4. Password cannot contain whitespace characters (string.whitespace)
# 5. Returns True if a valid password. False "), otherwise.

# Output: True/False

parser = argparse.ArgumentParser()
required = parser.add_argument_group('required arguments')
required.add_argument(
    '-w', help="password to check", metavar='', required=True)
args = parser.parse_args()

valid = []
valid.extend(string.punctuation + string.digits + string.ascii_letters)


def passwd_checker(word):
    # print("passwd: " + word)
    if (len(word) < 14):
        print("Password must be at least 14 chars")
        sys.exit(" False ")
    for char in word:
        if char not in valid or char * 3 in word:
            sys.exit(" False ")
    if re.search(r'[\d]', word) is None:
        sys.exit(" False ")
    if re.search(r'[a-z]', word) is None:
        sys.exit(" False ")
    if re.search(r'[A-Z]', word) is None:
        sys.exit(" False ")
    if re.search(r'[!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{\|}~]', word) is None:
        sys.exit(" False ")

    return sys.exit(" True ")


def main():
    passwd_checker(args.w)


if __name__ == '__main__':
    main()
