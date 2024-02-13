


class Solution:
    def longestCommonPrefix(self, sparshva):
        if not sparshva:
            return ""

        
        sparshva.sort()

        
        first_str = sparshva[0]
        last_str = sparshva[-1]

        common_prefix = []
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break

        return ''.join(common_prefix)
hi=Solution()
list=[]
n=int(input("Enter the number of elements you want to input:"))
for i in range(n):
    n=input("Enter the word:-")
    list.append(n)
hello=hi.longestCommonPrefix(list)
print(hello)
