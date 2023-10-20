"""
encode()	Returns an encoded version of the string

"""
#EXAMPLE 1: ENCODE THE FOLLOWING STRING
var_string_encode ="Straße is a German word"
print("")
print("The encoded variable is : ",var_string_encode.encode())

var_string_encode1 = "This is english"
print("The encoded variable is : ",var_string_encode1.encode())


"""

Syntax
string.encode(encoding=encoding, errors=errors)


Parameter Values
Parameter	Description
encoding	Optional. A String specifying the encoding to use. Default is UTF-8
errors	Optional. A String specifying the error method. Legal values are:
'backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	- ignores the characters that cannot be encoded
'namereplace'	- replaces the character with a text explaining the character
'strict'	- Default, raises an error on failure
'replace'	- replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character

"""

print("")
print("The encoded variable is : ",var_string_encode1.encode(encoding="UTF-8"))
print("The encoded variable is : ",var_string_encode1.encode(encoding="ascii"))



print("")
print("The encoded variable is : ",var_string_encode.encode(encoding="UTF-8"))
#print("The encoded variable is : ",var_string_encode.encode(encoding="ascii")) it is error does not accept ascii parameter

print("")
#the following is from w3schools
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))