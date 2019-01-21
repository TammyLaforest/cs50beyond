class Point: 
	# Constructor function

	def __init__(self, x, y):
		self.x = x
		self.y = y
		# Self = object in question
		# x, y arguments

	def shift(self, x, y):
		self.x = x + x
		self.y = y + y 

p = Point(10, 20)
p.shift(2, 3)

# Use dot notation to access particular property
print(p.x)
print(p.y)

