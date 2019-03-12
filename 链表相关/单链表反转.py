# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:  # 空或单节点,直接返回
            return head
        pre = None  # 倒置后的最后一个节点，必为None
        cur = head  # 当前要进行倒置的节点
        nxt = head.next  # 指向当前要倒置的节点的下一个节点

        while nxt:
            cur.next = pre  # 指向前一个节点，进行反转

            # 两个节点倒置完成后，将pre,cur,nxt整体右移一次

            pre = cur
            cur = nxt
            nxt = cur.next

        # 此时 cur是最后一个节点，需要进行最后一次反转

        cur.next = pre

        return cur
