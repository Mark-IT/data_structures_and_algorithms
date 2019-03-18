# -*- coding: utf-8 -*-

class QueueUnderflow(ValueError):
    pass


class SQueue:
    '''
    可以自动扩充存储的队列类
    '''

    def __init__(self, init_len=8):
        '''
        设置列队的初始状态
        :param init_len: 指定表的初始长度，默认长度为8
        '''
        self._len = init_len  # 记录存储区的有效容量
        self._elems = [0] * init_len  # 引用着队列的元素存储区
        self._head = 0  # 队列中首元素下表（在队列中最早存入的那个元素）
        self._num = 0  # 记录队列中元素的个数

    def is_empty(self):
        return self._num == 0

    def peek(self):
        '''
        取得队列首元素
        :return:
        '''
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:  # 队列满了自动扩容
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        '''
        将存储区长度加倍，把原有元素搬迁到新表里（最前面的位置）
        :return:
        '''
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0
