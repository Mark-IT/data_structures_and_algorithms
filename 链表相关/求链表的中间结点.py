# -*- coding: utf-8 -*-

'''
要求：

给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
'''

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    '''
    快慢指针法，快指针每次走2步，慢指针每次走1步，当快指针到达链尾时，慢指针到达中间结点
    '''
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



