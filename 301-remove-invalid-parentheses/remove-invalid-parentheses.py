class Solution:
    def removeInvalidParentheses(self, s: str):
        ans = set()

        left_remove = 0
        right_remove = 0

        # Find minimum removals needed
        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        def dfs(index, balance, left_remove, right_remove, path):

            # Reached the end
            if index == len(s):
                if balance == 0 and left_remove == 0 and right_remove == 0:
                    ans.add("".join(path))
                return

            ch = s[index]

            # Option 1: Remove current '('
            if ch == '(' and left_remove > 0:
                dfs(
                    index + 1,
                    balance,
                    left_remove - 1,
                    right_remove,
                    path
                )

            # Option 2: Remove current ')'
            if ch == ')' and right_remove > 0:
                dfs(
                    index + 1,
                    balance,
                    left_remove,
                    right_remove - 1,
                    path
                )

            # Option 3: Keep current character
            path.append(ch)

            if ch not in "()":
                dfs(
                    index + 1,
                    balance,
                    left_remove,
                    right_remove,
                    path
                )

            elif ch == '(':
                dfs(
                    index + 1,
                    balance + 1,
                    left_remove,
                    right_remove,
                    path
                )

            elif ch == ')' and balance > 0:
                dfs(
                    index + 1,
                    balance - 1,
                    left_remove,
                    right_remove,
                    path
                )

            path.pop()

        dfs(0, 0, left_remove, right_remove, [])

        return list(ans)
        