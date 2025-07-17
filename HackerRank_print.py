'''The included code stub will read an integer,n, from STDIN.
Without using any string methods, try to print the following:
1,2,3…n
Note that "…" represents the consecutive values in between.
Constraints
1<=n<=150
'''
import sys

try:
    n=int(sys.stdin.readline())
    if 1<=n<=150:
        i=1
        while(i<=n):
            if i!=n:
                print(i,end=",")
                i+=1
            else:
                print(i,end="")
                i+=1
    else:
        print("Follow Constraints (1-150)")
except:
    print("error: Input must be a valid number.")
