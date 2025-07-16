'''Today's topics:
- Writing and calling functions (def, return, parameters)
- List basics (append, remove, indexing, slicing)
- Looping through lists (for item in list:)
- Nested if conditions
'''
#writing a function
def myfunc():
    pass    #function body

#calling function
myfunc()

#function parameters
def myNameFunc(myname):
    print(myname)

#passing args when calling function
myNameFunc('sahiba')

#note: no. of parameters must be equal to the no. of args. Else, error.

#aribitrary *args-->use *parameter when you dunno the no. to args to be passed 
def cars(*carName):
    print(carName)

cars('sonata','civic','x7','bughati')

#keyword arguments-->key=value     kwargs
def keyArgs(song1,song2,song3):
    print(f'song 1 is {song1}')
keyArgs(song1='paro',song2='sahiba',song3='obvious')

#arbitrary keyword arguments--**kwargs
def kwArgs(**name):
    print(f'her name is {name["herName"]}')
kwArgs(myName='ayesha',herName='alina')

#defalut parameter value
def defPar(name='ayesha'):
    print(name)
defPar('alina')
defPar()

#passing list as an argument
def list(names):
    for name in names:
        print(name)
homies=['bella','emilly','rose','jena']
list(homies)

#return values
def retFunc():
    return 5
x=retFunc()
print(x)

#positional-only args
def posArgs(x,/):
    print(x)
#posArgs(value=5) error
posArgs(5)

#keyword-only args
def keyFunc(*,x):
    print(x)
keyFunc(x=3) #correct
#keyArgs(3) error

#keyword-only and positional-only combined
def combineFunc(x,y,/,*,m,n):
    print(f'postional-only are {x,y} and keyword-only are {m,n}')
combineFunc(10,11,m='nig',n='nug')

#recursion
def recursiveFunc(x):
    if x>0:
        result = x + recursiveFunc(x-1)
        print(result)
        return result
    else:
        result=0
        return result
print(f'example output {recursiveFunc(6)}')

#lists
names=['ayesha','fatima','zuha','zainab','zuha']
print(names)
print(names[1])
print(len(names))

#list datatypes
intList=[1,2,3,4,5]
print(intList)
strList=['sofa','bed','chair']
print(strList)
print(strList[:3])
print(strList[0:])
boolList=[True,False,False]
print(boolList)
multiList=['ayesha',20,True]
print(multiList)
print(type(multiList))
print(type(intList))

#list constructor
mylist=list(('him','him','him'))
print(mylist)

#append() insert() extend() remove() pop() del clear()
fruits=['apple','peaches','cherry']
print(fruits)
fruits.append('mango')
print(fruits)

fruits.insert(2,'orange')
print(fruits)

quantity=[2,4,5,6,7]
fruits.extend(quantity)
print(fruits)

fruits=['apple','peaches','orange','cherry']
fruits.remove('orange')
print(fruits)

fruits=['apple','peaches','orange','cherry']
fruits.pop(0) #specified index
print(fruits)
fruits.pop() #last item by defalut
print(fruits)

fruits=['apple','peaches','orange','cherry']
del fruits[2] #specified index
print(fruits)
del fruits

fruits=['apple','peaches','orange','cherry']
fruits.clear()
print(fruits)

#looping through list

#for loop
fruits=['apple','peaches','orange','cherry']
for fruit in fruits:
    print(fruit)

#for loop with range
for fruit in range(1,len(fruits)):
    print(fruits[fruit])

#while loop
fruits=['apple','peaches','orange','cherry']
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1

quantity=[2,4,5,6,7]
[print(x) for x in quantity]