# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/9/22 18:29

import pytest


class TestParam():

    @pytest.mark.parametrize("user,password", [('user001', 123456), ('admin', 88888888), (None, 111), ('123', None)])
    def test_login(self, user, password):
        print("输入用户名:", user)
        print("输入密码:", password)
        assert user is not None
        assert password is not None


if __name__ == '__main__':
    pytest.main()
