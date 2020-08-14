class Node:

	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None
        
	def insert(self, d):
		if self.data == d:
			return False
		elif d < self.data:
			if self.left:
				return self.left.insert(d)
			else:
				self.left = Node(d)
				return True
		else:
			if self.right:
				return self.right.insert(d)
			else:
				self.right = Node(d)
				return True

	def find(self, d):
		if self.data == d:
			return True
		elif d < self.data and self.left:
			return self.left.find(d)
		elif d > self.data and self.right:
			return self.right.find(d)
		return False