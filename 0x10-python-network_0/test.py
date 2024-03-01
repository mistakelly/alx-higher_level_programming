def find_peak(nums):
    peaks = []

    if nums is None:
        return
    for i in range(1, len(nums) - 1):
        if nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]:
            peaks.append(nums[i])
    return peaks

result = find_peak([])
print(result)

