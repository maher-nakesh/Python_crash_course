
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_list(self):
        node = self.head
        while node is not None:
            print(node, end=' ')
            node = node.next
        print('')

    def add_at_head(self, node):
        node.next = self.head
        self.head = node
        self.length += 1

    def remove_node_after(self, node):
        if node.next is not None:
            temp = node.next
            node.next = node.next.next
            temp.next = None
            self.length -= 1

    def remove_first_node(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

    def print_backward(self):
        def print_nodes_backward(node):
            if node.next is not None:
                print_nodes_backward(node.next)
            if node is not None:
                print(node, end=' ')

        if self.head is not None:
            print_nodes_backward(self.head)

        print('')
    def __str__(self):
        res = ""
        ptr = self.head
        while ptr:
            res += str(ptr.data) + ", "
            ptr = ptr.next
        res = res.strip(", ")

        if len(res):
            return "[" + res + "]"
        else:
            return "[]"


ll=LinkedList()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

ll.add_at_head(node1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current=ll.head
def lowest(l, k):
    min =l.head.data
    current=l.head
    count=0
    while current.next is not None :
        if current.next.data < min :
            min=current.next.data
            current=current.next
            count+=1
        else:
            current=current.next
    if min < count:
        return min
    else:
        return None
print(lowest(ll,5))

print(ll)

def equal_linked_lists(linked_list_1, linked_list_2):
    current1=linked_list_1.head
    current2=linked_list_2.head
    while current1.next is not None and current2.next is not None:
        if (current1.data == current2.data) and (current1.next.data != current2.next.data):
            return False
        else :
           return True


