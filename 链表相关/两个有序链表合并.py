# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 先解决特殊情况
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # 比较l1和l2的头节点，确定合并后的头结点

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            # 找到下一个节点后，向后移动cur节点，以便下次进行比较
            cur = cur.next

        if l1 is None:  # l1链表已遍历完，直接拼接剩余的l2
            cur.next = l2
        else:
            cur.next = l1
        return head