# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:  # 快慢指针，快指针追上慢指针，说明有环
                return True
        return False  # 快指针已到达尽头，仍然为成环


if __name__ == '__main__':
    head = None
    print(Solution().hasCycle(head))

    head = ListNode(1)
    print(Solution().hasCycle(head))

    head.next = ListNode(2)

    head.next.next = head
    print(Solution().hasCycle(head))
