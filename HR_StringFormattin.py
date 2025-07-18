'''Given an integer,n, print the following values for each integer n from i=1 to n:
Decimal
Octal
Hexadecimal (capitalized)
Binary'''
num=input("Enter a number (1-99): ")
try:
    num=int(num)
    if 1<=num<=99:
       print(f"{'Decimal':<8}{'Octal':<8}{'Binary':<10}{'Hexadecimal'}") #<8,8,10 for spaces 
       for i in range(1, num + 1):
            dec = i
            octal = oct(i)
            binary = bin(i)
            hexa = hex(i).upper()
            print(f"{dec:<8}{octal:<8}{binary:<10}{hexa}")
    else:
        print("Number is out of range")
except:
    print("Invalid Input")