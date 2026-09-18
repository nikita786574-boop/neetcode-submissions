class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = dict()
        for item in nums:
            dictionary[item] = dictionary.get(item, 0) + 1
        indexes = sorted(dictionary.items(), key=lambda x: -x[1])[:k]
        result = [x[0] for x in indexes]
        return result