def print_rangoli(size):
    # your code goes here
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    lines = []
    width = (4 * size) - 3
    for i in range(size):
        letters = alpha[size-1:size-i - 1: -1] + alpha[size-i - 1:size]
        lines.append('-'.join(letters).center(width, '-'))
    print('\n'.join(lines + lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)