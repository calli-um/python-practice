'''Features to include:
- Ask the user how many numbers they want to enter
- Collect numbers into a list
- Find the maximum and minimum values
- Show both results
- Use a function to do the checking
'''
numList=[]

def minFinder():
    min=numList[0]
    for i in range(len(numList)):
        if numList[i]<min:
            min=numList[i]
    return min
def maxFinder():
    max=numList[0]
    for i in range(len(numList)):
        if numList[i]>max:
            max=numList[i]
    return max

print("How many numbers you want to add in the list?")
total=input();
total=int(total)
for i in range(total):
    print(f'Enter number {i+1}:')
    num=input()
    num=int(num)
    numList.append(num)

print(numList)
min=minFinder()
print(f'Minimum number in the list is {min}')
max=maxFinder()
print(f'Maximum number in the list is {max}')


