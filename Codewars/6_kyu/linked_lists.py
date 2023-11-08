"""
Write a RemoveDuplicates() function which takes a list sorted
in increasing order and deletes any duplicate nodes from the list.
Ideally, the list should only be traversed once.
The head of the resulting list should be returned.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def check_nodes():
    """Test"""
    arr = Node(1)
    arr.next = Node(2)
    arr.next.next = Node(3)
    arr.next.next.next = Node(3)
    c = remove_duplicates(arr)
    new = []
    while c:
        new.append(c.data)
        c = c.next
    return new


print(check_nodes())
