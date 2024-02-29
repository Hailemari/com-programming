from collections import defaultdict
 
t = int(input())
for _ in range(t):
	n = int(input())
	arr = [ord(i) - ord("0") for i in input()]
 
	pre_sum_array = [0] + arr
	for i in range(1, len(pre_sum_array)):
		pre_sum_array[i] += pre_sum_array[i - 1]
 
	count = defaultdict(int)
	for i in range(len(pre_sum_array)):
		count[pre_sum_array[i] - i] += 1
 
	good_subarrays = 0
	for val in count.values():		
		good_subarrays += val * (val - 1) // 2
		
	print(good_subarrays)