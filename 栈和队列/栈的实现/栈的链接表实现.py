# -*- coding: utf-8 -*-

class StackUnderflow(ValueError):  # 栈下溢（空栈访问）
    pass


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack:
    '''
    基于连接表技术实现的栈类，用LNode作为结点
    对于链接表，前端插入和删除都是0(1)操作，应该用前端作为栈顶
    '''

    def __init__(self):
        self._top = None

    def is_empty(self):  # 判断栈是否为空
        return self._top is None

    def top(self):  # 返回栈里最后压入的元素，并将其返回（不删除）
        if self._top is None:
            raise StackUnderflow('in LStack.top()')
        return self._top.elem

    def push(self, elem):  # 将元素elem压入栈
        self._top = LNode(elem, self._top)

    def pop(self):  # 删除栈里最后压入的元素并将其返回
        if self._top is None:
            raise StackUnderflow('in LStack.top()')
        p = self._top
        self._top = p.next
        return p.elem
