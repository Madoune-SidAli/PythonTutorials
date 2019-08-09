import re
#in this part we will practice how to create regex ,how to apply regex,using parentheses and the pipe character"|"
#/d to  fetch for a digit, \D = !\d
#/w to fetch alphanumeric digit ,\W = !\w
#\s spaces or tab

sentence = "my phone number is 123-456-7890"
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo= phoneNumberRegex.search(sentence)
print(mo.group())

# #Using parentheses to unscrew the group on subgroups
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo= phoneNumberRegex.search(sentence)
print(mo.group(1))
print(mo.group(2))
#
#Using pipe :
sentence2 = "i love fruits ,i love all sort of berries and i'm big fan of stawberiies  and blueberries"
#which everyone found first return that
friitsRegex = re.compile(r'stawberiies|blueberries')
mo= friitsRegex.search(sentence2)
print(mo.group())

#Optional cases we just use ()?
phoneNumberRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search("my phone number is 456-7890")
print(mo.group())

#Repetition  cases we just use ()*
batregex = re.compile(r'Bat(wo)*man')
mo = batregex.search("i am a Batwowowowowowowoman")
print(mo.group())

#Necessity cases we use ()+ ,at less existe one
batregex = re.compile(r'Bat(wo)+man')
mo = batregex.search("i am a Batwowowoman")
print(mo.group())

#Search for multiple currencies
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumbers = phoneRegex.findall("the nimber of my mom is 123-456-7890 and my father is 789-456-1230")
print(phoneNumbers)

#Alphanumeric cases :
regex = re.compile(r'\w\w\w')
mo = regex.search("9iiw")
print(mo.group())

#Using \W = !\w
regex = re.compile(r'\W\W\W')
mo = regex.search("!!.")
print(mo.group())

#Spaces or tabs
regex = re.compile(r'\s\w+')
spaces = regex.findall("thhis is a little text")
print(spaces)