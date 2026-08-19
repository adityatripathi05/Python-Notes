# Need for regular expression:
'''
- 1) Look for a pattern appearance in a piece of text. Ex.
    - Search in Log data for specific date and time.
    - Check if either the word "color" or the word
    "colour" appears in a document with just one scan.

- 2) Check if an input is in accordance with a given
pattern. Ex.
    - Check whether an email address given by customer
is real or fake.

- 3) Extract specific portions of a text. Ex.
    - Collecting information of persons based on adddress
    pincode.

- 4) Replace portions of text. Ex.
    - Change any appearance of "color" or "colour" with "red".
    - Want to update a particular detail from student
database for all students.

- 5) Split a larger text into smaller pieces.
'''

# Regular Expression: RegEx
'''
- A RegEx is a sequence of characters that defines a
search pattern for searching something in a given text.
- A regular expression can be formed by using the mix of
    - literals(ordinary charcaters)
    - meta-characters(special charcaters)
    - special sequences and sets
    
- Ex. To match a text having 'file,file1,file2' pattern
can be file(1|2) or file/d?
'''

# RegEx Module:
'''
- Python 're' module provides an interface to the regular
expression engine.
- It allows us to compile RegEx into objects and then
perform matches with them.
'''

import re
#print(re.__doc__)

#for i in re.__dict__:
#    print(i)

###########
# compile():
'''
- RegEx are compiled into pattern objects, which have
methods for various operations such as searching for
pattern matches or performing string substitutions.
- Syntax: re.compile(pattern, flags=0)
'''
pattern = re.compile("hello")
#print(pattern)

pattern = re.compile("hello", flags=re.I)
#print(pattern)

###########
# Perform matches:
'''
- Match of pattern in text can be performed in two ways:
    - Apply function on pattern object.
    - Directly use 're' module functions.
'''

###########
# match():
'''
- A match is checked only at the beginning.
- Syntax: obj.match(string[, pos[, endpos]])
- Syntax: re.match(pattern, string, flags=0)
- It returns a Match object on success, None on failure.
'''

txt= '''Good afternoon all, good to see you here.'''

# match word 'good' in txt
pattern = re.compile("good", flags=re.I)
match = pattern.match(txt)
#print(match) #returns match object
#print(match.span())
#print(match.start())
#print(match.end())

match = pattern.match(txt, pos=5)
#print(match)

match = pattern.match(txt, pos=20)
#print(match)

match= re.match("good", txt, flags=re.I)
#print(match)

###########
# search():
'''
- A match is checked throughtout the string.
- Syntax: obj.search(string[, pos[, endpos]])
- Syntax: re.search(pattern, string, flags=0)
- It returns a Match object on success, None on failure.
'''

txt= '''Good afternoon all, good to see you here.'''

pattern = re.compile("good", flags=re.I)
match = pattern.match(txt)
#print(match)

match = pattern.match(txt, pos=5)
#print(match)

############
# finditer()
'''
- Finds all non-overlapping substrings where the match is
found.
- Syntax: obj.finditer(string[, pos[, endpos]])
- Syntax: re.finditer(pattern, string, flags=0)
- Returns all matches as an iterator of the Match object.
'''

txt= '''Good afternoon all, good to see you here.'''

pattern = re.compile("good", flags=re.I)
matches = pattern.finditer(txt)
#for match in matches:
#    print(match)
    
############
# findall():
'''
- Finds all non-overlapping substrings where the match is
found.
- Syntax: obj.findall(string[, pos[, endpos]])
- Syntax: re.findall(pattern, string)
- Returns all matches as a list.
'''

txt= 'Good afternoon all, good to see you here.'

pattern = re.compile("good", flags=re.I)
matches = pattern.findall(txt)
#print(matches)

###########
# split():
'''
- String is split based on the matches of the pattern.
- Syntax: obj.split(string[, maxsplit])
- Syntax: re.split(pattern, string, maxsplit=0)
- Returns a list where the string has been
split at each match.
'''

txt = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

# split txt by newline
pattern = re.compile("\n")
list_= pattern.split(txt)
#print(list_)

list_= pattern.split(txt, 1)
#print(list_)

############
# Metacharacters: In RegEx, there are 12 metacharacters
'''
- Backslash \
- Caret ^
- Dollar sign $
- Dot .
- Pipe symbol |
- Question mark ?
- Asterisk *
- Plus sign +
- Opening parenthesis (
- Closing parenthesis )
- Opening square bracket [
- The opening curly brace {

- NOTE: In order to treat a metacharacter like a literal,
we need to escape it using '\' character.
'''

txt = "This book costs $15."

# match $15
pattern = re.compile("$15") #no matches found
match= pattern.search(txt)
#print(match)
# We need to escape '$' metacharacter

pattern = re.compile("\$15")
match= pattern.search(txt)
#print(match)

############
# Backslash as literal:

txt = """
C:\Windows
C:\Python
C:\Windows\System32
"""

# Find 'C:\Windows\System32' substring in txt having
# windows style directory addresses.
pattern = re.compile("C:\Windows\System32") 
match= pattern.search(txt)
#print(match)

# No match found due to '\' metacharacter. Need to escape it
pattern = re.compile("C:\\Windows\\System32") 
match= pattern.search(txt)
#print(match)

# No match found again because '\' is escape character
# in python as well.
pattern = re.compile("C:\\\\Windows\\\\System32") 
match= pattern.search(txt)
#print(match)

#Or, Using rawstring
pattern = re.compile(r"C:\\Windows\\System32") 
match= pattern.search(txt)
#print(match)

##############
# Character Sets:
'''
- It allow us to define a character sequence that will
match if any of the defined characters on the set is
present.
- To define a character sets, use [ then any accepted
characters, and finally ].
'''

txt = """
Yesterday, I was driving my car without a driving licence.
The traffic police stopped me and asked me for my license.
I told them that I forgot my licence at home. 
"""
# Match all liscence and liscense
pattern = re.compile("licen[cs]e")
match = pattern.findall(txt)
#print(match)

##############
# Chaacter set range:
'''
- It is possible to use the range of a characters.
- Done by leveraging the hyphen symbol (-) between two
related characters. For ex.
    - To match any lowercase letter, use [a-z].
    - To match any single digit, [0-9].
    - To match any lowercase or uppercase letter, use [a-zA-Z].
    - Character sets range [0-385] means [012385].
'''

txt = """
The first season of IPL was played in 2008. 
The second season was played in 2009 in South Africa.
CSK won the title in 2010 and 2011 as well.
MI has also won the title 3 times in 2013, 2015 and 2017.
Last season was played in 2018 and won by CSK.
"""

# Retrieve all the years
pattern = re.compile("[1-9][0-9][0-9][0-9]")
matches= pattern.findall(txt)
#print(matches)

#############
# Negation of character set range:
'''
- We can invert the meaning of a character set by placing
a caret (^) symbol right after [. Ex.
    - To match all characters other than lowercase
    letters, use [^a-z]
'''

txt = """
The first season of IPL was played in 2008. 
The second season was played in 2009 in South Africa.
CSK won the title in 2010 and 2011 as well.
MI has also won the title 3 times in 2013, 2015 and 2017.
Last season was played in 2018 and won by CSK.
"""

# Filter all vowel charcaters:
pattern = re.compile("[^aeiou]")
matches= ''.join(pattern.findall(txt))
#print(matches)

##################
# Predefined Character Sets:
'''
- .  Matches any character except newline

- \d Matches any decimal digit; euivalent to [0-9]

- \D Matches any non-digit character; equivalent to [^0-9]

- \s Matches any whitespace character; equivalent to
[ \t\n\r\f\v]

- \S Matches any non-whitespace character; equivalent to
[^ \t\n\r\f\v]

- \w Matches any alphanumeric character; equivalent to
[a-zA-Z0-9_]

- \W Matches any non-alphanumeric character; equivalent to
[^a-zA-Z0-9_]
'''

txt = """
The first season of IPL was played in 2008. 
The second season was played in 2009 in South Africa.
CSK won the title in 2010 and 2011 as well.
MI has also won the title 3 times in 2013, 2015 and 2017.
Last season was played in 2018 and won by CSK.
"""
# Retrieve all all odd years
pattern = re.compile("\d\d\d[13579]")
matches= pattern.findall(txt)
#print(matches)

# Find all special symbols (non-alphanumeric,
# non-whitespace characters)
match= re.findall("[^\w\s]", txt)
#print(match)

################
# Alteration Set:
'''
- It used to match a single RegEx out of several possible
RegEx.
- Accomplished using the pipe symbol |.
'''

txt = """
the most common conjunctions are and, or and but.
"""
# Find all occurrences of and, or, the in a given text.
pattern = re.compile("and|or|the")
match = pattern.findall(txt)
#print(match)

################
# Quantifiers:
'''
- Quantifiers are the mechanisms to define how a
character, metacharacter, or character set can be
repeated just left to quantifier.
- List of 4 basic quantifers:
    - ?	Question Mark: Optional (0 or 1 repetition)
    - *	Asterisk: Zero or more times repetition
    - +	Plus Sign: One or more times repetition
    - {n,m} Curly Braces: Between n and m times repetition
    both inclusive.
        - {n} Repeated exactly n times.
        - {n,} Repeated at least n times.
        - {,n} Repeated at most n times.
'''

txt = """
I have 2 dogs.
One dog is 1 year old and other one is 2 years old.
Both dogs are very cute! 
"""
# Find all the matches for dog and dogs in the given text.
pattern = re.compile("dogs?")
match = pattern.findall(txt)
#print(match)

txt = """
file1.txt
file_one.txt
file.txt
fil.txt
file.xml
file-1.txt
"""
# Find all filenames starting with 'file' and ending with
# '.txt' .
pattern = re.compile("file[\w-]*\.txt")
match= pattern.findall(txt)
#print(match)

txt = """
file1.txt
file_one.txt
file09.txt
fil.txt
file23.xml
file.txt
"""
# Find all filenames starting with 'file' followed by 1
# or more digits and ending with '.txt'
pattern = re.compile("file\d+\.txt")
match= pattern.findall(txt)
#print(match)

txt = """
555-555-5555
555 555 5555
5555555555
"""
# Match all phone numbers:
pattern = re.compile("\d{3}[-\s]?\d{3}[-\s]?\d{4}")
match= pattern.findall(txt)
#print(match)

txt = """
123143
432
5657
4435
54
65111
"""
# Filter out all 4 or more digit numbers.
pattern = re.compile("\d{4,}")
match= pattern.findall(txt)
#print(match)

#############
# Greedy Behaviour of Quantifiers:
'''
- A greedy quantifier will try to match as much as
possible to have the biggest match result possible.
'''

txt = """
<html>
<head>
<title>Title</title>
</head>
</html>
"""
# Match all HTML tags:
pattern = re.compile("<.*>")
match= pattern.findall(txt)
#print(match)

# Non-Greedy Behaviour:
'''
- A quantifier marked as reluctant will behave like the
exact opposite of the greedy ones.
They will try to have the smallest match possible.
- This can be  requested by adding an extra question mark
to the quantifier. Ex. ??, *? or +?
'''
pattern = re.compile("<.*?>")
match= pattern.findall(txt)
#print(match)

#############
# Boundary Matcher:
'''
- ^ Matches at the beginning of a line
- $ Matches at the end of a line
- \b Matches a word boundary
- \B Matches the opposite of \b.
     i.e, anything that is not a word boundary
- \A Matches the beginning of the input
- \Z Matches the end of the input

- NOTE: Since \b is also an escape sequence for strings
in Python, hence we need to escape it.
'''

txt = """
Lorem Ipsum is simply dummy text of the printing and
typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text
ever since the 1500s.
"""
# Find all occurances of 'and' 'or' 'the'.
pattern = re.compile("and|or|the")
match= pattern.findall(txt)
#print(match)


pattern = re.compile("\\b(and|or|the)\\b")
match= pattern.findall(txt)
#print(match)

txt = """
Name:
Age: 0
Roll No.: 15
Grade: S

Name: Ravi
Age: -1
Roll No.: 123 Name: ABC
Grade: K

Name: Ram
Age: N/A
Roll No.: 1
Grade: G
"""
# Find all lines which start with pattern 'Name:'
pattern = re.compile("^Name: ?\w*")
match= pattern.findall(txt)
#print(match)

# e.M for re.MULTILINE, is a flag which is used to make
# begin/end (^, $) consider each line.
pattern = re.compile("^Name: ?\w*", flags=re.M)
match= pattern.findall(txt)
#print(match)

txt = """
Nature's first green is gold,
Her hardest hue to hold.
Her early leaf's a flower;
But only so an hour."""
# Find all sentences which do not end with a full stop
pattern = re.compile("^.+[^\.]$", flags=re.M)
match= pattern.findall(txt)
#print(match)

#############
# Substitution: sub()
'''
- It's a method which will replace all the leftmost
non-overlapping occurrences of a pattern in a given string
and return the new string as result.
- Syntax: sub(repl, string[, count=0])
- Syntax: re.sub(pattern, repl, string, count=0, flags=0)
'''
txt = "100 cats, 23 dogs, 3 rabbits"
# Replace all occurances of numbers with a '#'
pattern = re.compile("\d+")
newtxt = pattern.sub("#", txt)
#print(newtxt)

##############
# Grouping:
'''
- By placing part of a RegEx inside parentheses (, ), we
can group that part of the regex pattern together.
'''
# Apply a quantifier to the entire group using group:
txt = "abbbbbabbbb"
#match one or more repetitions of ab

pattern1 = re.compile("ab+")
match= pattern1.findall(txt)
#print(match)

pattern2 = re.compile("(ab)+")
match= pattern2.findall(txt)
#print(match)

# Group Capturing using group:
txt="""
https://www.amazon.com/dp/B001E4KFG0
https://www.amazon.com/dp/B006K2ZZ7K
https://www.youtube.com/watch?v=xhD4pQlkoJk
https://www.youtube.com/watch?v=Tqsz6fjvhZM
"""
#Capture the domain name and unique product id
p=re.compile(r'https://www\.([\w-]+)\.com/[\w?]+[/=]([a-zA-Z0-9]+)')
matches = p.finditer(txt)
#for match in matches:
#    print(match.group(1),':',match.group(2))

##################
# Backreferencing using group:
'''
- It allow us to specify in pattern that the contents
of an earlier capturing group must also be found at the
current location in the string.
'''

txt = """
hello hello
how are you
bye bye
"""
# find all the duplicated words:
#pattern = re.compile("(\w+) \\1") #\1 refering to group 1
pattern = re.compile(r"(\w+) \1")
# \1 need to escape because it is python escape sequence also
match=pattern.findall(txt)
#print(match)

txt = """
today is 23/02/2019.
yesterday was 22/02/2019.
tomorrow is 24/02/2019.
"""
#find all dates with format dd/mm/yyy and change them to
# yyyy-mm-dd format.
pattern = re.compile("(\d{2})/(\d{2})/(\d{4})")
newtxt = pattern.sub(r"\3-\2-\1", txt)
#print(newtxt)

##############
# Non-capturing group:
'''
- To make a group non-capturing, syntax (?:pattern)
'''

txt = """
i hate dragons
i love cats
i love dogs
"""
# find the strings 'i love cats' or 'i love dogs'
pattern = re.compile("i love (cats|dogs)")
match= pattern.findall(txt)
#print(match)

# findall() captured part contains only cats or dogs
# instead of complete sentences. Hence use non-capturing group syntax
pattern = re.compile("i love (?:cats|dogs)")
match= pattern.findall(txt)
#print(match)

txt="""
https://www.facebook.com
http://www.grade-up.edu
http://pm-india.gov.in
"""
# Match all website
pattern = re.compile('https?://(?:www\.)?[\w-]+\.(?:com|edu|in|gov)(?:\.\w+)?') 
match = pattern.findall(txt)
#print(match)

txt="""
mrhappy24@gmail.com
mr_happy24@yahoo.in
mr-happy24@adobe-india.co
"""
# Match all mailid
pattern = re.compile('[\w-]+@[\w-]+\.+(?:com|edu|in|co)')
match = pattern.findall(txt)
#print(match)

txt="""
Mr. Nikhil
Mr Nikhil
Ms Deepa
Mrs. Deepa
Mr. D
"""
# Match all names
pattern = re.compile(r'M(?:r|s|rs)\.?\s[A-Z]\w*')
match = pattern.findall(txt)
#print(match)

################
# Look Around: Look ahead and Look behind

################
# Look Ahead: Positive Look Ahead and Negative Look Ahead
'''
- Look ahead mechanism checks the match for a
non-consuming expression ahead of actual RegEx pattern.

- Positive look ahead will succeed if the passed
non-consuming expression does match against the
forthcoming input.
- Syntax: A(?=B) where A is actual, B is non-consuming

- Negative look ahead will succeed if the passed
non-consuming expression does not match against the
forthcoming input.
- Syntax: A(?!B)
'''

txt = """
i love python,
i love regex
"""
# match for 'love' only if it is followed by 'regex'
pattern = re.compile("love(?=\sregex)")
match = pattern.findall(txt)
#print(match)

txt = "My favorite colors are red, green, and blue."
# find all words which are followed by . or ,
pattern = re.compile("\w+(?=,|\.)")
match = pattern.findall(txt)
#print(match)

txt = """
i love python,
i love regex
"""
# match for 'love' only if it is not followed by 'regex'
pattern = re.compile("love(?!\sregex)")
match = pattern.findall(txt)
#print(match)


##############
# Look behind: Positive Look Behind and Negative Look Behind
'''
- Look behind mechanism checks the match for a
non-consuming expression behind a given pattern.
'''

txt = "love regex or hate regex, can't ignore regex"
# find a match for 'regex' only if it is succeeded by
# love or hate.
pattern = re.compile("(?<=(?:love|hate)\s)regex")
match = pattern.findall(txt)
#print(match)

txt = "love regex or hate regex, can't ignore regex"
# find a match for 'regex' only if it is not succeeded by
# love or hate.
pattern = re.compile("(?<!(?:love|hate)\s)regex")
match = pattern.findall(txt)
#print(match)





