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


priority = {"(": 1, "+": 3, "-": 3, "*": 5, "/": 5}  # 给开括号'('一个很低的优先级，是为了保证只有对应的')才能将其弹出'

infix_operators = "+-*/()"  # 把括号也看作运算符，但会进行特殊处理


def trans_infix_suffix(line):
    st = SStack()  # 用来存储运算符
    exp = []  # 用来记录转换得到的后缀表达式
    for x in tokens(line):
        if x not in infix_operators:
            exp.append(x)  # 将运算对象直接送出
        elif st.is_empty() or x == '(':  # 左括号进栈
            st.push(x)
        elif x == ')':  # 遇到右括号要一直弹出运算符，直到为空栈或遇到最近一个左括号停止
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())

            if st.is_empty():  # 没有找到左括号，就是不匹配
                raise SyntaxError("Missing '(' ")
            st.pop()  # 弹出左括号
        else:

            while (not st.is_empty() and priority[st.top()] >= priority[x]):  # 比较栈顶与当前运算符的优先级
                exp.append(st.pop())  # 将优先级高的运算符送入表达式中
            st.push(x)  # 算术运算符进栈
    while not st.is_empty():  # 送出栈里剩下的运算符
        if st.top() == '(':  # 如果还有左括号，就是不匹配
            raise SyntaxError("Extra '(' ")
        exp.append(st.pop())
    return exp


def tokens(line):
    '''
    生成器函数，逐一生成line中的一个个项。项是浮点数或运算符
    本函数不能处理一元运算符，也不能处理带符号的浮点数
    '''

    i, llen = 0, len(line)
    while i < llen:
        while i < llen and line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:  # 运算符
            yield line[i]  # 返回运算符
            i += 1
            continue
        j = i + 1  # 处理运算对象
        while (j < llen and not line[j].isspace() and line[j] not in infix_operators):  # 是运算对象
            if ((line[j] == 'e' or line[j] == 'E') and j + 1 < llen and line[j + 1] == '-'):  # 处理负指数
                j += 1
            j += 1
        yield line[i:j]  # 生成运算对象子串
        i = j


def test_trans_infix_suffix(s):
    print(s)
    suffix_list = trans_infix_suffix(s)
    print(suffix_list)
    print(''.join(suffix_list))


if __name__ == '__main__':
    test_trans_infix_suffix('(1+5*3)*(4/2)')
