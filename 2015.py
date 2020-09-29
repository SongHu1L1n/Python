question = '''
二进制文件input.dat，存放一堆intx型整数，每个数占四个字节，每次读取两个，构成一个坐标。
（1） 规定处于第一象限的数是有效点，（x > 0 and y > 0）， 问：有效点有多少个？
（2）键盘输入K 和 N , 从第一问的有效点中找出符合距离小于N的点的个数大于K 的点，将他们以文本格式输出到output.txt文件中
'''


class Solution:
    points = []  # 读取文件构成的点
    count = 0  # 第一象限点的数量
    k, n = eval(input('k, n:'))
    useful = []  # 第一象限的点
    output_list = []  # 用于最后输出

    def create_file(self):
        import struct
        import random

        file = open('../python/2015.bin', 'wb')
        for i in range(50):
            num = random.randint(-50, 50)
            file.write(struct.pack('i', num))
        file.close()

    def read_file(self):
        a = []
        import struct
        size = struct.calcsize('i')
        file = open('../python/2015.bin', 'rb')
        data = file.read(size)
        while data:
            val, = struct.unpack('i', data)
            a.append(val)
            data = file.read(size)
        for i in range(1, len(a)):
            self.points.append((a[i - 1], a[i]))
        file.close()

    def first_position_point(self):
        for i in range(len(self.points)):
            if self.points[i][0] > 0 and self.points[i][1]:
                self.useful.append(self.points[i])
                self.count += 1

    def distance(self, x, y):
        return pow((pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2)), 0.5)

    def qualified(self):
        for i in range(len(self.useful)):
            count = 0
            for j in range(len(self.useful)):
                if i == j:
                    continue
                if self.distance(self.useful[i], self.useful[j]) < self.n:
                    count += 1
            if count > self.k:
                self.output_list.append(self.useful[i])

    def deal(self):
        file = open('../python/2015_out.txt', 'w')
        for i in range(len(self.output_list)):
            file.write(str(self.output_list[i]) + '\n')
        file.close()


def main():
    s = Solution()
    s.create_file()
    s.read_file()
    s.first_position_point()
    s.qualified()
    s.deal()
