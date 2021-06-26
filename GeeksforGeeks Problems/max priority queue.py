import heapq

def main():
	container = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	N = 5

	price = sum(container)
	heapq._heapify_max(container)
	result = 0

	for _ in range(N):
		result+=price
		item = heapq._heappop_max(container)
		price -= item
		# print(result, price, item)

	print(result)


if __name__ == '__main__':
	main()