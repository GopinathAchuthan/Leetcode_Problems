import math

def connectedSum(graph_node, graph_from, graph_to):
	graphs = []

	length = len(graph_from)

	for i in range(length):
		flag = False 
		# print('graphs:',graphs)
		for graph in graphs:
			# print('graph:',graph)
			# print(graph_from[i], graph_from[i] in graph)
			if graph_from[i] in graph or graph_to[i] in graph:
				flag = True
				graph.update({graph_to[i], graph_from[i]})
				break
		if not flag:
			graphs.append({graph_from[i],graph_to[i]})
	
	# print(graphs)

	if len(graphs):
		i = 0
		while(i<len(graphs)):
			j = i+1
			while(j<len(graphs)):
				if graphs[i]&graphs[j]:
					graphs[i].update(graphs[j])
					graphs.pop(j)
				else:
					j+=1
			i+=1


	# print(graphs)


	node_sum = [len(x) for x in graphs]
	# print(node_sum)
	# print(node_sum)
	isolatedGraphCount = graph_node - sum(node_sum)

	return sumOfCeilOfSqrt(node_sum)+isolatedGraphCount


def sumOfCeilOfSqrt(arr):
	return sum([math.ceil(math.sqrt(x)) for x in arr])

if __name__ == '__main__':

	graph_node = 16
	graph_from = [6,9,11,15, 13,12,15,1]
	graph_to = [11,5,9,9, 15,14,16,16]

	res = connectedSum(graph_node, graph_from, graph_to)

	print(res)