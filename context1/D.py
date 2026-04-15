def equation(x):
    return x ** 2 + (x + 1) ** 0.5

c = float(input())
l = 0
r = c ** 0.5

while r - l > 1e-7:  
    mid = (l + r) / 2
    if equation(mid) > c:
        r = mid
    else:
        l = mid

print(round((l + r) / 2, 6))
