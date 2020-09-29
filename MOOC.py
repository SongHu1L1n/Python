
'''  数字转人民币  '''


def divide(num):
    integer = int(num)
    fraction = round((num - integer) * 100)  # round 四舍五入
    return str(integer), str(fraction)


han_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
unit_list = ['十', '百', '千']


def four_to_hanstr(num_str):  # 添加单位
    result = ''
    num_len = len(num_str)
    for i in range(num_len):
        num = int(num_str[i])
        if i != num_len - 1 and i != 0:
            result += han_list[num] + unit_list[num_len - 2 - i]
        else:
            result += han_list[num]
    return result


def integer_to_str(num_str):  # 数字字符串->汉字字符串
    str_len = len(num_str)
    if str_len > 12:
        print('数字太大，无法转换')
        return
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8]) + '亿' + four_to_hanstr(num_str[-8:-4]) + '万' + four_to_hanstr(num_str[-4:])
    elif str_len > 4:
        return four_to_hanstr(num_str[:-4]) + '万' + four_to_hanstr(num_str[-4:])
    else:
        four_to_hanstr(num_str)


def mooc_3_2():
    mon_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 2019
    month = 7
    day = 17
    sum_day = 0
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
    else:
        leap = False
    for i in range(1900, year):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            sum_day += 366
        else:
            sum_day += 365

    for i in range(1, month):
        if i <= 2:
            sum_day += mon_days[i - 1]
        else:
            sum_day += mon_days[i - 1] + leap
    sum_day += day
    week_day = 1 + (sum_day - 1) % 7

    import datetime
    anyady = datetime.datetime(2019, 7, 17).weekday() + 1


def mooc_3_3():
    value = (0, 1)
    candidate = [(A, B, C, D, E) for A in value
                 for B in value
                 for C in value
                 for D in value
                 for E in value]
    for item in candidate:
        count = 0
        if item[0] + item[1] == 2 or item == 0:  # A B都参加 或 A没参加
            count += 1
        if item[1] + item[2] == 1:  # B C 仅有一人参加
            count += 1
        if item[2] == item[3]:  # C D共进退
            count += 1
        if item[3] + item[4] >= 1:   # D E至少一人参加
            count += 1
        if item[0] + item[3] + item[4] == 3 or item[4] == 0: # E A D 一起参加 或 E没参加
            count += 1
        if count == 5:
            print(item)
            break


def mooc_4_1():
    dict1 = {}
    # 统计字符出现频率
    file = open(r'D:\python.mooc.txt', 'rt')
    data = file.readlines()
    for line in data:
        line = line.upper()
        for char in line:
            if 'A' <= char <= 'Z':
                dict1[char] = dict1.get(char, 0) + 1

    file.close()


def mooc_4_2():
    import re
    telnumber = 'suppose my number is 0521-6511888, yours is 010-67676868,and his is 0581-7877777'

    idx = 0
    pa = re.compile('(\d{3,4})-(\d{7,8})')
    while True:
        res = pa.search(telnumber, idx)
        if not res:
            break
        for i in range(3):
            print(res.group(i), res.start(i), res.end(i), sep=' ')
            idx = res.end(i)


class Mooc_5_2:
    def is_prime(self, num):
        import math
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                return False
        return True

    def goldbach(self, n):
        if n < 2 or n % 2 == 1:
            return False
        for i in range(2, n):
            if self.is_prime(i) and self.is_prime(n - i):
                return True
        return False


def mooc_5_3(n):
    v = 1
    list1 = []
    if n < 0:
        n *= -1
        list1.append('-')
    while v <= n // 2:
        v *= 2
    while v > 0:
        if n < v:
            list1.append('0')
        else:
            list1.append('1')
            n -= v
        v //= 2
    return ''.join(list1)


def mooc_5_4():
    import math
    a = math.pi
    for i in range(10):
        a += pow(-1, i) / (2 * i + 1)


def mooc_5_6(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return mooc_5_6(string[1:-1])


def mooc_7_2():
    # 八皇后
    def check(chessboard, row, col):
        for i in range(row):
            for j in range(col):
                if abs(col - chessboard[i]) in (0, abs(row)):
                    return False
        return True

    def eightqueens(chessboard, row):
        count = len(chessboard)
        if row == count:
            print(chessboard)
            return True

        for col in range(count):
            if check(chessboard, row, col):
                chessboard[row] = col
                if eightqueens(chessboard, row + 1):raise 1
        return False

    result = [None] * 8
    try:
        eightqueens(result, 0)
    except:
        pass