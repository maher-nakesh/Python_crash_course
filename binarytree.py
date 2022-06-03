 def PrintSmall(self):
        def __print_tree(node):
            if node is not None:
                __print_tree(node.left)
                __print_tree(node.right)
                print(node.data)

        return print( __print_tree(self))
#========================================================
def filter_bst(tree_node, a, b):
    if tree_node is None:
        return
    if tree_node.data >=a and tree_node.data <= b :
        print(tree_node.data)
    if tree_node.data >a:
        filter_bst(tree_node.left,a,b)
    if tree_node.data<b:
        filter_bst(tree_node.right,a,b)
    return
#========================================================
def tree_levels(tree):
    l=[]
    def trees(tree):

        if tree is None:
            return
        else:
            trees(tree.left)
            trees(tree.right)
            l.append(tree.data)
            return
    trees(tree)
    return  print(l)