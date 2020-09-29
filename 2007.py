Q = '''
将10-1000之间满足以下要求的数，保存到result.txt 文件中
(1) 是素数
(2) 他的反数也是素数: 123->321
'''


class Solution(object):
    def is_prime(self, data):
        import math
        if data < 2:
            return False
        for i in range(2, int(math.sqrt(data))):
            if data % i == 0:
                return False
        return True

    def deal(self):
        out_data = []
        for data in range(10, 1001):
            reverse_data = int(str(data)[::-1])
            if self.is_prime(data) & self.is_prime(reverse_data):
                out_data.append(data)

        file = open(r'D:\python\result.txt', 'w')
        for i in range(len(out_data)):
            file.write(str(out_data[i]) + ',')
        file.close()


s = Solution()
s.deal()