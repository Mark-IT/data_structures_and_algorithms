# -*- coding: utf-8 -*-

'''
思路

1. 我们需要找到链表中点(快慢指针法)
2. 将链表后半段倒置逆序排序
3. 将前半段和后半段遍历比较，判断是否为回文链表，偶数情况，使用偶数定位中点策略，要确定是返回上中位数或下中位数

注意事项：

快慢指针定位中点时要区分奇偶情况，奇数情况，中点位置不需要矫正，偶数情况，使用偶数定位中点策略，要确定是返回上中位数或下中位数
如果是返回上中位数，后半部分串头取next，如果是返回下中位数，后半部分串头既是当前节点位置，但前半部分串尾要删除掉当前节点
'''


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution(object):
    def is_palindrome(self, head: ListNode) -> bool:
        if head is None:  # 空
            return False
        if head.next is None:  # 1个节点
            return True
        slow = fast = head

        # 1. 定中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 快慢指针定位中点，此时fast已到达链尾，如果长度为奇数，则slow到达中心点，长度为偶数，则slow到达下中位点

        # 2. 后半段倒置

        pre = None  # 倒置后的最后一个节点必为None,以此确定第三步遍历时的终点
        cur = slow  # 当前要倒置的第一个节点
        nxt = slow.next  # 当前要倒置的节点的下一个节点

        while nxt:  # 只要没有到达原链表的终点就一直进行倒置

            cur.next = pre  # 将当前节点的下一个节点指向"前"一个节点，进行倒置

            # 相邻节点倒置完成后，向后整体偏移1个单位

            pre = cur
            cur = nxt
            nxt = cur.next

        # 当前cur是最后一个节点，需要和它前面的节点进行最后一次倒置，来完成整个后半段倒置

        cur.next = pre

        # 3. cur就是倒置完成后的后半段的头节点,同时遍历cur和head，如果遍历完cur未出现不同的节点，则为回文链表

        while cur.next:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next
        # 此时cur为后半段的最后一个节点，还需要判断此时的cur和head的值是否相同

        return cur.val == head.val


if __name__ == '__main__':
    # head =None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)

    print(Solution().is_palindrome(head))