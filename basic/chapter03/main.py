if __name__ == "__main__":
    # 浮点数
    assert 8 / 5 == 1.6
    # 整数
    assert 8 // 5 == 1
    # 原始字符串，不转义
    # 不能以奇数个反斜杠结束
    # https://docs.python.org/zh-cn/3.13/faq/design.html#why-can-t-raw-strings-r-strings-end-with-a-backslash
    assert R"C:\some\name" == "C:\\some\\name"
    # 跨越多行
    help_msg = """\
Usage: thingy [OPTIONS]
-h                        Display this usage message
-H hostname               Hostname to connect to
"""
    # 字符串拼接
    assert 3 * "un" + "ium" == "unununium"
    # 字符串合并
    assert "Python" == "Python"
    # 字符串不可变
    word = "Python"
    # 单字符没有专用的类型，就是长度为一的字符串
    assert word[0] == "P"
    # 用负数索引时，从右边开始计数：-1 是最后一个字符
    assert word[-1] == "n"
    # 切片
    assert word[0:2] == "Py"
    # 从倒数第二个 (含) 到末尾
    assert word[-2:] == "on"
    # 索引越界会报错，而切片会自动处理越界索引
    assert word[42:] == ""

    squares = [1, 4, 9, 16, 25]
    assert (squares + [36, 49, 64, 81, 100]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    rgb = ["Red", "Green", "Blue"]
    rgba = rgb
    # 指向同一个对象
    assert id(rgba) == id(rgb)

    list1 = [[1, 2, 3], [4, 5, 6]]
    # 切片操作返回包含请求元素的新列表
    # Python 中的简单赋值绝不会复制数据，浅拷贝
    list2 = list1[1:]
    list2[0].append(42)
    assert id(list1[1]) == id(list2[0])
    assert list1 == [[1, 2, 3], [4, 5, 6, 42]]
    assert list2 == [[4, 5, 6, 42]]

    letters = ["a", "b", "c", "d", "e", "f", "g"]
    # 切片赋值，可以改变列表
    letters[2:5] = ["C", "D", "E"]
    assert letters == ["a", "b", "C", "D", "E", "f", "g"]

    i = 42
    # 各参数项之间会插入一个空格
    print("The value of i is", i)
