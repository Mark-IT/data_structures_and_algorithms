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
    def depth(self):  # 检查栈的深度
        return len(self._elems)


def suffix_exp_evaluator(line):
    '''
    假定后缀表达式里的不同的项和运算符之间都有空格
    :param line:
    :return:
    '''
    return suf_exp_evaluator(line.split())


def suf_exp_evaluator(exp):
    operators = '+-*/'
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))  # 不能转换将自动引发异常
            continue

        if st.depth() < 2:  # x必为运算符，栈元素不够时抛出异常
            raise SyntaxError('Short of operand(s)')

        a = st.pop()  # 取得第二个运算对象
        b = st.pop()  # 取得第一个运算对象

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        else:
            break
        st.push(c)
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s)")


# def suffix_exp_calculator():
# while True:
#     try:
#         line = input("Suffix Expression: ")
#         if line == 'end':
#             return
#         res = suffix_exp_evaluator(line)
#         print(res)
#     except Exception as e:
#         print("Error: ", type(e), e.args)


if __name__ == '__main__':
    # suffix_exp_calculator()
    print(suffix_exp_evaluator('1 2 +') == 3)
