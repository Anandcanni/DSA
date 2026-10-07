class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        q = deque([s])
        visited = {s}
        answer = []

        while q:
            found = False

            for _ in range(len(q)):
                curr = q.popleft()

                if is_valid(curr):
                    answer.append(curr)
                    found = True
                    continue

                if found:
                    continue

                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue

                    new_s = curr[:i] + curr[i + 1:]

                    if new_s not in visited:
                        visited.add(new_s)
                        q.append(new_s)

            if found:
                return answer

        return [""]
        