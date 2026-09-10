class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("infinity")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            # This character now meets the required amount
            if char in countT and window[char] == countT[char]:
                have += 1

            # The window contains every required character
            while have == need:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Remove the left character to shrink the window
                leftChar = s[left]
                window[leftChar] -= 1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1

                left += 1

        left, right = res
        return s[left:right + 1] if resLen != float("infinity") else ""