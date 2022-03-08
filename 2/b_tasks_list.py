class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node) -> None:
    while node:
        print(node.value)
        node = node.next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    print(node.value)
    return node


def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next_item = head
        return new_node
    previous_node = get_node_by_index(head, index - 1)
    new_node.next_item = previous_node.next_item
    previous_node.next_item = new_node
    return head

# def test():
node3 = Node("node3", None)
node2 = Node("node2", node3)
node1 = Node("node1", node2)
node0 = Node("node0", node1)
# solution(node0)
get_node_by_index(node0, 3)
#     # Output is:
#     # node0
#     # node1
#     # node2
#     # node3

