# -*- coding: utf-8 -*-


def is_palindrome(s: str) -> bool:
    length = len(s)
    if not s:  # 空字符串
        return True
    mid_index = length // 2  # 如果s长度为奇数则是中点，偶数则是后面那个中点
    index = 0
    status = True
    while index < mid_index:
        if s[index] == s[length - 1 - index]:
            index += 1
        else:
            status = False
            break
    return status


if __name__ == '__main__':
    print(is_palindrome(''))
    print(is_palindrome('122'))
    print(is_palindrome('1221'))
