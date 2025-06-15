import re

T = int(input().strip())

for i in range(T):
    S= input().strip()
    if any(op + '+' in S for op in ['*', '+', '?']):
        print("False")
    else:
        try:
            re.compile(S)
            print('True')
        except re.error:
            print('False')