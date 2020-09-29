Q = '''
一段英文文档，加密 求密匙cip1, cip2 以及解密后的第一个句子:
    (1) cip1, cip2 都是八位无符号整数
    (2) 加密过程： 每次从文本中去除八位字符，然后将该字符和密钥交替 异或 ，便得到该位置的密文
'''


class Solution:
    def creat_file(self):
        try:
            file = open(r'D:\python\info.txt', 'w')

            string = 'Good morning dear professors.\nIt is my great honor to introduce the history of computer to you.\n'
            cip1 = 2
            cip2 = 56

            print('明文：', string)

            for i in range(len(string)):
                if string[i] != ' ':
                    if i % 2 == 0:
                        file.write(chr(ord(string[i]) ^ cip1))
                    else:
                        file.write(chr(ord(string[i]) ^ cip2))
                else:
                    file.write(string[i])

            file.close()
        except IOError:
            print('Error')

    def is_valid(self, data):
        if 'a' <= data <= 'z' or 'A' <= data <= 'Z' or '0' <= data <= '9' or data == '!' or data == '.' or data == '?' or data == ',' or data == '\"' or data == '\'' or data == '\n' or data == '':
            return True
        else:
            return False

    def find_keys(self, List):
        cip1 = cip2 = 0

        for cip1 in range(256):
            i = 0
            for i in range(len(List)):
                if i % 2 == 0:
                    if self.is_valid(chr(ord(List[i]) ^ cip1)):
                        continue
                    else:
                        break
            if i == len(List) - 1:
                break

        for cip2 in range(256):
            i = 0
            for i in range(len(List)):
                if i % 2 == 1:
                    if self.is_valid(chr(ord(List[i]) ^ cip2)):
                        continue
                    else:
                        break
                if i == len(List) - 1:
                    break
        return cip1, cip2

    def decode(self):
        try:
            List = []

            with open(r'D:\python\info.txt', 'r') as file:
                data = file.readline()
                for i in data:
                    List.append(i)
            file.close()

            cip1, cip2 = self.find_keys(List)
            char = ''
            for i in range(len(List)):
                cip = cip1 if i % 2 == 0 else cip2
                char += chr(ord(List[i]) ^ cip)
            return char
        except IOError:
            print('文件无法打开')


s = Solution()
s.creat_file()
s.decode()