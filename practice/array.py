nums = [1,2,3,4,5,6]
# sort
# reverse
# any other array
# start = 0
# end = len(nums) -1
# while start < end:
#     nums[start] , nums[end] = nums[end] , nums[start]
#     start +=1
#     end-=1
# print(nums)

# [6, 5, 4, 3, 2, 1]
odd_no = 0
even_no = 0
for i in nums:
    if i%2==0:
        even_no += i
    else:
        odd_no += i
print(even_no)
print(odd_no)
