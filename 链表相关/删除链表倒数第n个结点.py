# -*- coding: utf-8 -*-

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
说明：
给定的 n 保证是有效的。
进阶：
使用一趟扫描实现
"""


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    '''
    要删除倒数第n个节点则需要找到倒数第n+1个节点(x)，将其x.next= x.next.next
    如何找到倒数第n+1个节点呢？
    我们可以采用双指针法
    具体看代码
    '''

    def removeNthFromEnd(self, head, n):  # n一定是有效值
        dummy = ListNode()
        dummy.next = head  # 为简化特殊情况，如只有一个节点等情况，我们在头结点前增设一个哑节点作为新的头结点

        first = second = dummy  # first,second指针都指向新的头节点

        for _ in range(n + 1):
            first = first.next  # first提前走n+1步
        # 此时first 和second 相距n+1个节点
        while first:
            first = first.next
            second = second.next
        # 当first 为最后一个节点时，second距first n+1 个节点即第倒数第n+2个节点
        # 由于终止条件是first为None时,second又往前走了一步，所以此时second是倒数第n+1个节点

        # 现在已经找到到了倒数第n+1个节点（second），可以进行删除倒数第n个节点的操作了

        second.next = second.next.next

        return dummy.next
