import re

def regExp(text):
    # create a regex object
    phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    # pass string to regex object search() method
    mo = phoneNumRegex.search(text)
    # call match object's group() method
    print("Phone Number found: " + mo.group())

# regExp('My number is 415-555-4242.')


# find vowels in an text
def findVowels(text):
    # regex object
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    # method findall returns a list of tuples of strings
    vowels = vowelRegex.findall(text)

    print(vowels)

# findVowels('RoboCop eats baby food. BABY FOOD.')


# matching first and last name with .*
def matchName(text):
    # create a regex object
    nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    # pass a string to search method
    mo = nameRegex.search(text)

    print(mo.group(2))

# matchName('First Name: Ai Last Name: Freeman')

# substituting strings with the sub() method
def hideName(text):
    # create a regex object
    # nameRegex = re.compile(r'name \w+', re.I)
    nameRegex = re.compile(r'name (\w)\w+', re.I)
    # pass a substitute string and the string for regular expression
    mo = nameRegex.sub(r'\1***', text)
    print(mo)

hideName('Drivers Name Joe and the passenger\'s name Doe')