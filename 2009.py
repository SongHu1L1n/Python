Q = '''
文件org.dat中存放长度小于15的文章，为十进制或八进制的数字，数字之间用','分割，数字内部存在且仅存在空格
八进制数以起始位'0' 作为与十进制的划分
  顺序读取这些数，转换为十进制，从大到小输出到文件new.txt中，每个数字一行
例：'23'
'''
' 235 ,34 2, 043 1,1 3'


class Solution(object):
    def create_file(self):
        with open(r'D:\python\org.dat', 'w') as file:
            string = ' 235 ,34 2, 043 1,1 3'
            file.write(string)
        file.close()

    def read_file(self):
        with open(r'D:\python\org.dat', 'r') as file:
            data = file.read()
            nums = data.rstrip('\n').split(',')
        file.close()
        print(nums)
        return nums

    def deal(self, nums):
        ten_num = []
        eig_num = []
        for i in range(len(nums)):
            data = nums[i].strip(' ')
            print(data, end=' ')
            num = ''
            for j in data:
                if j != ' ':
                    num += j
            print(num[0])
            if num[0] != '0':
                ten_num.append(int(num))
            else:
                eig_num.append(num)
        for data in eig_num:
            ten_num.append(int(data, 8))

        nums = sorted(ten_num, reverse=True)
        return nums

    def dispaly(self, nums):
        file = open(r'D:\python\new.txt', 'w')
        for i in nums:
            file.write(str(i) + '\n')
        file.close()


s = Solution()
s.creat_file()
nums = s.read_file()
nums = s.deal(nums)
s.dispaly(nums)