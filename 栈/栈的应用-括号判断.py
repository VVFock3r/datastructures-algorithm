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


"""
    使用堆栈来解决问题

    遍历字符串
        不是右括号
            入栈
        是右括号
           栈没数据 False
           对应左括号 ！= 栈顶  False
"""


def is_valid(s):
    m = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c not in m:
            stack.append(c)
        elif not stack or m[c] != stack.pop():
            return False
    return not stack


s1 = "{}"
s2 = "[{}]"
s3 = ")("
s4 = "[{(})]"

print(is_valid(s1))
print(is_valid(s2))
print(is_valid(s3))
print(is_valid(s4))
