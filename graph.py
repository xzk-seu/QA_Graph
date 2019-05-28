"""
@description: 图结构的基类
@author: Xu Zhongkai
@email: 1399350807@qq.com
@time: 2019-05-27
@version: 0.0.1
"""

import networkx as nx
import json
import os


class Graph(nx.MultiDiGraph):
    def __init__(self, graph=None, file_name=None):
        if file_name:
            path = os.path.join(os.getcwd(), 'export', '%s.json' % file_name)
            try:
                with open(path, 'r', encoding='utf-8') as fr:
                    data = json.load(fr)
                graph = nx.node_link_graph(data)
            except Exception as e:
                print(e)
        nx.MultiDiGraph.__init__(self, graph)

    def export(self, file_name):
        """将图导出至文件"""
        temp_graph = nx.MultiDiGraph(self)
        data = nx.node_link_data(temp_graph)
        dir_path = os.path.join(os.getcwd(), 'export')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, '%s.json' % file_name)
        with open(file_path, 'w', encoding='utf-8') as fw:
            json.dump(data, fw)

    def show(self):
        """将图显示至屏幕"""
        if not self:
            print("There is nothing to show!")
            return
        flag = True
        if not self.is_multigraph():
            flag = False
        print('=================The graph have %d nodes==================' % len(self.nodes))
        for n in self.nodes:
            data = self.node[n]
            print(str(n).ljust(30), '\t', str(data).ljust(30))
        # print('=================The graph have %d edges==================' % len(self.edges))
        print('The graph have %d edges'.center(100, '=') % len(self.edges))
        for e in self.edges:
            # multigraph的边结构为(u, v, k)
            # 非multigraph的边结构为(u, v)
            if flag:
                data = self.get_edge_data(e[0], e[1], e[2])
            else:
                data = self.get_edge_data(e[0], e[1])
            print(str(e).ljust(30), '\t', str(data).ljust(30))


if __name__ == '__main__':
    test_graph = nx.complete_graph(5)
    g = Graph(test_graph)
    g.show()
    g.export('text')
