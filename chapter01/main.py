#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    # /xxx/Python-learning/chapter01/main.py
    print(sys.argv[0])

    # / 总是返回浮点数，想得到整数可以使用 //
    print(2 / 3)
    print(2 // 3)
    # 2^3
    print(2**3)
    # 原始字符串，不转义
    print(r"1\n2")
    # 包含多行，将自动添加换行符，可以使用 \ 来避免
    print(
        """\
123
123
"""
    )
    # 字符串合并，只能用于字面值
    print("1" + "2")
    print("1" "2")
    # 重复
    print("12" * 2)

    # str，不可变
    word = "Python"
    # 字符串长度
    print(len(word))
    # 索引，得到长度为 1 的字符串
    print(word[0])
    # 从右边开始计数，从 -1 开始，n
    print(word[-1])
    # slice
    print(word[1:3])
    print(word[-2:])
    # 自动处理越界，而索引不会
    print(word[42:])

    # list，可变，也支持索引和 slice
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    # 添加新元素
    letters.append("h")

    letters[2:5] = ["C", "D", "E"]
    print(letters)
    letters[2:5] = []
    print(letters)
