class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def delete_node(node, idx):
    if idx == 0:
        next_node = get_node_by_index(node, idx + 1)
        return next_node
    prev_node = get_node_by_index(node, idx-1)
    current_node = get_node_by_index(node, idx)
    prev_node.next_item = current_node.next_item
    return node


def solution(node, idx):
    node = delete_node(node, idx)
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    # result is node0 -> node2 -> node3
