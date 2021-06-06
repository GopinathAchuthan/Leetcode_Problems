# Binary Search
def binarySearch(key: int, nums: list[int]) -> int:
	left = 0
	right = len(nums)-1

	while(left<=right):
		mid = left + (right-left)//2
		if nums[mid]<key:
			left = mid+1
		elif nums[mid]>key:
			right = mid-1
		else:
			return mid

	return -1

# Find closest element to the key
	

def main():
	nums = [i for i in range(2,34)]
	key = 36

	result = binarySearch(key, nums)

	print("Result:", result)

if __name__ == '__main__':
	main()