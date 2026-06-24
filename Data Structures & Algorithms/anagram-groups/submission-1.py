class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # key = sorted version of the word
        # value = list of words with that same key
        hashmap = {}

        # Go through each word in the input list
        for word in strs:

            # Create a key by sorting the letters
            key = ''.join(sorted(word))

            # If this is the first time we've seen this key,
            # create an empty list for it
            if key not in hashmap:
                hashmap[key] = []

            # Add the current word to its anagram group
            hashmap[key].append(word)

        # Return only the groups (the dictionary values)
        return list(hashmap.values())









        