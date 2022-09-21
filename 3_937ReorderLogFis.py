from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        return letters + digits

class Solution2:
    def reorderLogFiles(self, logs: List[str]) -> List:
        word, digits = [],[]
        for log in logs:
            if log.split()[1].isdigit() : digits.append()
            else : word.append()
        
        word.sort(key=lambda x : (x.split()[1:], x.split()[0]) )
        return word + digits

sol = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(sol.reorderLogFiles(logs))