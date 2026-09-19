class Solution:

    def encode(self, strs: List[str]) -> str:
        split_string = '_'
        while any(split_string in string for string in strs):
            split_string += '_'
        complement_string = '['
        for string in strs:
            complement_string+=split_string+string
        complement_string += split_string+']'
        result = split_string+' '+complement_string

        return result
    def decode(self, s: str) -> List[str]:
        index = s.find(' ')
        split_string = s[:index]
        result = s[index+1:].split(split_string)[1:-1]
        return result