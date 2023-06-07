# Correction


class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)

    def add_child(self, noeud) -> None:
        self.children.append(noeud)

    def is_leaf(self):
        return len(self.children) == 0

    def get_depth(self) -> int:
        if self.is_leaf():
            return 1
        
        depth_list = [child.get_depth() for child in self.children]

        # depth_list = []
        # for child in self.children:
        #     depth_list.append(child.get_depth())

        return max(depth_list) + 1
    
    def dfs(self)  -> list:
        if self.is_leaf():
            return [self.value]
        
        result_list = []
        for child in self.children:
            result_list += child.dfs()
        result_list.append(self.value)
        return result_list

    def bfs(self) -> list:
        queue = [self]
        result = []
        while len(queue) != 0:
            elt = queue.pop(0)
            result.append(elt.value)
            for child in elt.children:
                queue.append(child)
        return result

root = Tree(0)
node_1 = Tree(1)
node_2 = Tree(2)
node_3 = Tree(3)
node_4 = Tree(4)
node_5 = Tree(5)
node_6 = Tree(6)
node_7 = Tree(7)

root.add_child(node_1)
root.add_child(node_2)

node_1.add_child(node_3)
node_1.add_child(node_7)
node_2.add_child(node_5)

node_3.add_child(node_4)

node_4.add_child(node_6)

print(root.bfs())