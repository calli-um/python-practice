'''You split the string into equal chunks of length k
For each chunk:
Keep only the first occurrence of each character
Preserve order'''

def ignore_duplicates(chunk):
    alr = []
    result = ""
    for letter in chunk:
        if letter not in alr:
            alr.append(letter)
            result += letter
    return result   

def split(s, k):
    k = int(k)  
    if k <= 0:
        print("Input must be greater than 0.")
        return
    if len(s) % k != 0:
        print("Input must be a factor of the string length.")
        return
    for i in range(0, len(s), k):
        chunk = s[i:i+k]
        res = ignore_duplicates(chunk)
        print(res)

s = input("Enter string: ")
print(f"string length: {len(s)}")
k = input("Enter factor of string length (length % factor==0): ")
split(s, k)

