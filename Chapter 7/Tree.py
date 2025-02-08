tree = {}

tree[10] = [5, 20]
tree[5] = [2, 7]
tree[2] = [3, 6]
tree[7] = [44, 43]
tree[20] = [25, 1]
tree[25] = [100, 24]
tree[1] = [46, 87]

class Tree:
    def __init__(self, tree):
        self.tree = tree

    def displayChilds(self, val):
        print(self.tree[val])
    
    def displayParent(self, val):
        for key, value in self.tree.items():
            if val in value:
                print(key)
                break
        return -1
    
    def displayTree(self):
        for key, value in zip(self.tree.keys(), self.tree.values()):
            print(f"{key}: {value}")

if __name__ == "__main__":
    t = Tree(tree)
    print(t.displayTree())