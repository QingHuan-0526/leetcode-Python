"""
leetcode20 ： 括号匹配
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 存储元素
        stack = []
        # 映射关系
        mappings = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in mappings:
                # 右
                top = stack.pop()if stack else "#"
                if top != mappings[c]:
                    return False
            else:
                # 左
                stack.append(c)
        return not stack

"""
注：
if stack   如果列表为空 则为false
top = stack.pop()if stack else "#"   先执行if 为空则返回"#"否则弹出第一个  解决了空指针问题
"""