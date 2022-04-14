class Node:
    """
    Напишите функцию solution, которая принимает на вход голову списка и номер
    удаляемого дела и возвращает голову обновлённого списка.
    >>>from unloved_business import *
    >>>node3 = Node("node3", None)
    >>>node2 = Node("node2", node3)
    >>>node1 = Node("node1", node2)
    >>>node0 = Node("node0", node1)
    >>>print_linked_list(node0)
    node0 -> node1 -> node2 -> node3 -> Last is None
    >>>node, index, value = node1, 1, 'new_node'
    >>>head = add_node(node, index, value)
    >>>print_linked_list(head)
    node1 -> new_node -> node2 -> node3 -> Last is None
    >>>print_linked_list(node0)
    node0 -> node1 -> new_node -> node2 -> node3 -> Last is None
    >>>remove_node(node0, 1)
    >>>print_linked_list(node0)
    node0 -> new_node -> node2 -> node3 -> Last is None
    """
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    while idx:
        node = node.next_item
        idx -= 1
    return node


def add_node(head, idx, value):
    new_node = Node(value)
    if idx == 0:
        new_node.next_item = head
        return new_node
    previous_node = solution(head, idx-1)
    new_node.next_item = previous_node.next_item
    previous_node.next_item = new_node
    return head


def remove_node(head, idx):
    if idx == 0:
        head = head.next_item
    previous_node = solution(head, idx - 1)
    next_node = solution(head, idx + 1)
    previous_node.next_item = next_node
    return head


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next_item
    print('Last is None')


# Make

# def solution(node, idx):
#     def get_node(node, index):
#         while index:
#             node = node.next_item
#             index -= 1
#         return node
#     if idx == 0:
#         node = node.next_item
#     else:
#         previous_node = get_node(node, idx - 1)
#         next_node = get_node(node, idx + 1)
#         previous_node.next_item = next_node
#     return node


# def test():
#     node3 = Node("node3", None)
#     node2 = Node("node2", node3)
#     node1 = Node("node1", node2)
#     node0 = Node("node0", node1)
#     new_head = solution(node0, 1)
#     # result is node0 -> node2 -> node3
