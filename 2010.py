class Solution(object):
    def creat_file(self):
        try:
            import os
            import struct
            import random
            os.chdir(r'D:\python')

            with open('data.txt', 'ab') as file:
                rand_num = random.randint(20, 100)

                for i in range(rand_num):
                    file.write(struct.pack('i', random.randint(1, 2048)))

                for i in range((2048 - rand_num)):
                    file.write(struct.pack('i', 0))
            file.close()
        except IOError:
            print('Error')

    def read_file(self):
        list = []
        import struct
        import os

        os.chdir(r'D:\python')
        count = 0
        with open('data.txt', 'rb') as file:
            size = struct.calcsize('i')
            data = file.read(size)
            while data:
                value, = struct.unpack('i', data)
                if value == 0:
                    count += 1
                list.append(value)
                data = file.read(size)
        file.close()
        print(list)
        return list, count

    def is_prime(self, num):
        import math
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                return False
            else:
                continue
        return True

    def find_maximum_prime(self, list, count):
        max_num = 0
        for i in range(count):
            max_num = list[i] if self.is_prime(list[i]) and list[i] > max_num else max_num
        return max_num

    def deal(self, list, count):
        count_list = []
        for i in range(count):
            count_list.append(list[i])
        count_list.sort(reverse=True)
        if (count - 1) % 3 == 0:
            count_list.pop()

        elif (count - 2) % 3 == 0:
            count_list.pop()
            count_list.pop()

        fir_position = []
        sec_position = []
        the_position = []
        
        i = 0
        while i < len(count_list):
            if 0 <= i < len(count_list) / 3:
                fir_position.append(count_list[i])
            elif len(count_list) / 3 <= i < (len(count_list) / 3) * 2:
                sec_position.append(count_list[i])
            else:
                the_position.append(count_list[i])
            i += 1
        return max(sec_position), min(sec_position)


s = Solution()
s.creat_file()
list, count = s.read_file()
max_num, min_num = max(list), min(list)
max_prome = s.find_maximum_prime(list, count)