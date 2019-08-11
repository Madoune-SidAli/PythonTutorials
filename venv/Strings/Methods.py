#Indexing
#NB : all the string start by index 0
print("Sid Ali"[0])
print("Madoune"[-1])

#Slicing
# the slice methis has 2 parametres => form the first index to the second one
print("Sid Ali"[0:3]) #return Sid
print("Sid Ali"[4:])  #return ALI

#Concatination
a = 5 + 5
print(a)
print("31" + "31")
#print(5+"51") this will case error because we  cant add string with an integer


#String Methods
#Startwith fonction return True Or False
print("madoune".startswith("mad")) #return True
print("madoune".startswith("sid")) #return False
print("Sid ali".endswith("ali")) #return True
print("Sid ali".endswith("Sid")) #return False

#Tcheking if does it exist ?
sentence = "My name is Madoune Sid ali!"
print("Madoune" in sentence)                #return True
print("Madoune" not in sentence)            #return False

sentence.upper()                            #sentence will be ni uppercase
sentence.lower()                            #sentence will be in lowercase

splitsentence=sentence.split(' ')
print(splitsentence)                    #return ['My', 'name', 'is', 'Madoune', 'Sid', 'ali!']
print(' '.join(splitsentence))          #return My name is Madoune Sid ali!

sentence = "    Hello world!    "
print(sentence.strip())                    #will remove the spaces befor and after Hello world!
print(sentence.lstrip())                   # return "Hello world!      " remove the left space
print(sentence.rstrip())                   # return "     Hello world!"  remove the right space
