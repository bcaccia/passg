# Description

A simple command line password generator.

# Usage

To install locally on your machine run:

`pip install passg/`

To uninstall run:

`pip uninstall passg`

Generate a password with a length of 20 characters that includes uppercase and lowercase letters, numbers, and special characters:

`passg -l 20 -up -lo -n -s`

Do the same but omit the letters ABCabc and the numbers 123:

`passg -l 20 -up -lo -n -s -x "ABCabc123"`

Display help:

`passg`

```
Usage: passg.py [OPTIONS]

Options:
  --num_pass INTEGER          set number of passwords to generate  [default:
                              1]
  -l, --length INTEGER RANGE  set length of generated password  [1<=x<=128]
  -up, --upper                include uppercase letters
  -lo, --lower                include uppercase letters
  -n, --num                   include numbers
  -s, --special               include special ascii characters
  -e, --extended              include extended ascii characters
  -p, --punct                 include punctuation
  -q, --quotes                include quotes
  -d, --dashes                include dashes and slashes
  -m, --math                  include math symbols
  -b, --braces                include braces
  -x, --exclude TEXT          items to exclude, case sensitive, surround in ""
  --version                   Show the version and exit.
  --help                      Show this message and exit.
  ```