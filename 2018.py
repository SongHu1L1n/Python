question = '''
二进制文件有2W个数 求最大子集写入另一个文件中
(1) 最大子集任意两个数不成倍数， 最大公约数为1
(2) 按格式写入文件中：
    12(个数)
    2   3   5   7   13
    17  23  29  31  37
    41  43
'''


class Solution:
    array = []
    prime = []
    already = []

    def create_file(self):
        import struct
        with open(r'D:\python\2018.bin', 'wb') as file:
            for i in range(50):
                if i == 3 or i == 5:
                    continue
                else:
                    file.write(struct.pack('i', i))
        file.close()

    def read_file(self):
        import struct
        file = open(r'D:\python\2018.bin', 'rb')
        size = struct.calcsize('i')
        data = file.read(size)
        while data:
            value, = struct.unpack('i', data)
            self.array.append(int(value))
            data = file.read(size)
        file.close()

    def is_prime(self, data):
        import math
        if data < 2:
            return False
        i = 2
        while i <= math.sqrt(data):
            if data % i == 0:
                return False
        return True

    def sort_array(self, arr):
        if len(arr) <= 1:
            return arr
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                j = i - 1
                data = arr[i]
                while arr[j] > data and j >= 0:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = data

    def unique(self, arr):
        count = 0
        for i in range(1, len(arr)):
            if arr[count] != arr[i]:
                count += 1
                arr[count] = arr[i]
        self.already = arr[:count]

    def right_num(self):
        for i in range(len(self.already)):
            if self.is_prime(self.already[i]):
                self.prime.append(self.already[i])

        for i in range(len(self.already)):
            flag = True
            for j in range(len(self.prime)):
                if self.already[i] % self.prime[j] == 0:
                    flag = False
                    break

                if flag:
                     self.prime.append(self.already[i])

    def display(self):
        num = len(self.prime)
        file = open(r'D:\python\2018_display.txt', 'w')
        file.write(str(num) + '\n')
        count = 0
        for i in range(len(self.prime)):
            file.write(str(self.prime[i] + '' * (5 - len(self.prime[i]))))
            count += 1
            if count == 5:
                file.write('\n')
        file.close()


def main():
    s = Solution()
    s.create_file()
    s.read_file()
    s.sort_array(s.array)
    s.unique(s.array)
    s.right_num()
    s.sort_array(s.prime)
    s.display()
