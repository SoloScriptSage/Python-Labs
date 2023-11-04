#Binary-tree

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.__root = None

    def isEmpty(self):
        return self.__root == None

    #insert-node
    def __insert(self, value, node):
        if node is None:
            node = Node(value)
        elif value < node.data:
            node.left = self.__insert(value, node.left)
        elif value > node.data:
            node.right = self.__insert(value, node.right)

        return node

    def insert(self, value):
        self.__root = self.__insert(value, self.__root)

    #preorder-NodeLeftRight
    def __preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.__preorder(node.left)
            self.__preorder(node.right)

    def preorder(self):
        self.__preorder(self.__root)
        print()

    #inorder-LeftNodeRight
    def __inorder(self, node):
        if node is not None:
            self.__inorder(node.left)
            print(node.data, end=' ')
            self.__inorder(node.right)

    def inorder(self):
        self.__inorder(self.__root)
        print()

    #postorder-LeftRightNode
    def __postorder(self, node):
        if node is not None:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(node.data, end=' ')

    def postorder(self):
        self.__postorder(self.__root)
        print()

    #binarysearch-ontree
    def __search(self, key, node):
        if node is None:
            return None
        elif node.data == key:
            return node
        elif key < node.data:
            return self.__search(key, node.left)
        elif key > node.data:
            return self.__search(key, node.right)

    def search(self, key):
        return self.__search(key, self.__root)

def main():
    tree = BinaryTree()
    testData = [5,3,1,7,2,4,9,8,6]

    for value in testData:
        tree.insert(value)

    print("Preorder:", end=' ')
    tree.preorder()

    print("Inorder:", end=' ')
    tree.inorder()

    print("Postorder:", end=' ')
    tree.postorder()

    key = 0
    while key != -1:
        key = int(input("Search key (-1 to quit): "))
        match key:
            case -1:
                quit()
            case _:
                node = tree.search(key)
                if node is None:
                    print("Key wasn't found!")
                else:
                    print(f"Found key - ", key)
                    if node.left is not None:
                        print(f"Left - {node.left.data}")
                    else:
                        print("None", end=' ')

                    if node.right is not None:
                        print(f"Right - {node.right.data}")
                    else:
                        print("None", end=' ')



main()
