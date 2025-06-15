# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
num = sorted(set(map(int, input().split())))

N = int(input())
for _ in range(N):
    c = input().split()
    op = c[0]
    
    if op == "pop":
        if num:
            num.pop(0)  # Remove from beginning
    elif op == "remove":
        try:
            num.remove(int(c[1]))
        except ValueError:
            pass
    elif op == "discard":
        if int(c[1]) in num:
            num.remove(int(c[1]))

print(sum(num))