class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                v = stack.pop()
                if i == ")" and v == "(":
                    continue
                if i == "}" and v == "{":
                    continue
                if i == "]" and v == "[":
                    continue
                return False

        return len(stack) == 0
