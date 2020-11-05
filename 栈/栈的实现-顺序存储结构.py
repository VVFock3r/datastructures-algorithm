#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
顺序存储结构的栈实现
'''


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
