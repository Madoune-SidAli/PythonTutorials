import re
#Exercise 1:use the regular expression to have a number or more then a space then one or more characters
regex= re.compile(r'\d+\s\w+')
sol = regex.findall("12 apples,10 strawberries,2eggs")
print(sol)

#Exercise 2 :figure all the vowels in a sentences
vowelRegex = re.compile(r'[AEIOUaeiou]')
vowels = vowelRegex.findall("know you can fetch the vowels from this sentence")
print(vowels)

#Exercise 2 :figure all the consonants in a sentences
vowelRegex = re.compile(r'[^AEIOUaeiou]')
vowels = vowelRegex.findall("know you can fetch the vowels from this sentence")
print(vowels)

#Exercise 3 : sentence must begin with  Hello
helloRegex = re.compile(r'^Hello')
mo = helloRegex.search("Hello! i am sid ali")
print(mo.group())

#Exercise 4 : ending wirth number
numberRegex = re.compile(r'\d+$')
mo = numberRegex.search("your numbrr is 54")
print(mo.group())
