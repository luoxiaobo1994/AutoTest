# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/12/6 20:25

"""
1. 转换后的字符串只保留字母[a-zA-Z]和数字[0-9]，去除其他字符；
2. 输入字符串中的字母字符的前一字符如非字母或数字，该字母转换后为大写，其他字母转换后为小写；
    例外：转换后的字符串第一个字符如果是字母，则该字母转换后为小写；
3. 转换后的字符串保留数字字符。
4. 字符串如果为空或者无[a-zA-Z]和数字[0-9]中字符，请默认输出如下字符串"shopee"
"""

import string


class Solution:
    def camelCase(self, newString):
        # write code here
        if len(newString)==0:
            return 'shopee'
        str_ls = []
        pattern = string.ascii_letters + string.digits
        for i in range(len(newString)):
            if i == 0 and newString[i] in pattern:
                str_ls.append(newString[i].lower())
            else:
                if newString[i] not in pattern:
                    pass
                elif newString[i - 1] not in pattern:
                    str_ls.append(newString[i].upper())
                else:
                    str_ls.append(newString[i])
        return ''.join(str_ls)


s = Solution()
print(s.camelCase('Https___98)pYthHn*535'))
