# Inserting the value in sorted manner in a Linked List

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class SortedLinkedList:
	def __init__(self):
		self.head = None

	def insert(self, value):
		# if head is none
		curr = self.head

		if curr is None:
			self.head = Node(value)
			return
		
		prev = None
		# travsersal
		while(curr):
			if curr.value >= value:
				if prev is None:
					self.head = Node(value)
					self.head.next = curr
				else:
					prev.next = Node(value)
					prev.next.next = curr
				return
			
			prev = curr
			curr = curr.next

		# insert at the end
		prev.next = Node(value)

		return


	def printList(self):
		temp = self.head

		while temp:
			print(temp.value, end='\t')
			temp = temp.next



def main():
	data = [2,1,5,4,6,2,7]

	l1 = SortedLinkedList()
	for item in data:
		l1.insert(item)

	l1.printList()

if __name__ == '__main__':
	main()