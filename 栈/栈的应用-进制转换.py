#!/usr/bin/env python
# -*- coding:utf-8 -*-


class StackEmptyError(Exception): pass


class Stack:
    def __init__(self):
        '''栈初始化，为空列表'''
        self._stack = []

    def is_empty(self):
        '''判断栈是否为空'''
        return self._stack == []

    def size(self):
        '''返回栈大小'''
        return len(self._stack)

    def pop(self):
        '''元素出栈'''
        if self.is_empty():
            raise StackEmptyError("pop from empty stack")
        return self._stack.pop()

    def push(self, item):
        '''元素入栈'''
        self._stack.append(item)

    def peek(self):
        '''仅返回栈顶元素'''
        if self.is_empty():
            return None
        return self._stack[-1]


def scale(src, base=2):
    '''
    将10进制数字转换为base进制，暂不支持大于10进制数字

    进制转换规则：
        将数字与进制数取模运算，模数放到最终转换成的数字 从右向左排列，
        将数字整除进制数，得到一个新数字
        使用新数字循环上面步骤，直到新数字为1

        将最终转换的数字从左向右连起来，即是最终数字        
    '''
    stack = Stack()
    dst = ''
    if src == 0:
        stack.push(0)
    while src > 0:
        mod = src % base
        stack.push(mod)
        src = src // base
    while not stack.is_empty():
        dst += str(stack.pop())
    return dst


print(scale(500, 2))  # 111110100
