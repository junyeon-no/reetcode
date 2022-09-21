from typing import List
import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        banned.sort(key=len, reverse=True)
        par_re:str = ""
        ban = ""
        for b in banned : 
            ban += b+"|"
        ban = ban[:-1]
        paragraph = re.sub(ban, "", paragraph)
        par_re = re.sub('[^0-9a-z ]'," ", paragraph)
        rst_dic = collections.Counter(par_re.split())
        if rst_dic.most_common() == []:
            return ""
        return rst_dic.most_common(1)[0][0]
    
class Solution2:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #소문자
        #특수문자 -> 공백
        #밴 -> 공백
        par_list = [\
            word \
            for word in re.sub('[^0-9a-zA-z]', " ", paragraph).lower().split() \
                if word not in banned\
                    ]
        rst = collections.Counter(par_list)
        return rst.most_common()[0][0]

sol = Solution ()

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit", "bhbh"]
# paragraph = "a."
# banned = []
print(sol.mostCommonWord(paragraph, banned))