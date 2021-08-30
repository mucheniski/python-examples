name = str("Diego Mucheniski")
print(name[0])
print(name[4])

# Last element is index -1
print(name[-1])
print(name[-2])

# Combine string
print(name[1:4])

# Only second variables
print(name[::2])

print(len(name))


print(name + " it's me")

print(3*name)

print("Test \n new line")
print("Test \t tab")
print("Test \\ backslash")
print(r"Test backslash \ another way")

# whe we apply a method in a string a new string are created
a = str("text to string a")
b = a.upper()
print(a)
print(b)

a = str("text to string a")
b = a.replace("string", "xbacon")
print(a)
print(b)

a = str("text to string a")
b = a.find("ext")
c = a.find("dont exist")
print(a)
print(b)
#  -1 because the text don't exist
print(c)

# Even elements
numbers = "0123456"
print(numbers[::2])

print("0123456".find("1"))