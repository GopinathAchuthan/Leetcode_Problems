# Find the number of integer coordinates that are illuminates by exactly 1 lamp.

def main():
	lambs = [[-2,3],[2,3],[2,1]]

	merges = []
	intervals = []

	lights = [[x-y,x+y] for x,y in lambs]
	
	lights = sorted(lights, key = lambda x : x[0])

	for light in lights:
		if intervals and intervals[-1][1]>=light[0]:
			merges.append([light[0], min(intervals[-1][1], light[1])])
			intervals[-1][1] = max(intervals[-1][1],light[1])
		
		else:
			intervals.append(light)

	merges = sorted(merges, key = lambda x : x[0])
	intervals2 = []
	for merge in merges:
		if intervals2 and merge[0]<=intervals2[-1][1]:
			intervals2[-1][1] = max(intervals2[-1][1],merge[1])
		else:
			intervals2.append(merge)


	coord1 = sum([x[1]-x[0]+1 for x in intervals])
	coord2 = sum([x[1]-x[0]+1 for x in intervals2])

	print(coord1-coord2)

if __name__ == '__main__':
	main()