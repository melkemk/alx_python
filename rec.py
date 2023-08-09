# class x:
#     def sol(nums,target):
#         self.target=target
#         self.nums=nums
#         def rec(i,curr):
#             print(sol)
#             if i>=len(self.nums):
#                 return 
#             if len(curr)==2:
#                 if(sum(curr)==self.target):
#                     sol.append(curr[:])
#                 return
#             curr.append(self.nums[i])
#             rec(i+1,curr)
#             curr.pop()
#         return rec(0,[])
            
# y=x()
# print(y.sol([0,1,2,3,4],4))


class x:
    def sol(self,nums, target):
        result = []
        def rec(i, curr):
            # print(curr)
            if i >= len(nums):
                return
            if len(curr) == 2:
                if sum(curr) == target:
                    result.append(curr[:])
                return
            curr.append(nums[i])
            rec(i, curr)
            curr.pop()

            rec(i + 1, curr) 
        rec(0, [])
        return result

y = x()
print(y.sol([0, 1, 2, 3, 4], 4))
