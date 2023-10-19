class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        result = []
        i = 0
        j = 0
        while i<l1 and j<l2:
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        result.append(word1[i:])
        result.append(word2[j:])
        l3 = "".join(result)
        return l3