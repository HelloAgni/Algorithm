class Node:
    """
    Функция должна напечатать элементы списка по одному в строке.
    >>>from to_do_list import Node, solution
    >>>node3 = Node("node3 node3", None)
    >>>node2 = Node("node2 node2", node3)
    >>>node1 = Node("node1 node1", node2)
    >>>node0 = Node("node0", node1)
    >>>solution(node0)
    node0
    node1 node1
    node2 node2
    node3 node3
    None
    """
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node):
    while node:
        print(node.value)  # optional end=' -> '
        node = node.next_item
    print('None')  # if no elements -> None


# Make


# def solution(node):
#     while node:
#         print(node.value)
#         node = node.next_item


# def test():
#     node3 = Node("node3 node3", None)
#     node2 = Node("node2 node2", node3)
#     node1 = Node("node1 node1", node2)
#     node0 = Node("node0", node1)
#     solution(node0)
