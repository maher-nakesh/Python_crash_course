class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def insert(self,value):
        def __insert(node):
            if node.data > value:
                if node.left is not None:
                    __insert(node.left)
                    return
                node.left=TreeNode(value)

            if node.data <= value:
                if node.right is not None:
                    __insert(node.right)
                    return
                node.right=TreeNode(value)
        __insert(self)
    def PrintTree(self):
        def __print_tree(node):
            if node is not None:
                print(node.data)
                __print_tree(node.right)
                __print_tree(node.left)
        __print_tree(self)
    def PrintSmall(self):
        def __print_tree(node):
            if node is not None:
                __print_tree(node.left)
                __print_tree(node.right)
                print(node.data)

        return print( __print_tree(self))

dd=TreeNode(1)
dd.insert(5)
dd.insert(4)
dd.insert(3)
dd.insert(5)
dd.insert(1)


def filter_bst(tree_node, a, b):
    if tree_node is not None:
        if a <= tree_node.data and tree_node.data >= b :
            print(tree_node.data)
        if tree_node.data <a:
            filter_bst(tree_node.left,a,b)
        if tree_node.data>b:
            filter_bst(tree_node.right,a,b)
    return


def tree_levels(tree):
    levels_list=[]
    def print_levels(tree_node,level,levels_list):
        if level <= len(levels_list):
            levels_list.append([])
        levels_list[level].append(tree_node.data)
        print_levels(tree_node.left,level+1)
        print_levels(tree_node.right,level+1)
    return print(levels_list)
    print_levels(tree)
    for i in levels_list:
        print(levels_list[i])






tree_levels(dd)
dd.PrintTree()
