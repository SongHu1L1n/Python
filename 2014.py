question = '''
二进制文件input.dat, 存有Int型数字，每次读取两个，构成一个坐标
(1) 有效点个数：第一象限
(2) 键盘输入坐标(x, y) 和 k ，输出k个离该点距离最近的坐标和每个坐标到该点的距离
'''


class Solution:
    points = []
    effective = []  # 第一象限
    point = (x, y) = tuple(input())
    k = map(int, input('k'))
    dis = []

    def create_file(self):
        import struct
        import random

        with open(r'D:\python\2014.dat', 'wb') as file:
            for i in range(100):
                file.write(struct.pack('i', random.randint(-100, 100)))

    def read_file(self):
        import struct
        size = struct.calcsize('i')
        with open(r'D:\python\2014.dat', 'rb') as file:
            num1, num2 = file.read(size), file.read(size)
            while num1 and num2:
                val1, = struct.unpack('i', num1)
                val2, = struct.unpack('i', num2)
                self.points.append((val1, val2))
                num1, num2 = file.read(size), file.read(size)

    def first_position(self):
        for i in range(len(self.points)):
            if self.points[i][0] > 0 and self.points[i][1] > 0:
                self.effective.append(self.points[i])

    def distance(self, x, y):
        return pow((pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2)), 0.5)

    def deal(self):  # 计算距离
        for i in range(len(self.effective)):
            self.dis.append(self.distance(self.point, self.effective[i]))

    def display(self):
        with open(r'D:\python\2014_out.txt', 'w') as file:
            while self.k:
                length = max(self.dis)  # 当前最大距离
                idx = self.dis.index(length)  # 最大距离点坐标
                point = self.effective[idx]  # 取该点
                file.write(str(point) + '-' + str(length) + '\n')
                self.dis[idx] = -1
                self.k -= 1


def main():
    s = Solution()
    s.create_file()
    s.read_file()
    print(s.points)
    s.first_position()
    print(s.effective)

main()