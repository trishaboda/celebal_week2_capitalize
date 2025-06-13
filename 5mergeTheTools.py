import textwrap
def merge_the_tools(string, k):
    # your code goes here
    c = textwrap.wrap(string, k)
    for i in c:
        print(''.join(list(set(i))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)