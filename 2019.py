class Solution2019:
    arr = []
    res = [0 for i in range(10)]
    test = [i for i in range(10)]  # 结果测试
    effective_length = 0
    string = ''

    def create_file(self):
        import random
        with open(r'D:\python\2019data.txt', 'w') as file:
            for i in range(100):
                data = random.randint(0, 20)
                file.write(str(data) + '\n')

    def read_file(self):
        with open(r'D:\python\2019data.txt', 'r') as file:
           num = file.readline().strip('\n')
           while num:
               self.arr.append(int(num))
               num = file.readline().strip('\n')

    def display(self):
        count = 0
        for i in range(len(self.arr)):
            count += 1
            print('{:6d}'.format(self.arr[i]), end='')
            if count % 10 == 0:
                print('\n')

    def count(self):
        for i in range(len(self.res)):
            self.res[i] = self.arr.count(i)

    def print_res(self):
        count = 0
        for i in range(len(self.res)):
            count += 1
            print('{:6d}'.format(self.res[i]), end='')
            if count % 5 == 0:
                print('\n')

    def sum_factor(self, data):  # 因子和 函数
        if data == 0:
            return 0
        elif data == 1:
            return 1
        else:
            sum_val = 0
            for i in range(2, data + 1):
                if data % i == 0:
                    sum_val += i
            return sum_val + 1

    def sort_array(self):  # 直插排序思想
        for index in range(2, len(self.arr)):
            if self.sum_factor(self.arr[index]) < self.sum_factor(self.arr[index - 1]):
                data = self.arr[index]
                factor = self.sum_factor(data)
                j = index - 1
                while j >= 0 and self.sum_factor(self.arr[j]) >= factor:
                    if self.sum_factor(self.arr[j]) == factor:   # 两数因子和相等
                        if self.arr[j] < data:
                            break
                    self.arr[j + 1] = self.arr[j]
                    j -= 1
                self.arr[j + 1] = data

    def filter_array(self):
        # 快排思想，交换前后奇偶数，再对偶数进行直接插入排序
        low, high = 0, len(self.arr) - 1
        while low < high:
            while high > low and self.arr[high] % 2 == 1:
                high -= 1
            while low < high and self.arr[low] % 2 == 0:
                low += 1
            if low != high:
                self.arr[low], self.arr[high] = self.arr[high], self.arr[low]
        self.effective_length = low + 1

        # 对偶数进行直插排序
        if low >= 1:
            for i in range(2, self.effective_length):
                if self.arr[i] < self.arr[i - 1]:
                    temp = self.arr[i]
                    last = i - 1
                    while last >= 0 and self.arr[last] > temp:
                        self.arr[last + 1] = self.arr[last]
                        last -= 1
                    self.arr[last + 1] = temp

    def prime_factor(self, data):
        self.string = ''
        num = data
        if data >= 2:
            j = 2
            self.string += str(num) + ' = '
            while True:
                if data % j == 0:
                    data /= j
                    self.string += str(j) + ' * '
                    if data == 1:
                        break
                else:
                    j += 1

    def final_output(self):
        with open(r'D:\python\2019outdata.txt', 'w') as file:
            for i in range(self.effective_length):
                self.prime_factor(self.arr[i])
                file.write(self.string.rstrip(' * ') + '\n')


def main():
    s = Solution2019()
    s.create_file()
    s.read_file()
    s.display()
    s.count()
    s.print_res()
    s.sort_array()
    s.filter_array()



main()
