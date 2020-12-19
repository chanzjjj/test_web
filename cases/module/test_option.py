import pytest

def test_host_1(request):
    env = request.config.getoption("--host")
    print("case env: %s" % env)

def test_host_2(host_env):
    print("case env:%s" % host_env)
    # assert 0