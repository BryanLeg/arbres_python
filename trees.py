class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def add_child(self, value):
        self.children.append(Tree(value))

    def is_leaf(self):
        return len(self.children) == 0

    def get_children(self):
        return self.children

    def get_depth(self):
        if self.is_leaf():
            return 1
        
        depth_list = [child.get_depth() for child in self.children]

        return max(depth_list) + 1
    
    def dfs(self)  -> list:
        if self.is_leaf():
            return [self.value]
        
        result_list = []
        for child in self.children:
            result_list += child.dfs()
        result_list.append(self.value)
        return result_list


root = Tree(1)
root.add_child(2)
root.add_child(3)
root.add_child(4)

node_2 = root.get_children()[0]
node_2.add_child(5)
node_2.add_child(6)
node_2.add_child(7)

node_3 = root.get_children()[1]
node_3.add_child(8)
node_3.add_child(9)

node_5 = node_2.get_children()[0]
node_5.add_child(10)
# print((root.get_children()))

print(root.get_depth())
print(root.dfs())