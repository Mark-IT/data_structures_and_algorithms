# -*- coding: utf-8 -*-

class StackUnderflow(ValueError):  # 栈下溢（空栈访问）
    pass


class SStack:
    '''
    基于顺序表技术实现的栈类，所有栈操作都映射到list操作
    对于顺序表，后端插入和删除是O(1)操作，应该用后端作为栈顶
    '''

    def __init__(self):
        self._elems = []  # 用list对象 _elems存储栈中元素

    def is_empty(self):  # 判断栈是否为空
        return self._elems == []

    def top(self):  # 返回栈里最后压入的元素，并将其返回（不删除）
        if self.is_empty():
            raise StackUnderflow('in SStack.top()')
        return self._elems[-1]

    def push(self, elem):  # 将元素elem压入栈
        self._elems.append(elem)

    def pop(self):  # 删除栈里最后压入的元素并将其返回
        if self.is_empty():
            raise StackUnderflow('in SStack.top()')
        return self._elems.pop()


class ESStack(SStack):
    def depth(self):
        return len(self._elems)


if __name__ == '__main__':
    st1 = SStack()
    st1.push(1)
    st1.push(2)
    while not st1.is_empty():
        print(st1.pop())
