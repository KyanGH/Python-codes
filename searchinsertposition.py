nums = [1,3,5,6]
target = 7
for i in range(len(nums)) :
    if nums[i] == target:
        print(i)
        break
    if nums[i] > target:
        print (str(i) + " 2")
print (i + 1)