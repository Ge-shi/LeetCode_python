class Solution:
    def minArray(self, numbers: list) -> int:
        # return sorted(numbers)[0]
        left = 0
        right = len(numbers) - 1
        while right > left:
            mid = (right + left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[left]