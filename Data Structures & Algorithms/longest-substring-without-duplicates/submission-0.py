class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Left = start of the window & Right pointer = end of the window
        l, r = 0, 0

        # Set that stores all characters currently inside the window
        chars = set()

        # Stores the longest valid substring found so far
        max_sub = 0

        # Keep going until the right pointer reaches the end of the string
        while r < len(s):

            # If the current character is already inside the window,
            # keep shrinking the window from the left until the duplicate is gone
            while s[r] in chars:

                # Remove the character at the left pointer
                chars.remove(s[l])

                # Move the left pointer one position to the right
                l += 1

            # Add the current character to the window
            chars.add(s[r])

            # Calculate the current window length
            current_length = r - l + 1

            # Keep whichever is larger:
            max_sub = max(max_sub, current_length)

            # Expand the window by moving the right pointer
            r += 1

        # Return longest substring without duplicates
        return max_sub

        