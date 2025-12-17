from enum import Enum


def http_error(status: int):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


class Point:
    # 为属性指定其在模式中对应的位置
    __match_args__ = ("x", "y")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def where_is(point: Point):
    match point:
        case Point(1, 0):
            print("Origin")
        # 如果没有定义 __match_args__，则需要指明属性名
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0) as p:
            print(f"X={x}")
            print(p)
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point():
            print("Somewhere else")


def where_is2(points: list[Point]):
    match points:
        case []:
            print("No points")
        # 至少包含一项
        case [Point(0, 0), *_]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


if __name__ == "__main__":
    # x = int(input("Please enter an integer: "))

    words = ["cat", "window"]
    for index, w in enumerate(words):
        words[index] = w.upper()
    assert words == ["CAT", "WINDOW"]

    users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}
    # 如果不 copy 的话会出错
    # RuntimeError: dictionary changed size during iteration
    for user, status in users.copy().items():
        if status == "inactive":
            del users[user]
    assert users == {"Hans": "active", "景太郎": "active"}

    active_users = {}
    for user, status in users.items():
        if status == "active":
            active_users[user] = status

    # range 返回一个可迭代对象
    assert list(range(5, 10)) == [5, 6, 7, 8, 9]

    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, "equals", x, "*", n // x)
                break
        # 循环的 else 子句，如果循环在未执行 break 的情况下结束，else 子句将会执行
        else:
            print(n, "is a prime number")

    where_is(Point(0, 0))

    color = Color("red")

    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")

    d = {1: 2, 3: 4}
    match d:
        # 和 list 不同，其他的键会被忽略
        case {1: 2}:
            print("Dictionary with one item")
        # {} 会匹配任何字典
        case {**extra} if not extra:
            print("empty dict")
        case _:
            print("Something else")

    # 键字 in，用于确认序列中是否包含某个值
    print(1 in [1, 2, 3])


# 函数内的第一条语句是字符串时，该字符串就是文档字符串
# 没有返回值的函数返回 None
# 可以有默认参数
def fib(n: int = 2):
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


i = 5


def f(arg: int = i):
    print(arg)


i = 6
# 5，默认参数在函数定义时求值
# 如果默认值为列表、字典或类实例等可变对象时，结果会不同
f()


# 函数调用时，关键字参数必须跟在位置参数后面
# 标注以字典的形式存放在函数的 __annotations__ 属性中
def parrot(
    voltage: str,
    state: str = "a stiff",
    action: str = "voom",
    type: str = "Norwegian Blue",
):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print("-- This parrot is", voltage, "volts.")
    voltage.endswith("123")
