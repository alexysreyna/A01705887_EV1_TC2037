"""
Author: Alexys Reyna
Date: 01/04/2024
Project: Chalkobsa set of words
Purpose of the project: Regex creation for certain words.
"""

import re

# Function that uses re library
def match_regex(string):
    regex = "^a((bra pl.\ ibar)|((d|kr)ab)|(la(m|zor)))$" # Regular expression that I generated
    return re.match(regex, string) # "match" function verifies that the string follows the RE

# Test strings
test_strings = [
    "abra pl. ibar",   # Valid string 1
    "adab",            # Valid string 2
    "akrab",           # Valid string 3
    "alam",            # Valid string 4
    "alazor",          # Valid string 5
    "aabra pl. ibar",  # Invalid string 1
    "abrab pl. ibar",  # Invalid string 2
    "dabr",            # Invalid string 3
    "krabr",           # Invalid string 4
    "lamm",            # Invalid string 5
    "lazr",            # Invalid string 6
]

# Test
for string in test_strings:
    if match_regex(string):
        print(f"'{string}' matches the RE.")
    else:
        print(f"'{string}' does not match the RE.") 