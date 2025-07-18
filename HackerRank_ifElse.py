'''Given an integer,n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Constraints
1<=n<=100
'''
n=input("Enter a number:")
try:
        n=int(n)
        if 1<=n<=100:                #check constraint
            if n%2==0:               #check if even
                if n in range(2,6):
                    print("Not Weird")
                elif n in range(6,21):
                    print("Weird")
                elif n>20:
                    print("Not Weird")
            else:                       #odd
                print("Weird")
        else:
            print("Follow Constraint (1-100)")
except:
    print("n must be a valid number")
    
