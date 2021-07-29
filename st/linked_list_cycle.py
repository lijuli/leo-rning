# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __str__(self):
    #     return f'[{self.val}]->{self.next}'


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return None
        list_set = set()
        list_set.add(head)
        item = head
        while item.next is not None:
            if item.next in list_set:
                return item.val
            list_set.add(item)
            item = item.next
        return None


if __name__ == "__main__":
    s = Solution()
    linked_list1 = ListNode(3)
    linked_list2 = ListNode(2)
    linked_list3 = ListNode(0)
    linked_list4 = ListNode(-4)
    linked_list1.next = linked_list2
    linked_list2.next = linked_list3
    linked_list3.next = linked_list4
    linked_list4.next = linked_list2
    # print(linked_list1)
    print(s.hasCycle(linked_list1))
