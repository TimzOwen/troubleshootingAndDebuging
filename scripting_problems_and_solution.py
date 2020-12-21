# Meeting email reminder
# Fix the issue of some meetings not working

meeting_info = $(zenity --forms\
    --title 'Meeting'--text 'Reminder information'\
    --add-calender 'Date' --add-entry 'Title' \
    --add-entry 'Emails'\
    2>/dev/null)
# soln trial 1(print to check if info is well generate)
echo $meeting_info
if [[ -n "$meeting_info" ]]; then
    python3 send_reminders.py "meeting info"
fi

# check the configuration and fix the python script for the correct date formating




# The compare_strings function is supposed to compare just the alphanumeric content of two strings,
# ignoring upper vs lower case and punctuation.
# But something is not working. Fill in the code to try to find the problems, then fix the problems.


import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  # Ignore punctuation
  punctuation = r"[.?!,;:-']"
  string1 = re.sub(punctuation, r"", string1)
  string2 = re.sub(punctuation, r"", string2)

  # DEBUG CODE GOES HERE
  print(___)

  return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False

# soln
import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  #Ignore punctuation
  punctuation =r"[.?!,;:0-9']"
  string1 = re.sub(punctuation, r"", string1)
  string2 = re.sub(punctuation, r"", string2)

  #DEBUG CODE GOES HERE
  print(string1)
  print(string2)

  return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False



# problem 2

# The datetime module supplies classes for manipulating dates and times, and contains many types, objects,
# and methods. You've seen some of them used in the dow function, which returns the day of the week for a
# specific date. We'll use them again in the next_date function, which takes the date_string parameter in
# the format of "year-month-day", and uses the add_year function to calculate the next year that this date
# will occur (it's 4 years later for the 29th of February during Leap Year, and 1 year later for all other
# dates). Then it returns the value in the same format as it receives the date: "year-month-day".

# Can you find the error in the code? Is it in the next_date function or the add_year function? How can you determine
# if the add_year function returns what it's supposed to? Add debug lines as necessary to find the problems,
# then fix the code to work as indicated above.

import datetime
from datetime import date

def add_year(date_obj):
  try:
    new_date_obj = date_obj.replace(year = date_obj.year + 1)
  except ValueError:
    # This gets executed when the above method fails, 
    # which means that we're making a Leap Year calculation
    new_date_obj = date_obj.replace(year = date_obj.year + 4)
  return new_date_obj

def next_date(date_string):
  # Convert the argument from string to date object
  date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
  next_date_obj = add_year(date_obj)

  # Convert the datetime object to string, 
  # in the format of "yyyy-mm-dd"
  next_date_string = next_date_obj.strftime("yyyy-mm-dd")
  return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today))) 
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29



# Soln
import datetime
from datetime import date

def add_year(date_obj):
  try:
    new_date_obj = date_obj.replace(year = date_obj.year + 1)
  except ValueError:
    # This gets executed when the above method fails, 
    # which means that we're making a Leap Year calculation
    new_date_obj = date_obj.replace(year = date_obj.year + 4)
  return new_date_obj

def next_date(date_string):
  # Convert the argument from string to date object
  date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
  next_date_obj = add_year(date_obj)

  # Convert the datetime object to string, 
  # in the format of "yyyy-mm-dd"
  next_date_string = next_date_obj.strftime("%Y-%m-%d")
  return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today))) 
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29



def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

# Binary search syntax
def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

