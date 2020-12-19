import pytest

# request.param只有在fixture里面才能拿到

@pytest.fixture(params=["user1", "user2", "user3"])
def register_uer(request):
    user = request.param     # 获取测试数据
    print("拿着账号去注册：%s" % user)
    result = {"code": 0, "msg": "success"}
    return user, result

def test_register(register_uer):
    # 拿到前面的测试数据
    user, actual_result = register_uer
    print("case: %s" % user)
    print("实际结果：%s" % actual_result)
    assert actual_result["msg"] == "success"