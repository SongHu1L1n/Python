Q = '''
二进制文件data.bin 
(1) 读取文件中所有数据
(2) 每相邻两个整数构成一个坐标：12， 13， 14， 15 -> (12, 13), (13, 14), (14, 15)
(3) 一每个坐标为圆心 计算半径。当计算到最后一个点时，与第一个点计算半径
(4) 计算所有园的点密度值， 输出：
    (x, y) | 包含点数(占5列， 右对齐) | 点密度(占7列， 右对齐，保留2位小数)
'''


class Solution:
    arr = []  # read
    points = []  # 坐标点
    dis = []  # 存储相邻两点间的距离
    count = []  # 符合条件点数目
    des = []

    def create_file(self):
        import random
        import struct
        file = open(r'D:\python\2017.bin', 'wb')
        for i in range(50):
            data = random.randint(-50, 50)
            file.write(struct.pack('i', data))
        file.close()

    def read_file(self):
        import struct
        file = open(r'D:\python\2017.bin', 'rb')
        size = struct.calcsize('i')
        data = file.read(size)
        while data:
            val,  = struct.unpack('i', data)
            self.arr.append(val)
            data = file.read(size)
        file.close()

    def create_point(self):
        for i in range(1, len(self.arr), 2):
            point = (self.arr[i - 1], self.arr[i])
            self.points.append(point)

    def distance(self, A: tuple, B: tuple):
        return pow((pow(A[0] - B[0], 2) + pow(A[1] - B[1], 2)), 0.5)

    def cal_dis(self):
        for i in range(len(self.points)):
            if i != len(self.points) - 1:
                self.dis.append(self.distance(self.points[i], self.points[i + 1]))
            else:
                self.dis.append(self.distance(self.points[0], self.points[i]))

    def density(self):
        import math
        self.count = [1 for _ in range(len(self.points))]  # 初始化
        for i in range(len(self.points)):
            for j in range(len(self.points)):
                if i == i:
                    continue
                if self.distance(self.points[i], self.points[j]) <= self.dis[i]:
                    self.count[i] += 1
            self.dis.append(self.count[i] / math.pi * pow(self.dis[i], 2))

    def display(self):
        i = 0
        with open(r'D:\python\2017dataout.txt', 'w') as file:
            while i < 5:
                index = self.des.index(max(self.des))
                print(self.points[index], '{:>5d}'.format(self.count[index]), '{:>7.7f}'.format(self.des[index]), sep='|')
                self.des[index] = -1
                i += 1