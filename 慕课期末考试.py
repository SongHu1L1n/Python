def func_1(n):
    product, sum_val = 1, 0
    while n:
        n, digit = divmod(n, 10)
        product += digit
        sum_val += digit
    return product - sum_val


def func_2(ls: list):
    def solu_1(ls):
        import collections
        dt = collections.Counter(ls)
        for key in dt:
            if dt[key] != 1:
                return False
        return True

    def solu_2(ls):
        dt = {}
        for i in ls:
            dt[i] = dt.get(i, 0) + 1
        if set(ls) != ls:
            return False
        return True
    

def dunc_3(ls):
    ques = '''
    给定一个非负整数列表lst，返回lst的排序结果，排序要求首先是奇数在前，偶数在后，然后是按照数字从大到小排序。
    '''
    if len(ls) <= 1:
        return ls
    low, high = 0, len(ls) - 1
    while low < high:
        while low < high and ls[high] % 2 == 0:
            high -= 1
        while low < high and ls[low] % 2 == 1:
            low += 1
        if low != high:
            ls[low], ls[high] = ls[high], ls[low]

    def insert(nums, start, end):
        for i in range(start + 1, end + 1):
            if nums[i] < nums[i - 1]:
                temp = nums[i]
                j = i - 1
                while nums[j] > temp and j >= start:
                    nums[j + 1] = nums[j]
                    j -= 1
                nums[j + 1] = temp

    insert(ls, 0, low)
    insert(ls, low + 1, len(ls) - 1)
    print(ls)


def func_4(string):
    ques = '''给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。有效字符串需'''
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in mapping:
            elem = stack.pop() if stack else '#'
            if mapping[char] != elem:
                return False
        elif char == ' ' or char == '':
            continue
        else:
            stack.append(char)
    return not stack