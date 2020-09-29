Q = '''
文件中存放一段句子，单词之间使用空格 隔开，无其它符号
顺序读取文章的单词(大小写敏感)， 同时在读取的过程中排除所有的 以THE为变形的单词
将所有符合要求的读取的单词 首字母大写，存入new.txt中，每个单词一行
'''


class Solution(object):
    def create_file(self):
        try:
            string = 'The constructor is used to initialize the objext\
The destructor is used to delete the Object\
the calling sequence of constructor is oppose to calling the sequence of destructor'
            with open(r'D:\python\org.dat', 'w') as file:
                file.write(string)
            file.close()
        except IOError:
            print('Error')

    def read_file(self):
        file = open(r'D:\python\org.dat', 'r')
        string = file.read()
        file.close()
        return string

    def deal(self, string):
        all_the = ['The', 'THe', 'ThE', 'THE']
        str_list = string.title().split(' ')
        list = []
        if ' ' in str_list:
            str_list.remove(' ')
        for i in str_list:
            if i != ' ' and i not in all_the:
                list.append(i + '\n')
        file = open(r'D:\python\new.txt', 'w')
        file.writelines(list)
        file.close()


s = Solution()
s.creat_file()
string = s.read_file()
s.deal(string)