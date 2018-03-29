#!/usr/bin/env python3
#The function should take one argument, a string containing a password.
import re
import string 
import random
#@ @c0demech // Mechanic
#Checks that the input string (password) follows the following guidelines:
#    1. Password must be at least 14 characters in length
#    2. Password must contain at least one character from each of the following four character sets:
#        * Uppercase characters (string.ascii_uppercase)
#        * Lowercase characters (string.ascii_lowercase)
#        * Numerical Digits (string.digits)
#        * Special Characters (string.punctuation)
#    3. Password cannot contain more than three consecutive characters from the same character set.
#    4. Password cannot contain whitespace characters (string.whitespace)
#    5. Returns True if a valid password. False, otherwise.
## 
#Output: True/False
valid = []
valid.extend(string.punctuation + string.digits + string.ascii_letters)
def passwd_checker(s):
  print("passwd: "+s)
  if (len(s) < 14):
    print("Password must be at least 14 chars")
    return False
# This only allows a string s with valid chars
# and checks for triplets =)
  for p in s:
    if p not in valid or p*3 in s:
      return False
# This is where I check for at least one of the required chars
# ugly but does the job
  if re.search(r'[\d]',  s) is None:
    return False
  if re.search(r'[a-z]', s) is None:
    return False
  if re.search(r'[A-Z]', s) is None:
    return False
  if re.search(r'[!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{\|}~]', s) is None:
    return False
# We only get here if sanity checks all pass  
  return True

def main():
#@standard test
    m = passwd_checker("P@$$w0rd!qwerty123")
    print(m)
#@test with mixed chars
    #p=passwd_checker("0823ru2h0928219h3rih1!!3290r2-r")
    #test w/ really long string
    #length of string is limited to system RAM
    # don't increase X to huge numbers unless you know what you are doing
    X = 18 # change this to increase passwd length not responsible if u make it 1 billion.
    p = passwd_checker(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(X)))
    print(p)
    g = passwd_checker("abcdefghijklmnopq")
    print(g)
#@test for three consecutive chars 
    #q = passwd_checker("0823ru2a77h0928219h3rih1!!32%%%90r2-r")
    #print(q)
#@test for whitespace execution stops
#@use comments to test individual function calls
    s = passwd_checker("jklk!aKjsldflmnaop123")
    print(s)
    t = passwd_checker("jklmnaajfolajfodaaooop")
    print(t)
    v = passwd_checker("jklmnaajfolajfodaaop\n")
    print(v)
#@test for < 14 chars
#    passwd_checker("jklmnop")


if __name__ == '__main__':
  main()
