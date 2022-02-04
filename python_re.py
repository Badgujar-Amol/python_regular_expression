# using search method
import re

s = "Hello from python"
i = re.search("from", s)
if (i):
    print("string match")
else:
    print("No match found")

# ^ start with string
a = "This is regular expression"
j = re.search("^This", a)
if (j):
    print("string match")
else:
    print("No match found")

# $ end with string
result = re.search("python$", "Hello from python")
if (result):
    print('Match found')
else:
    print('not found')

# using findall method
b = "Hello from python 3.9 version, This is regular expression"
str = re.findall("[a-z]", b)  # lower case
str3 = re.finditer('[a-z]', b)
str1 = re.findall("[A-Z]", b)  # upper case
str2 = re.findall("[0-9]", b)  # digits
print(str3)
print(str)
print(str1)
print(str2)

# using compile method
pattern = re.compile('sir')
res = pattern.findall('hello  sir ')
print(res)
r = pattern.search('sir')
print(r)


# using sub method
sub1 = "hello sir this is python"
res1 = re.sub('sir', 'mam', sub1)
print(res1)

sub2 = 'hello sir this is python and hello sir good morning'
res2 = re.subn('sir', 'mam', sub2)
print(res2)

# using split method
res3 = re.split(' ','hi felix it')
print(res3)
res4 = re.split('sir', 'hi sir from felix it')
print(res4)
res5 = re.split(' ', ' hi sir python is good', maxsplit=3)
print(res5)