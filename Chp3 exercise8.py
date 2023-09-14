# Initialise variables
hotdog = 10
buns = 8

# Prompt to enter the number of people and the number of hotdog per person
numb = int(input("Number of People: "))
person = int(input("Hot dog per person: "))

# A. Calculating number of packages of required hot dogs
numhotdog = numb * person
pack = numhotdog
leftover = hotdog - numhotdog % hotdog

# Calculating Minimum Number of Packets
if numhotdog // buns == numhotdog:
    bunspack = numhotdog
    bunsleft = 0
else:
    bunspack = numhotdog
    bunsleft = buns - numhotdog % buns

# Printing Results.
print("Minimum Hot dog required.", pack)
print("Minimum Hot dog Buns required.", bunspack)
print("Leftover Hot dog required.", leftover)
print("Leftover Hot dog buns required.", bunsleft)
