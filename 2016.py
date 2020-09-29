question = '''
文本文件input.txt 中有若干英文单词 分隔符(空格 回车 换行) 统计不同单词出现次数。
将统计结果按出现频度从高到低排序， 并将频度大于5的单词及其频度输出到output.txt文件中
说明：
    (1) 多个连续的分隔符视为一个分隔符
    (2) 单词大小写敏感
    (3) 每个单词长度不超过20个字符
'''


class Solution:
    words = []  # 接受file中所有单词
    dict_count = {}  # 记录每个单词数量
    top_5 = []  # 输出

    def create_file(self):
        words = '''Thank you for comforting me when I\'m sad 
Loving me when mad 
Picking me up when down 
Thank you for being my friend and being around 
Teaching me the meaning of love 
Encouraging me when I need a shove  
But most of all thank you for 
Loving me for who I am '''
        file = open(r'D:\python\2016.txt', 'w')
        file.write(words)
        file.close()

    def read_file(self):
        file = open('../python/2016.txt', 'r')
        sentence = file.readline().strip('\n').strip()
        while sentence:
            self.words.extend(sentence.split())
            sentence = file.readline()
        file.close()

    def deal(self):
        import collections
        self.dict_count = collections.Counter(self.words)
        num = 0
        for i in sorted(self.dict_count.items(), key=lambda items: items[0], reverse=True):  # 字典中按照value排序
            self.top_5.append(i)
            num += 1
            if num == 5:
                break

    def display(self):
        file = open('../python/2016_out.txt', 'w')
        for i in range(5):
            file.write('{:<20s}{:>7d}{:3}'.format(self.top_5[i][0], self.top_5[i][1], '\n'))
            file.write('\n')
        file.close()


def main():
    s = Solution()
    s.create_file()
    s.read_file()
    s.deal()
    s.display()
