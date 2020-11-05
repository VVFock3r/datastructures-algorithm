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


def postfix(exp):
    '''将中缀表达式转为后缀表达式
        9+(3-1)*3+10/2 -> 9 3 1 - 3 * + 1 0 2 / +
        (1+6)/2-2      -> 1 6 + 2 / 2 -
    '''

    stack = Stack()  # 栈初始化
    high = ['*', '/']  # 高优先级符号
    low = ['-', '+']  # 低优先级符号
    output = []  # 输出列表
    tmp = ""  # 将连续数字作为一个整体临时使用的存储变量

    # 表达式以-开头，那么开头补0
    if exp.startswith("-"):
        exp = "0" + exp

    # 遍历表达式
    for index, i in enumerate(exp):

        # 如果是连续的数字，需要将连续的数字看做是一个整体，对连续数字只做一次循环
        if i.isdigit() or i == ".":
            tmp += i
            try:
                if exp[index + 1].isdigit() or exp[index + 1] == ".":
                    continue
            except IndexError:
                pass

        if i.replace(".", "").isdigit():
            i = tmp
        else:
            tmp = ""

        # 数字直接输出
        if i.replace(".", "").isdigit():
            output.append(i)
            continue

        # 优先级高的和左括号入栈
        if (i in high) or (i == '('):
            stack.push(i)
            continue

        # 遇到右括号，出栈直到遇到左括号，并将左括号出栈扔掉
        if i == ")":
            while True:
                if stack.peek() == "(":
                    stack.pop()
                    break
                else:
                    output.append(stack.pop())
            continue

        # 优先级低的和栈顶元素比较
        #   栈顶优先级高，全部出栈，然后将元素入栈
        #   栈顶优先级低，低优先级元素全部出栈，本次元素再入栈
        if (i in low):
            if stack.peek() in high:
                while not stack.is_empty():
                    output.append(stack.pop())
            if stack.peek() in low:
                while stack.peek() in low:
                    output.append(stack.pop())
            stack.push(i)
            continue

    # 输出栈内所有元素
    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)


def calc(exp):
    '''后缀表达式计算'''

    stack = Stack()
    for i in exp.split():
        if i.replace(".", "").isdigit():
            stack.push(float(i))
            continue

        b = stack.pop()
        c = stack.pop()
        if i == "+":
            stack.push(c + b)
        elif i == '-':
            stack.push(c - b)
        elif i == '*':
            stack.push(c * b)
        elif i == "/":
            stack.push(c / b)

    return stack.pop()


# 20
print(
    calc(
        postfix("9+(3-1)*3+10/2")
    )
)

# 18
print(
    calc(
        postfix("10-1+9")
    )
)

# 631
print(
    calc(
        postfix("30*(2+100)/5-1+20")
    )
)

# -199495
print(
    calc(
        postfix("(10+5)/3+500-1000*200")
    )
)

# 26
print(
    calc(
        postfix("1+2+3+4+5-6+7-8+9*2")
    )
)

# 0.5
print(
    calc(
        postfix("1+(2*3/4)-2")
    )
)

# 53.33333333333333
print(
    calc(
        postfix("100*100/300+20")
    )
)

# 15
print(
    calc(
        postfix("-1+10-2+4*2")
    )
)

# -3
print(
    calc(
        postfix("-1.2*5+3")
    )
)
