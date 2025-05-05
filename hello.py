import itertools

def lb16():
    x = int(input("What's x? "))
    # 生成所有排列（如n=2时生成 (1,2)和(2,1)）
    permutations = list(itertools.permutations(range(1, x+1)))
    all_signed = []  # 用于保存所有带符号的排列
    
    for perm in permutations:
        # 生成所有符号组合（如n=2时生成 (1,1), (1,-1), (-1,1), (-1,-1)）
        for signs in itertools.product((1, -1), repeat=x):
            # 将排列中的每个数字与符号相乘
            signed = [num * sign for num, sign in zip(perm, signs)]
            all_signed.append(signed)  # 添加到结果列表
    
    # 输出总数和所有排列
    print(len(all_signed))
    for item in all_signed:
        print(" ".join(map(str, item)))  # 转换为字符串输出

lb16()
