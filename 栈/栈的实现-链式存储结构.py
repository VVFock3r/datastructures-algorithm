#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
链式存储结构的栈实现
'''


class StackEmptyError(Exception): pass


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        '''栈初始化，栈顶为None'''
        self._top = None
        self._size = 0

    def is_empty(self):
        '''判断栈是否为空'''
        return self._top is None

    def size(self):
        '''返回栈大小'''
        return self._size

    def push(self, data):
        '''入栈'''
        self._top = Node(data, next=self._top)
        self._size += 1

    def pop(self):
        '''出栈'''
        if self.is_empty():
            raise StackEmptyError("pop from empty stack")
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def peek(self):
        '''查看栈顶元素'''
        if self.is_empty():
            return None
        return self._top.data
