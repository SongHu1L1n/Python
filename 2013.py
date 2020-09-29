class Graph:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class Solution:
    paths = []
    root = Graph(0)
    request_path = []
    out_path = []

    def read_file(self):
        import re
        left_brocket = re.compile('\[')
        right_brocket = re.compile('\]')
        with open(r'D:\python\2013data.txt', 'r') as file:
            num = int(file.readline().rstrip('\n'))
            while num:
                path = file.readline().rstrip('\n')
                path = right_brocket.sub('', left_brocket.sub('', path)).split(',')  # 去除左右括号，并拆分为列表

                self.paths.append(path)
                num -= 1

    def in_graph(self, root: Graph, name):
            if root:
                if root.name == name:
                    return root
                if root.left:
                    return self.in_graph(root.left, name)
                if root.right:
                    return self.in_graph(root.right, name)
            return None

    def create_relationship(self):
        for i in range(len(self.paths)):
            if i == 0:
                point1 = Graph(self.paths[i][0])
                point2 = Graph(self.paths[i][1])
                point1.left = point2
                self.root.left = point1
            else:
                pre, last = self.in_graph(self.root, self.paths[i][0]), self.in_graph(self.root, self.paths[i][1])
                if pre is not None:  # 第一个点已经在图当中
                    if last is None:  # 第二个点不在图中，新建
                        last = Graph(self.paths[i][1])
                    if pre.left is None:
                        pre.left = last
                    else:
                        pre.right = last
                else:  # 第一个点不在图中
                    pre = Graph(self.paths[i][0])
                    self.root.right = pre  # 若为孤立结点，将其赋给root的右子树
                    if not last:  # 第二个点不在， 新建
                        last = Graph(self.paths[i][1])
                    if pre.left is None:
                        pre.left = last
                    else:
                        pre.right = last

    def request_file(self):
        with open(r'D:\python\2013request.txt', 'r') as file:
            import re
            left_brocket = re.compile('\[')
            right_brocket = re.compile('\]')
            num = int(file.readline().rstrip('\n'))
            while num:
                path = file.readline().rstrip('\n')
                path = right_brocket.sub('', left_brocket.sub('', path)).split(',')
                self.request_path.append(path)
                num -= 1
            print(self.request_path)

    def deal(self):
        for path in self.request_path:
            step = int(path[2])
            start = self.in_graph(self.root, path[0])
            end = self.in_graph(self.root, path[1])
            if step == self.find_path(start, end, 0):
                self.out_path.append([path[0], path[1], 'YES'])
            else:
                self.out_path.append([path[0], path[1], 'NO'])

    def find_path(self, start, end, count):
        if start:
            if start == end:
                return count
            elif start.left:
                return self.find_path(start.left, end, count + 1)
            elif start.right:
                return self.find_path(start.right, end, count + 1)
            else:
                return -1