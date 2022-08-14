numbers = tuple(map(float, input().split()))
nums_count = {}
for num in numbers:
    if num not in nums_count:
        nums_count[num] = 0
    nums_count[num] += 1
for nums, count in nums_count.items():
    print(f'{nums} - {count:.1f} times')

