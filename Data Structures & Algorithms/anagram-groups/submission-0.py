class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        dictionary = dict()
        for string in strs:
            item = tuple(sorted(Counter(string).items()))
            lst = dictionary.get(item, [])
            lst.append(string)
            dictionary[item] = lst
        return list(dictionary.values())