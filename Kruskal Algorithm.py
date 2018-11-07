class Kruskal:
    def __init__(self):
        self.root = {}
        self.rank = {}

    def make_set(self,point):
        self.root[point] = point
        self.rank[point] = 0

    def find_root(self, point):
        if self.root[point] != point:
            self.root[point] = self.find_root(self.root[point])

        return self.root[point]

    def union(self, u, v):
        self.root1 = self.find_root(u)
        self.root2 = self.find_root(v)

        if self.root1 != self.root2:
            if self.rank[self.root1] > self.rank[self.root2]:
                self.root[self.root2] = self.root1
            else:
                self.root[self.root1] = self.root2

                if self.rank[self.root1] == 0:
                    self.rank[self.root2] += 1

    def kruskal(self, graph):
        for point in graph['vertices']:
            self.make_set(point)

        self.mst = []
        edges = graph['edges']
        edges.sort()

        for edge in edges:
            w, v, u = edge

            if self.find_root(v) != self.find_root(u):
                self.union(v, u)
                self.mst.append(edge)
        print(self.mst)

gragh = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (7, 'B', 'A'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (8, 'C', 'B'),
    (5, 'C', 'E'),
    (5, 'D', 'A'),
    (9, 'D', 'B'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (7, 'E', 'B'),
    (5, 'E', 'C'),
    (15, 'E', 'D'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (6, 'F', 'D'),
    (8, 'F', 'E'),
    (11, 'F', 'G'),
    (9, 'G', 'E'),
    (11, 'G', 'F'),
    ]
}

k = Kruskal()
k.kruskal(gragh)