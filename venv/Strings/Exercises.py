#count subtring
def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
        index += 1
    return total

print(count_substring("papa pony and the parcel post problem", "p"))



#is_substring(param1,param2) return True if param1 part of param2 otherwise false
def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False

print(is_substring('oo', 'book'))


#String to Integer
"""In this next exercise, your goal is to write a program that asks the user
for three numbers, adds those numbers up, and then prints a message saying what the sum is. """
n1 = input("Enter a number: ")
n2 = input("Enter another number: ")
n3 = input("Enter a third number: ")
sum = int(n1) + int(n2) + int(n3)

#There are two  cases :
#The First One is :
print(f"{n1} + {n2} + {n3} = {sum}")

#The Second one is  :
print(n1 + ' + ' + n2 + ' + ' + n3 + ' = ' + str(sum))
