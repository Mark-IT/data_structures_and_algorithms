# -*- coding: utf-8 -*-

class StackUnderflow(ValueError):  # 栈下溢（空栈访问）
    pass


class SStack:
    '''
    基于顺序表技术实现的栈类，所有栈操作都映射到list操作
    '''

    def __init__(self):
        self._elems = []  # 用list对象 _elems存储栈中元素

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self.is_empty():
            raise StackUnderflow('in SStack.top()')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('in SStack.top()')
        return self._elems.pop()


def check_parens(text):
    '''
    括号配对检查函数
    :param text: 被检查的字符串
    :return:
    '''
    parens = "()[]{}"  # 所有括号字符
    open_parens = "([{"  # 开括号字符
    opposite = {  # 括号的配对关系
        ")": "(",
        "]": "[",
        "}": "{"
    }

    def parenthese(text: str):
        '''
        括号生成器，每次调用返回text里的下一个括号及其位置
        :param text: 待检查的字符串
        :return:
        '''
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()  # 保存括号的栈

    for pr, i in parenthese(text):  # 对text里的各括号和位置进行迭代
        if pr in open_parens:  # pr为开括号，压进栈
            st.push(pr)
        elif st.pop() != opposite[pr]:  # pr为闭括号，寻找已入栈的是否是其对应的开括号
            print(f'索引值{i}处，发现不匹配括号：{pr}')
            return False  # 不匹配则退出
        # 匹配成功，则继续
    print('所有括号全部匹配成功')
    return True


if __name__ == '__main__':
    text1 = '{123(45[67]89)}'
    text2 = '{123(4567]89)}'
    print(check_parens(text1))
    print(check_parens(text2))
