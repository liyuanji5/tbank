from sys import stdout

def query(x):
    print(x)
    stdout.flush()
    return input()

def guess_number(n):
    l = 1
    r = n
    while l < r:
        m = (l + r + 1) // 2   
        response = query(m)
        if response == '<':
            r = m - 1
        else:  # response == '>='
            l = m
    print(f'! {l}')

n = int(input())
guess_number(n)
