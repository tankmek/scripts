#!/usr/bin/env python3
#@
#@@ c0demech
#
## APFT Calculator
import requests
import sys
import re
# Shamelessly using this site
url = 'http://apftscore.com/score.php'
re_points = re.compile(r'\d{2,3}')
re_fscore = re.compile(r'(\d{2,3})</b>')
## Set arbitrary initial values
data ={
  'soldier[0][pu]': 60,
  'soldier[0][su]': 76,
  'soldier[0][ru]': '16:36',
  'soldier[0][age]': 34,
  'soldier[0][gender]': 'Male'
}
#
# Capture values for use in POST
# These were identified from browsing the website
# source code and looking at the form tags
def getInput():
  data.update({'soldier[0][pu]':  check_pu()})
  data.update({'soldier[0][su]':  check_su()})
  data.update({'soldier[0][ru]':  check_run_format()})
  data.update({'soldier[0][age]': check_age()})
  data.update({'soldier[0][gender]': check_gender()})
# Set boundaries for age the
# user can input
def check_age():
  age = int(input("Enter Age:"))
  if age < 17 or age > 100:
      # Retirement after 65 ? 
      print ("Age must be between 17-65")
      exit(1)
  return age
# set limits for input the max
# reps on the APFT chart is 100
# and u can't do less than 0
def check_pu():
    raw = int(input("Enter PU Reps:"))
    if raw < 0 or raw > 100:
        print ("Enter a number between 0-100")
        exit(1)
    return raw
def check_su():
    raw = int(input("Enter SU Reps: "))
    if raw < 0 or raw > 100:
        print ("enter a number between 0-100")
        exit(1)
    return raw
# The website being used expects a colon (:)
# in between the minutes and seconds
# so we check for that here
def check_run_format():
    run_fmt = input("Enter Raw RU (00:00):")
    if ':' not in run_fmt and len(run_fmt) != 5:
        print ("Run time format 00:00")
        exit(1)
    return run_fmt
#simplify the process and only get
#one char for gender and lowercase it
def check_gender():
    gender = (input("Enter Gender (M/F):")).lower()
    if len(gender) > 1:
        print ("Enter single character")
        exit(1)
    if 'm' in str(gender):
        return "Male"
    if 'f' in str(gender):
        return "Female"

def apft_score():
  print ("==========================")
## This is the part that interacts with
## the website sending and receiving
  response = requests.post(url,data)
# Python3 turns what was str data into
# bytes so we need decode() here
  lines = response.content.decode()
  lines = str(lines).split('\n')
  points = re_points.search(lines[33])
  print ("Push Up Points: ", points.group())
  points = re_points.search(lines[35]) 
  print ("Sit  Up Points: ", points.group())
  points = re_points.search(lines[37]) 
  print ("2 Mile  Points: ", points.group())
  points = re_fscore.search(lines[40])
  print ("Score: ", points.groups()[0])

def main():
  if sys.version_info < (3,0):
    print ("Use Python 3")
    exit(1)

  getInput()
  apft_score()


if __name__ == '__main__':
  main()
