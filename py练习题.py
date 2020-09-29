def dive():
    a, b = eval(input('输入正整数a, b:'))
    a, b = divmod(a, b)
    print('{0}为商，{1}为余数'.format(a, b))


def distance():
    #  输入两个平面上坐标点，计算距离
    toks = input('依次输入坐标值：x1, y1, x2, y2').split(',')
    x1, y1, x2, y2 = float(toks[0]), float(toks[1]), float(toks[2]), float(toks[3])
    destance = pow((pow(x1 - x2, 2) + pow(y1 - y2, 2)), 0.5)


#  显示当前北京时间

def findout_time():
    import time
    localtime = time.localtime(time.time())
    print()


def drink():
    question = '''一只大象口渴了，要喝20升水才能解渴，但现在只有一个深h厘米，底面半径为r厘米的小圆桶(h和r都是整数)。\
    问大象至少要喝多少桶水才会解渴。编写程序输入半径和高度，输出需要的桶数（一定是整数）'''
    r, h = eval(input('输入桶的半径和高度r, h(单位为cm):'))
    import math
    a = math.ceil(20000 / (math.pi * pow(r, 2) * h))  # 向上取整
    print('大象需要喝{:d}桶水'.format(a))
    #  https://www.cnblogs.com/fat39/p/7159881.html  学习


class Random:
    def reverse(self):
        question = '''产生一个随机3位正整数，并将该整数的数字首尾互换输出，例如：157 互换后为 751。'''
        import random
        num = random.randint(100, 999)
        res = 0
        for i in range(3):
            a = num % 10
            num //= 10
            res = res * 10 + a


class Triangle:
    def calculate_Area(self):
        question = '''
        编写一个程序，提示用户输入三角形的三个顶点(x1,y1)、（x2,y2）、（x3,y3），然后计算三角形面积，这里假定输入的三个点能构成三角形。\
        将面积输出到屏幕，要求占7列，保留2位小数，左对齐。三角形面积公式如下:
        T =(l1 + l2 + l3) / 3, s = (T(T - l1) (T - l2 ) (T - l3)) ** 0.5 ;l1, l2 l3 为边长
        '''
        length = lambda a, b: pow((pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)), 0.5)
        (x1, y1) = eval(input('三角形第一个顶点：'))
        (x2, y2) = eval(input('三角形第二个顶点：'))
        (x3, y3) = eval(input('三角形第三个顶点：'))
        side1 = length((x1, y1), (x2, y2))
        side2 = length((x1, y1), (x3, y3))
        side3 = length((x2, y2), (x3, y3))
        T = (side1 + side2 + side3) / 2
        area = pow((T * (T - side1) * (T - side2) * (T - side3)), 0.5)
        print('三角形的面积为{:<7.2f}'.format(area))


def rate():
    question = '''
    假设每月存100元到一个年利率为6%的储蓄账户。因此，月利率为0.06/12=0.005。
    第一个月后，账户的存款金额为: 100*(1+0.005)=100.5
    第二个月后，账户的存款金额为: (100+100.5)*(1+0.005)=201.5025
    第三个月后，账户的存款金额为: (100+201.5025)(1+0.005)=303.3115
    请编写程序计算5个月后，该储蓄账户的存款金额是多少，并显示在屏幕上，要求保留5位小数，右对齐。\
    计算总体收益相对总体本金的收益率(此收益率值：总收益/总本金)，并显示在屏幕上，要求以百分数形式显示，保留2位小数，右对齐
    '''
    month = int(input('请输入月数：'))
    money, balance = 0, 0

    for i in range(month):
        money += 100  # 总投入有本金
        balance += 100  # 本金 + 利息
        balance *= (1 + 0.05)

    print('余额为:%.5f' % balance)
    profit = balance - money
    profit_rate = profit / money
    print('收益率为：%.2f%%' % (profit_rate * 100))


def position_sum():
    question = '''从键盘输入一个3位整数，请编写程序计算三位整数的各位数字之和，并输出到屏幕上，要求输出站4列，右对齐'''
    a = num = int(input('输入三位整数：'))
    sum = 0
    for i in range(3):
        sum += num % 10
        num //= 10
    print('{0:4}的各位数字之和为{1:4}'.format(a, sum))

################################
def complex_num():
    question = '''请编写一个程序，产生两个[10,50]之间的随机数，\
    用这两个数构造一个复数，计算复数的模、辐角(要求转换成角度)，最后将复数、复数的模和辐角显示在屏幕上。\
    要求每个占7列，右对齐。'''
    import random
    a = random.uniform(10, 50)
    b = random.uniform(10, 50)
    x1 = complex(a, b)
    x2 = complex(b, a)
    import cmath
    m1, n1 = cmath.polar(x1)  # 极坐标
    m2, n2 = cmath.polar(x2)
    print('复数1为：{0:>7.2f},它的模和辐角为：{1:7.2f}和{2:7.2f}'.format(x1, m1, n1))
    print('复数2为：{0:>7.2f},它的模和辐角为：{1:7.2f}和{2:7.2f}'.format(x2, m2, n2))

################################
def past_time():
    ###
    question = '''请计算当前距离1970年1月1日过去了多少天又多少小时，并输出到屏幕上'''
    import time
    time = time.time()
    d = time // 86400  # 天数
    h = time % 86400 / 3600
    print('当前距离1970年1月1日过去了{0}天又{1}小时'.format(d, h))


def equation():
    question = '''从键盘输入三个浮点数a、b和c，求解ax2+bx+c=0的解，并将结果输出到屏幕上。\
    在求解过程中，需要考虑a等于0的无意义情况并给出相应提示信息，同时需要考虑有实数解和无实数解的两种不同的情况。\
    （注：当有实数解时不允许使用复数形式来表示结果）。结果（含负数解的实部和虚部）的显示格式要求为：小数部分5列（不含小数点），整个数占10列。'''
    nums = input("输入三个浮点数，以','分隔：").split(',')
    a, b, c = eval(nums[0]), eval(nums[1]), eval(nums[2])
    if a == 0:
        print('Error，二项式系数为0')
    else:
        d = pow(b, 2) - 4 * a * c
        x1 = (0 - b + pow(d, 0.5)) / (2 * a)
        x2 = (0 - b - pow(d, 0.5)) / (2 * a)

        if d > 0:
            print('当a = {0}, b = {1}, c = {2}时，方程的实数解为：x1 = {3}, x2 = {4}'.format(a, b, c, x1, x2))
        elif d == 0:
            print('当a = {0}, b = {1}, c = {2}时，方程的两个相等的根：x1 = x2 = {3}'.format(a, b, c, x1))
        elif d < 0:
            print('当a = {0}, b = {1}, c = {2}时，方程无解，两根分别为：x1 = {3:10.5f}, x2 = {4:10.5f}'.format(a, b, c, x1, x2))


def triangle():
    nums = input("请输入三个坐标，坐标之间以';'分隔， 坐标内部以',分隔'").split(';')
    (x1, y1), (x2, y2), (x3, y3) = eval(nums[0]), eval(nums[1]), eval(nums[2])
    if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
        print('不能构成三角形')
    else:
        import math
        side1 = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        side2 = math.sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2))
        side3 = math.sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2))
        s = (side3 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        print('面积：{0}, 周长：{1}'.format(area, s * 3))


def alpha(string):
    question = '从键盘输入一个字母，如果输入的是小写英文字母，请将其转换为大写字母后显示输出；\
    如果输入的是大写英文字母，请将其转换为小写字母后显示输出；如果既不是小写英文字母、也不是大写英文字母，则原样显示。'
    for char in string:
        if char.isalpha():
            print(char.swapcase())
        else:
            print(char)


def game():
    question = '''假设数字0表示剪刀，1表示布，2表示石头；\
    请编写程序产生一个[100,999]之间的随机整数，根据随机整数的十位上的数字对3求余的值表示石头、剪刀和布。\
    现在提示用户输入数字0、1或2，判断计算机与用户之间谁赢？并输出结果。'''
    import random
    rule = ((0, 1), (2, 0), (1, 2))
    people = input('输入0或1或2：')
    random_num = random.randint(100, 999)
    computer = (random_num // 10 % 10) % 3
    if people == computer:
        print('平手')
    elif (computer, people) in rule:
        print('computer')
    else:
        print('people')


def multiplication_table(n):
    question = '''
    输出一个乘法表。要求输入一个整数n,输出n*n的乘法表，乘法表打印出来为下三角样式，格式工整。
    '''
    a = '————'
    print('    ', end='')
    for row in range(1, n + 1):
        print('{:4d}'.format(row), end='')
    print('\n    {}'.format(a * (n + 1)))
    for row in range(1, n + 1):
        print('{}:4d'.format(row), end='')
        for col in range(1, row + 1):
            print('{:4d}'.format(row * col), end='')
        print('')


def hexagon(length):
        question = '''
        用*输出一个正六边形，\
        输入一个整数length代表输出的正六边形的边的长度(*的数目)。
        '''
        for i in range(1, 2 * length):
            print('  ' * abs(length - i), ' *  ' * (2 * length - 1 - abs(length - i)))


def e20(n):
    question = '''输出一个等边三角形'''
    p = ''
    for i in range(1, n + 1):
        p += '  * '
        print('  ' * (n - i), p)


def circle_input():
    question = '''
    循环提示用户输入一个整型数字n）（n代表后续需要输入整型数的数量，将n个整型数加起来并输出，\
    如果输入的是非整型数则提示当前的输入非法需要重新输入数值，如果输入‘n=0’代表退出程序，否则继续提示用户输入新的n
    '''
    num = eval(input('int:'))
    while type(num) != int:
        num = eval(input('int:'))
    else:
        i = 1
        sum_value = 0
        while num != 0:
            while i <= num:
                j = eval(input('输入第{}个整数'.format(i)))
                if type(j) == input():
                    i += 1
                    sum_value += j
                else:
                    print('重新输入!')
                    continue
            print('这{0}个整型的和为：{1}'.format(num, sum_value))
            num = eval(input('输入一个整数（0将结束输入）：'))
            while type(num) != int:
                num = eval(input('int:'))
            else:
                i = 1
                sum_value = 0


def prime(number):
    question = '''
    提示用户输入一个整数n,然后输出[1,n）内的所有的素数。\
    提示：质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数的数称为质数。
    '''
    import math
    for num in range(2, number):
        i = 2
        while i < math.sqrt(number):
            if num % i == 0:
                break
            else:
                i += 1
        if i > math.sqrt(number):
            print(num, end='')


def char_expression(num, count):
    question = '''
    求 的值。其中a是一个数字。a和n都是由键盘输入。例如：求S=2+22+222+2222+22222+222222, 那么a=2且n=6
    '''
    data = num
    sum_val = 0
    for i in range(count):
        sum_val += data
        data = data * 10 + num


class String:
    def string_comb(self, s):
        question = '''一个字符串s，返回一个由s的前2个字符和后2个字符组成的新字符串。如果s的长度小于2，则返回空字符串。'''
        if len(s) < 2:
            return ''
        return '{0}{1}'.format(s[:2], s[-2:])

    def string_del(self, s, n):
        question = '''处理用户输入的字符串，按用户要求删除其中第n个字符，返回删除字符后的字符串'''
        return s[:n - 1] + s[n:]

    def string_conver(self, s):
        question = '''给定字符串，将其中的单词倒序输出'''
        list1 = s.split()[::-1]
        for i in list1:
            print(i, end='')
        string = 'What a wonderful day!'
        s = ' '.join(string.split()[::-1])
        print(s)

    ################################
    def string_count(self, s):
        question = '''统计每个字符出现的次数'''
        for i in range(len(s)):
            if i < s.rfind(s[i]):
                continue
            else:
                print('{0}:{1}'.format(s[i], s.count(s[i])))

    def english(self, word):
        question = '''
        英语语法中，动词的第三人称单数形式规则简要概括（不完全）如下：
        a)	如果动词以y结尾，则去掉y并加上ies。
        b)	如果动词以o， ch，s， sh， x， z结尾，则加上es。
        c)	默认直接在动词后加上s。
        现在请你写一个程序，对于任意给定的一个动词，返回其第三人称单数形式
        '''
        l = ['o', 'ch', 's', 'sh', 'x', 'z']
        if word[len(word) - 1] == 'y':
            return '{}的第三人称单数:{}ies'.format(word, word[:len(word) - 1])
        elif word[len(word) - 1] or word[len(word) - 1: len(word) - 2] in l:
            return '{}的第三人称单数:{}es'.format(word, word)
        else:
            return '{}的第三人称单数:{}s'.format(word, word)

    def string_check(self, string):
        question = '''
写一个简单的拼写检查程序。实现以下功能：
a)	两个或两个以上的空格出现时将其压缩为一个。
b)	在标点符号后加上一个空格，如果这个标点符合之后还有字母。
例：给定字符串："Thisisveryfunnyandcool.Indeed!"
输出："Thisisveryfunnyandcool.Indeed!"
其中“”代表一个空格。
        '''
        punctuation = [',', '，', '.', '/', '?', ';', ':', '', '!', chr(34)]
        for i in range(len(string) - 1):
            if string[i] in punctuation and string[i + 1] != ' ':
                # 标点后+ 空格 + 后面字符串
                string = string[:i + 1] + ' ' + string[i + 1:]
            else:
                continue

        list1 = string.split()[::]
        for i in list1:
            print(i, end=' ')

    ################################
    def analysis(self, string):
        question = '''
请写一个Python程序以尝试解析XML/HTML标签。现有如下一段内容：
<composer>Wolfgang Amadeus Mozart</composer>
<author>Samuel Beckett</author>
<city>London</city>
希望自动格式化重写为：
composer: Wolfgang Amadeus Mozart
author: Samuel Beckett
city: London
        '''
        import re
        stopword = ''
        s1 = string + '\n'
        for line in iter(string, stopword):
            s1 += line + '\n'
        list1 = s1.splitlines()

        for i in list1:
            part1 = re.compile("</.+>")
            part2 = re.compile("<")
            part3 = re.compile(">")

            s2 = part3.sub(':', part2.sub('', part1.sub('', i)))

# TODO


class Screen_prime:
    def search_prime(self, start, end):
        # 求某一范围内所有质数
        #  两数互质  递归法求最大公约数，当最大公约数是1的时候，两个数互质
        list1 = list(range(start, end))
        i = 0
        while i < len(list1) - 1:
            j = i + 1
            while j < len(list1) - 1:
                if list1[j] % list1[i] == 0:
                    del list1[j]
                else:
                    j += 1
            i += 1
        return list1

    def print_list(self, list1, row_number):
        # 控制输出格式
        count = 0
        for data in list1:
            print('{:<5d}'.format(data), end='')
            count += 1
            if count % row_number == 0:
                print()
        print()

    def main(self):
        list1 = self.search_prime(2, 500)
        self.print_list(list1, 5)


def weight():
    list1 = [65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8]
    #  计算体重方差
    average = sum(list1) / len(list1)
    n = 0
    for data in list1:
        n += (data - average) ** 2
    result = n / len(list1)
    return result


def restructure(s1, s2):
    question = '''编写程序让用户输入两个字符串（一定是小写字母组成），判断两个字符串是否同构。\
    如果有两个字符串，其中一个字符串的字符重新排列后，能变成另一个字符串，那么称为同构'''
    return list(s1).sort() == list(s2).sort()


def random_matrix():
    question = '''编写程序对一个4*4的矩阵进行随机赋值，然后对该矩阵进行转置，并输出转置后的结果'''
    import random
    x1 = x2 = [[0] * 4 for i in range(4)]
    for row in range(4):
        for col in range(4):
            x1[row][col] = random.randint(100, 999)
    # 对局矩阵进行转置

    for row in range(4):
        for col in range(4):
            x2[col][row] = x1[row][col]
    return x1, x2


def achievement(name, mark1, mark2):
    total_mark = []
    for i in range(5):
        total_mark.append(mark1[i] + mark2[i])
    res = list(zip(total_mark, name))
    res.sort(reverse=True)  # 根据第一个元素判断大小
    for i in range(len(res)):
        prime('{}的成绩是{}'.format(res[i][1], res[i][0]))


def magic_square(n):
    solution = '''
*第一个元素放在第一行中间一列 
*下一个元素存放在当前元素的上一行、下一列
 *如上一行、下一列已经有内容，则下一个元素存放在当前列的下一行。 
    '''
    row, col = 0, n // 2
    magic = [[0 for i in range(n)] for j in range(n)]
    magic[row][col] = 1
    for i in range(2, n * n + 1):
        r, l = (row - 1 + n) % n, (col + 1) % n  # 下一步将要到达的横纵坐标
        if magic[r][l] == 0:  # 如果将要到达的位置没有赋值过->即合法,则跳转
            row, col = r, l
        else:
            row = (row + 1) % n
        magic[row][col] = i
    for row in range(n):
        for col in range(n):
            print('{: 3d}'.format(magic[row][col]), end='')
        print('\n')

# TODO
class Dictionary:
    def same_keys(self):
        question = '''在程序中创建两个字典，1.找出并显示两个字典中相同的键,2.按照value排序'''
        import random
        dict1 = {'a': 'A', 'b': 'B', 'c': 'C'}
        dict2 = {'1': 'A', 'b': 'B', '3': 'C'}

        key1 = set(list(dict1.keys()))
        key2 = set(list(dict2.keys()))
        same_key = key1 & key2
        print(dict1)
        print(dict2)
        prime(same_key)

        print()
        dict3 = {k: random.randint(10, 20) for k in range(1, 5)}
        print(dict(sorted(dict3.items(), key=lambda item: item[1])))

    def employee(self):
        question = '''
        创建一个有关雇员姓名和编号处理的程序。从键盘输入一组雇员姓名和编号。在此基础上实现：
        (1).按照雇员姓名的顺序输出数据，雇员姓名显示在前面，后面是对应的雇员编号。
        (2).按照雇员编号的顺序输出数据，雇员编号显示在前面，后面是对应的雇员姓名。
        '''

        def name_sort(dict1):
            list1 = list(dict1.items())
            list1.sort(key=lambda x: x[0])
            return list1

        def num_sort(dict1):
            list2 = list(dict1.items())
            list2.sort(key=lambda x: x[1])
            return list2

        def main():
            count = int(input('总共几组雇员-编号：'))
            dict1 = {}

            for i in range(count):
                name = input('雇员姓名：')
                num = input('雇员编号：')
                dict1[name] = num

            print('按照name排序：')
            list1 = name_sort(dict1)
            for i in list1:
                print('{}:{}'.format(i[0], i[1]))

            print('按照编号排序：')
            list2 = num_sort(dict1)
            for j in list2:
                print('{}:{}'.format(j[0], j[1]))


class Same_or_not:
    question = '''
            通过[0,500]范围内随机数发生的方法分别创建两个整数数据的集合，要求每个集合中数据的个数分别要超过200个。在此基础上实现：
            (1).求出两个集合中不相同的数据，并进行显示。要求每行显示10条，每个数占5列，右对齐；
            (2).求出两个集合中相同的数据，并进行显示。要求每行显示10条，每个数占5列，右对齐；
            '''

    def sets(self, s1, s2):
        list1, list2 = [], []
        for x in s1:
            if x not in s2:
                list1.append(x)  # 不同
            else:
                list2.append(x)  # 相同
        return list1, list2

    def random_dict(self):
        import random
        s1, s2 = set(), set()
        while len(s1) <= 201:
            n1, n2 = random.randint(500), random.randint(500)
            s1.add(n1)
            s2.add(n2)
        list1, list2 = self.sets(s1, s2)
        count = 0
        print('不同的数据：')
        for i in list1:
            print('{:>5}'.format(i), end='')
            count += 1
            if count % 10 == 0:
                print()
        print()

        count = 0
        print('相同的数据：')
        for i in list2:
            print('{:>5}'.format(i), end='')
            count += 1
            if count % 10 == 0:
                print()
        print()


def circile_out(step, number):
    question = '''从文件中读取数，构成列表
    循环出圈（4），求第20个出来的数字
    '''
    #############################
    import random
    list1 = [random.randint(1, 999) for i in range(100)]

    def create_file(list1):
        try:
            with open(r'D:\python\list.txt', 'w') as file:
                for data in list1:
                    file.write(str(data) + ',')
        except IOError:
            print('ERROR')

    def read_file():
        with open(r'D:\python\list.txt', 'r') as file:
            list2 = file.read().strip('\n').split(',')
            if '' in list2:
                list2.remove('')
            if ' ' in list1:
                list2.remove(' ')
        return list2

    def out_num(list2, step, number): # number:第几个出圈的数；step: 步幅
        last = 0
        count = 1
        remain_list = list2.copy()
        while len(remain_list):
            index = (last + step - 1) % len(remain_list)
            count += 1
            if count == number:
                return remain_list[index]
            remain_list.pop(index)
            last = index

    create_file(list1)
    list2 = read_file()
    num = out_num(list2, 4, 20)
    print(num)


def random_set():
    question = '''
    使用random模块生成一个整数类型的随机数集合：从0到9(包括9)中随机选择，生成1到10个[0,1000]范围内的随机数。这些数字组成集合A。\
    同理，按此方法生成集合B。在此基础上实现以下功能：
(1).显示A和B的结果。要求每行最多显示10个数，每个数占5列，右对齐；
(2).要求用户输入 A | B 和 A & B 的结果，并告诉用户他(或她)的答案是否正确。\
如果用户回答错误，允许他(或她)修改解决方案，然后重新验证用户输入的答案。如果用户三次提交的答案均不正确，程序将显示正确结果。
'''
    import re
    import random
    n1, n2 = random.randint(0, 9), random.randint(0, 9)
    s1, s2 = set(), set()

    for i in range(n1 + 1):
        s1.add(random.randint(0, 1000))
    for i in range(n2 + 1):
        s2.add(random.randint(0, 1000))

    print('集合A：')
    count = 0
    for i in s1:
        print('{:>5}'.format(i), end='')
        count += 1
        if count % 10 == 0:
            print()
    print()

    print('集合B：')
    count = 0
    for i in s2:
        print('{:>5}'.format(i), end='')
        count += 1
        if count % 5 == 0:
            print()
    print()

    flag = False
    count = 0
    while (not flag) and count < 3:
        answer = input('输入A|B的结果：')
        list1 = re.findall(r'\d+', answer)  # 将输入数据变为列表
        list1 = [int(x) for x in list1]  # 将str -> int
        if set(list1) == s1.union(s2):
            print('Right')
            flag = True
        else:  
            count += 1
    if not flag:
        print('A|B:', s1.union(s2))

    flag = False
    count = 0
    while (not flag) and count < 3:
        answer = input('输入A&B的结果：')
        list1 = re.findall('\d+', answer)  # 将输入数据变为列表
        list1 = [int(x) for x in list1]  # 将str -> int
        if set(list1) == s1.intersection(s2):
            print('Right')
            flag = True
        else:
            count += 1
    if not flag:
        print('A&B:', s1.intersection(s2))


def factor(num):
    question = '''
    1.	编写一个函数，计算一个整数的所有因子之和，其中因子不包括整数本身，\
    并编写测试程序，在测试程序中输入整数和输出整数的所有因子之和。例如：输入8，调用该函数之后，得到结果为7。
    '''
    sum_value = 0
    for i in range(num):
        if num % i != 0:
            continue
        sum_value += i
    return sum_value


class Reverse_prime:
    question = '''
    反素数指一个素数将其逆向拼写后也是一个素数的非回文数。\
    例如：17和71都是素数且都不是回文数，所以17和71都是反素数。\
    请编写一个函数判断一个数是否是反素数？并编写测试程序找出前30个反素数输出到屏幕上，\
    要求每行输出8个数，每个数占5列，右对齐。
    '''

    def is_prime(self, num):
        import math
        flag = True
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):  # 注意范围 及 +1
            if num % i == 0:
                flag = False
                break
        return flag

    def deal(self):
        count, num, each_line = 30, 10, 0
        while count > 0:
            reverse_num = int(str(num)[::-1].lstrip('0'))
            if self.is_prime(num) and self.is_prime(reverse_num) and num != reverse_num:
                print('{:<5d}'.format(num), end='')
                count -= 1
                each_line += 1
                if each_line % 8 == 0:
                    print()
            num += 1


class Mersenne_prime:
    question = '''
    如果一个 素数 可以写成2^p-1形式，其中p是一个正整数，那么该数就称作梅森素数。\
    请编写一个函数判断一个素数是否是梅森素数，如果是，则返回p的值，否则返回-1。\
    并编写测试程序找出1000以内的所有梅森素数输出到屏幕上，要求输出格式如下：
    P(占3列右对齐)   2^p-1 (占4列右对齐)     # 此行不需要输出
    '''

    def is_mersenne_prime(self, num):
        flag, p = False, 0
        import math
        p = math.log2(num + 1)
        if p % 1 == 0.0:  # 判断是否为整数
            flag = True
            for i in range(2, int(math.sqrt(num) + 1)):
                if num % i == 0:
                    flag = False
                    break
            p = int(p) if (flag and num > 1) else -1
        else:
            p = -1
        return p

    def output_mersenne_prime(self):
        print('{:3}'.format('P'), end='')
        print('{:>4}'.format('2^p-1'), end='')
        print()
        for i in range(1, 1000):
            p = self.is_mersenne_prime(i)
            if p != -1:
                print('{:<3}  '.format(p), end='')
                print('{:<4}'.format(pow(2, p) - 1))
                print()


class Password:
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    question = '''
    5.	编写一个加密函数，实现对一个给定字符串中的字母转变为其后n个字符，\
    如果遇到超过字母边界，则从最小字母继续计数，(连续的数字) 字符作为一个整数扩大n倍之后替换到对应位置，其中n默认为5。\
    再编写一个解密函数实现对上述加密字符串进行解密。\
    例如：字符串str1:  avbV125av1,  n默认为5
    则新的字符串str2: fagA625fa5 '''

    def main(self):
        judge = input('加密输入1， 解密输入2：')
        if judge == '1':
            string = input('输入需要加密的字符串：')
            encryption_string = self.encryption(string)
            print(encryption_string)
        else:
            string = input('输入需要解密的字符串：')
            decryption_string = self.decryption(string)
            print(decryption_string)

    def encryption(self, string):
        import re
        list1 = re.findall('\d+|[A-Za-z]+|\W+', string)
        str1 = ''

        for char in list1:
            if char.isalpha():  # 是字母
                for each_char in char:  # 对单个字母进行遍历
                    i = ord(each_char)
                    j = i + 5
                    if ord('Z') < j <= (ord('Z') + 5) or j > ord('z'):
                        j -= 26
                    each_char_2 = chr(j)
                    str1 += each_char_2
            elif char.isalnum():
                num = int(char) * 5
                str1 += str(num)
            else:
                str1 += char
        return str1

    def decryption(self, string):
        import re
        list1 = re.findall(r'\d+|[A-Za-z]+|\W+', string)
        str2 = ''
        for char in list1:
            if char.isalpha():
                for each_char in char:  # 对单个字母进行遍历
                    i = ord(each_char)
                    j = i - 5
                    if ord('a') - 5 <= j < ord('a') and j < ord('A'):
                        j += 26
                    each_char_2 = chr(j)
                    str2 += each_char
            elif char.isalnum():
                num = int(char) // 5
                str2 += str(num)
            else:
                str2 += char
        return str2

# TODO
class Count:
    question = '''
    统计一个给定的英文语句中，某个指定位置的字符在字符串中出现的次数，\
    统计时不区分字母的大小写，默认字符位置为0。\
    编写测试程序，在测试程序中输入英文语句，指定要查找的字符位置，并输出该字符在语句中出现的次数。\
    例如：英文语句：This is a test example.\
    统计位置0的字符是t，则在语句中出现的次数为：3。(3次包括大写和小写的t)
    '''

    def count_Alpha(self, string, num):
        s = string.lower()
        count = 0
        for i in range(len(s)):
            if s[i] == s[num]:
                count += 1
        return count

    def main(self):
        string = input('输入英文字符串：')
        num = int(input('输入查找字母位置：'))
        number = self.count_Alpha(string, num)
        print('次数为：', number)


class Fibonacci:
    question = '''
    求解Fibonacci数列（兔子繁殖）问题的某项的值。\
    编写测试程序，从键盘输入指定项，并输出Fibonacci数列指定项的值
    '''

    def fib(self, num):
        if num == 1 or num == 2:
            return 1
        else:
            return self.fib(num - 1) + self.fib(num - 2)

    def main(self):
        n = int(input('Fib第几项：'))
        number = self.fib(n)
        print(number)


class Calculation:
    question = '''
    当前路径下有文本文件Numbers.txt，文件中的 每一行 都是 一个 浮点数，编写程序读取出所有的浮点数。要求：
  （1）从小到大排序，将排序后的结果写到当前路径下新生成的一个文本文件Sort.txt中，每个数占一行。
  （2）求出这些数字的均值、方差，将结果写到当前路径下新生成的一个文本文件Sort.txt中每个数占一行。
  （要求生成的文本文件Sort.txt中包含排序和均值、方差的结果。）
    '''

    def create_file(self):
        try:
            import random
            with open(r'D:\python\Numbers.txt', 'w') as file:
                data = random.uniform(0, 100)
                count = 0
                while count < 100:
                    file.write(str(data) + '\n')
                    data = random.uniform(0, 100)
                    count += 1
        except IOError:
            print('create_file:Error')

    def read_file(self):
        try:
            with open(r'D:\python\Numbers.txt', 'r') as file:
                list1 = []
                data = file.readline()
                while data != '':
                    list1.append(eval(data.rstrip('\n')))
                    data = file.readline()
        except IOError:
            print('read_file:ERROR')
        else:
            return list1

    def deal(self):
        list1 = self.read_file()
        list1.sort()
        try:
            with open(r'D:\python\Sort.txt', 'a+') as file:
                for data in list1:
                    file.write(str(data) + '\n')
                average = sum(list1) / len(list1)
                file.write('均值：' + str(average) + '\n')
                num = 0
                for data in list1:
                    num += pow((data - average), 2)
                variance = num / len(list1)
                file.write('方差：' + str(variance) + '\n')

        except IOError:
            print('deal:Error')


class Folder:
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    question = '''
    当前路径下有一个文件夹Folder，文件夹下有多个文本文件file1~file4（文件名称和文件内容都是英文的），\
    将这些文本文件内容合并生成一个新的 文本文件merge.txt 存放在 Folder文件夹 中，不破坏原始文件。
    '''

    def create_file(self):
        try:
            import os
            os.chdir(r'D:\oython')
            dir_name = os.path.join(os.getcwd(), 'floder')  # 路径=当前目录名 + floder文件夹
            out_file = open(os.path.join(dir_name, 'merge.txt'), 'w')  # 创建新文件
            list1 = []
            for file_name in os.listdir(dir_name):  # 遍历文件夹里的文件
                in_file = open(os.path.join(dir_name, file_name), 'r')  # 打开每一个文件，进行操作
                string = in_file.readline()
                while string != '':
                    out_file.writelines(string.rstrip('\n') + '\n')
                    string = in_file.readline()
                in_file.close()
        except IOError:
            print('create_file:Error')
        else:
            out_file.close()


class Vowel:
    question = '''
    当前路径下有文本文件word.txt中包含了20个英文单词，编写一个程序，删除文件中所有不以元音开头的单词。结果保存在当前路径下新生成的new_word.txt中。
    '''

    def deal(self):
        try:
            with open(r'D:\python\word.txt', 'r') as in_file:
                word_list = []
                word = in_file.readline()
                while word != '':
                    word_list.append(word.strip().rstrip('\n'))
                    word = in_file.readline()
            with open(r'D:\python\new_word.txt', 'w') as out_file:
                for word in word_list:
                    if word[0] not in ['a', 'e', 'i', 'o', 'u']:
                        out_file.write(word + ' ')
        except IOError:
            print('ERROR')
        else:
            in_file.close()
            out_file.close()


class Dir_file:
    question = '''
    当前路径下有一个文本文件Names.txt，包含了按照字典序排序的名字。\
    编写一个程序，当用户自己给定一个名字，按照字典序将其插入到正确的位置。如果这个名字已经存在于文件中，则不要插入。
    例如：
     
    Names.txt文件中有如下文本（每个名字占一行）
    Aaron
    Cornell
    用户输入的待插入文本是：Abbott
    则生成的新文件夹new_word.txt的内容是：
    Aaron
    Abbott
    Cornell
    '''

    def deal(self):
        try:
            with open(r'D:\python\Name.txt', 'r') as in_file:
                name_list = []
                name = in_file.readline()
                while name != '':
                    name_list.append(name.strip().rstrip('\n'))
                    name = in_file.readline()

            with open(r'D:\python\new_Name.txt', 'w') as out_file:
                name = input('输入名字：')
                name_list.append(name)
                name_list.sort()
                out_file.writelines(name_list)
        except IOError:
            print('Error')
