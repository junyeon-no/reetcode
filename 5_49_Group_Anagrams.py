import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rst = []
        rst_dic={}

        for str in strs:
            str_l = list(str)
            str_l.sort(key = lambda x : ord(x))
            temp_word=""
            for s in str_l : 
                temp_word+=s
            if temp_word not in rst_dic : 
                rst_dic[temp_word] = []
                rst_dic[temp_word].append(str)
            else : 
                rst_dic[temp_word].append(str)
        for d in rst_dic.items():
            rst.append(d[1])
        return rst

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rst_dic = collections.defaultdict(list)
        for word in strs:
            rst_dic[''.join(sorted(word))].append(word)
        return list(rst_dic.values())



sol = Solution2()
strs = ["eat","tea","tan","ate","nat","bat"]
strs = [""]
strs = ["a"]
print(sol.groupAnagrams(strs))