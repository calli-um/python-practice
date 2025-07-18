#Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

print("Direct Conversion Using .lower()")
string=input("Enter String: ")
string=str(string)
if string.strip():
    lowerCase_Str=string.lower()
    print(lowerCase_Str)
else:
    print("Error: string is empty.")

#using ASCII
#A-Z 65-90
#a-z 97-122
#Difference = 32 
#ord --> ASCII
#chr --> Character

print("Conversion using ASCII")
string=input("Enter String: ")
string=str(string)
lowerCase=""
if string.strip():
    for word in string:
        ascii=ord(word)
        if 65<=ascii<=90:
            lowerCase+=chr(ascii+32)
        else:
            lowerCase+=chr(ascii)
    print(lowerCase)
else:
    print("Error: String is empty.")