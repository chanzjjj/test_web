import pytest
from pytest import assume

def test_a():
    print("111111111")
    a = "hello"
    b = "hello world"
    print(a)
    # assert a in b
    # pytest.assume(a == b)
    # with assume:
    #     assert a == b
    # # 断言通过，后面的代码会继续
    # print("断言后：%s" % b)

    # pytest.assume(a in b)
    with assume:
        assert a in b
    print("断言失败后：%s" % b)


def test_b():
    print("22222222")
    a = "hello"
    b = "hello world"
