def equation(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d

def find_root(a, b, c, d):
    # 寻找使函数值异号的区间
    l = -100
    r = 100
    
    # 扩大区间直到两端函数值异号
    while equation(a, b, c, d, l) * equation(a, b, c, d, r) > 0:
        l *= 2
        r *= 2
    
    # 二分查找
    for _ in range(60):  # 固定迭代次数保证精度
        mid = (l + r) / 2
        if equation(a, b, c, d, mid) == 0:
            return round(mid, 4)
        elif equation(a, b, c, d, mid) * equation(a, b, c, d, l) > 0:
            l = mid
        else:
            r = mid
    
    return round((l + r) / 2, 4)

a, b, c, d = map(int, input().split())
print(find_root(a, b, c, d))
