# Quick Sort
def partition(arr, low, high):
	pivot = arr[high]
	i = low

	for j in range(low,high):
		if arr[j]<pivot:
			arr[j], arr[i] = arr[i], arr[j]
			i+=1
	
	arr[i], arr[high] = arr[high], arr[i]
	return i

def quickSort(arr, low, high):
	if low<high:
		pivot_idx = partition(arr, low, high)
		quickSort(arr,low,pivot_idx-1)
		quickSort(arr, pivot_idx+1,high)

def main():
	pass
	arr = [10, 7, 8, 9, 1, 5] 
	n = len(arr) 
	quickSort(arr,0,n-1) 
	print ("Sorted array is:") 
	for i in range(n): 
		print (arr[i], end=" ")
	print()

if __name__ == '__main__':
	main()