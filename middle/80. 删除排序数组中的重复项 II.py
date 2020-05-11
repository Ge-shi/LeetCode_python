def removeDuplicates(nums: list) -> int:
    cnt = 0
    flag = False
    for i in range(1, len(nums)):
        if nums[i] != nums[cnt]:
            cnt += 1
            nums[cnt] = nums[i]
            flag = False
            continue
        if flag == False:
            flag = True
            cnt += 1
            nums[cnt] = nums[i]
            continue
    print(nums[:cnt+1])
    return cnt + 1


nums = [2,2,2,2,2,3,3,3,4]
print(removeDuplicates(nums))