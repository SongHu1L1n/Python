Q = '''
二进制文件包含整形，每个点与其后面一个点构成坐标，
(1) 处于第一象限为有效点，数据中总共含有点的个数？有效点个数？
(2) 每个有效点与坐标原点构成矩形，所有矩形最小公共面积？
(3) 寻找符合以下条件的点：以该坐标点为原点，其余坐标点在这种情况下 仍然是有效点
(4) 对坐标点进行分组，每个点只属于一个组，符合以下规则：对组内所有点的x坐标排序，[x1, y1] 在[x2, y2]前面，则 x1 < x2;y1 < y2
'''


class Solution(object):
    def creat_file(self):
        import struct
        import random
        try:
            file = open(r'D:\python\org.dat', 'wb')
            for i in range(100):
                file.write(struct.pack('i', random.randint(-20, 100)))
            file.close()
        except IOError:
            print('文件创建失败!')

    def read_file(self):
        num = []
        import struct
        file = open(r'D:\python\org.dat', 'rb')
        size = struct.calcsize('i')
        data = file.read(size)
        while data:
            value, = struct.unpack('i', data)
            num.append(value)
            data = file.read(size)
        file.close()
        return num

    def effective_point(self, num):
        point_list = []
        point = []
        for i in range(1, len(num)):
            point_list.append([num[i - 1], num[i]])

        for i in range(len(point_list)):
            if point_list[i][0] > 0 and point_list[i][1] > 0:
                point.append(point_list[i])

        return len(point_list), point

    def minimum_com_area(self, point):
        #  minimum纵坐标, minimun横坐标
        minimum_height = 1000
        minimum_width = 1000
        for i in range(len(point)):
            if point[i][0] < minimum_width:
                minimum_width = point[i][0]
            if point[i][1] < minimum_height:
                minimum_height = point[i][1]
        print('最小宽度：', minimum_width)
        print('最小高度：', minimum_height)
        area = minimum_height * minimum_width
        return area

    def origin(self, point):
        for i in range(len(point)):
            flag = 0
            for j in range(len(point)):
                if j == i:
                    continue
                if point[i][0] <= point[j][0] and point[i][1] <= point[j][1]:
                    flag = 1
                    origin_point = point[i]
                    break
            if flag:
                print('符合条件的点为：(%d, %d)' % (point[i][0], point[i][1]))
                return
        print('没有符合条件的点')

    def point_sort(self, point):
        for i in range(len(point)):
            for j in range(i):
                if point[j][0] > point[i][0]:
                    temp = point[i]
                    point[i] = point[j]
                    point[j] = temp
                elif point[j][0] == point[i][0]:
                    if point[j][1] > point[i][1]:
                        temp = point[j][1]
                        point[j][1] = point[i][1]
                        point[i][1] = temp
        return point

    def group(self, point):
        group_num = [0] * len(point)  # 判断是否已经被分组，未分组为0，以分组为组号
        group_count = 0
        for i in range(len(point)):
            if group_num[i] == 0:  # 组号
                group_count += 1   # 目前组个数
                group_num[i] += group_count
            point_x = point[i][0]
            point_y = point[i][1]

            for j in range(i + 1, len(point)):
                if group_num[j] == 0 and point[j][0] > point_x and point[j][1] > point_y:
                    group_num[j] = group_count

        for i in range(1, group_count + 1):
            group_list = []
            for j in range(len(point)):
                if group_num[j] == i:
                    group_list.append(point[j])
            print('第%d组：' % i, end='')
            print(group_list)


s = Solution()
s.creat_file()
num = s.read_file()

all_point_num, point = s.effective_point(num)
k = effective_point_num = len(point)
print('所有点的个数为：%d' % all_point_num)
print('有效点个数为： %d' % k)

minimun_common_area = s.minimum_com_area(point)
print('最小公共面积为：%d' % minimun_common_area)

s.origin(point)
'排序'

s.point_sort(point)
print(point)

s.group(point)