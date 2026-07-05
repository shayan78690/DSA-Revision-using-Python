class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        self.func(digits, phone, 0, [], result)

        return result

    def func(self, digits, phone, index, current, result):

        if index == len(digits):
            result.append("".join(current))
            return

        letters = phone[digits[index]]

        for ch in letters:
            current.append(ch)

            self.func(digits, phone, index + 1, current, result)

            current.pop()
