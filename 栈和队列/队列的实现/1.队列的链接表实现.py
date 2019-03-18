# -*- coding: utf-8 -*-

class LinkedListUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:
    def __init__(self):  # 创建空表 O(1)
        self._head = None
        self._rear = None  # 初始化尾结点引用域

    def is_empty(self):  # 判断空表：O(1)
        return self._head is None

    def peek(self):  # O(1)
        '''
        取得队列首元素
        :return:
        '''

        return self._head

    def dequeue(self):  # 首端删除元素O(1)
        '''
        删除表头节点并返回这个结点里的数据
        :return:
        '''
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def enqueue(self, elem):  # 尾端加入元素O(1)
        '''
        在链表的最后插入元素
        :param elem:
        :return:
        '''

        if self._head is None:  # 是空表
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
