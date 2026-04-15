n = int(input())
array = list(range(1, n + 1))

for i in range(2, n):  # i 从 2 到 n-1
    array[i], array[i // 2] = array[i // 2], array[i]

print(' '.join(map(str, array)))
