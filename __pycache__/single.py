# a=[1,2,3,3,2]
# print('the odd one is',a[0])
# a=[4,4,2,3,1,3,2]
# for i in a:
#     if  a.count(i)==1:
#       print('the odd one is =',i)

# 137
# a=[4,4,2,3,1,3,2]
# for i in a:
#      if  a.count(i)==1:
#       print('the odd one is =',i)
class Solution(object):
   def letterCombinations(self, digits):
      if len(digits) == 0:
         return []
      characters = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
      result = []
      self.solve(digits,characters,result)
      return result
   def solve(self, digits, characters, result, current_string="",current_level = 0):
      if current_level == len(digits):
         result.append(current_string)
         return
      for i in characters[int(digits[current_level])]:
         self.solve(digits,characters,result,current_string+i,current_level+1)
ob1 = Solution()
print(ob1.letterCombinations("223"))