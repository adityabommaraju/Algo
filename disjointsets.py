class Node:
    def __init__(self):
        self.data = 0.0
        self.parent = Node
        self.rank = 0


class Disjointset:
    map = dict()

    def makeset(self,data):

        node = Node()
        node.data = data
        node.parent = node
        node.rank = 0
        self.map[data] = node

    def union(self, data1, data2):
        node1 = self.map.get(data1)
        node2 = self.map.get(data2)

        parent1 = self.findset(node1)
        parent2 = self.findset(node2)

        if parent1 == parent2:
            return False

        if parent1.rank >= parent2.rank:
            parent1.rank = parent1.rank if parent1.rank == parent2.rank else parent2.rank + 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2
        return True

    def findsetnum(self, num=1):
        ### findset code
        return self.findset(self.map.get(num)).data

    def findset(self,node):
        ##### findset code
        parent = node.parent
        if parent == node:
            return parent
        node.parent = self.findset(node.parent)
        return node.parent


ds = Disjointset()
ds.makeset(1)
ds.makeset(2)
ds.makeset(3)
ds.makeset(4)
ds.makeset(5)
ds.makeset(6)
ds.makeset(7)

ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(5, 6)
ds.union(3, 7)

for i in range(1,8):
    print(ds.findsetnum(i))
