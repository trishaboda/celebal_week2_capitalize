# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
tot=0
n=int(input())
shoe_size=list(map(int,input().split()))
n=int(input())
#size,price=map(int,input().split())
c=Counter(shoe_size)
for i in range(n):
    size,price=map(int,input().split())
    if c[size]!=0:
        tot+=price
        c[size]-=1
        
print(tot)