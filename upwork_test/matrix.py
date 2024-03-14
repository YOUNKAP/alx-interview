class Matrix(object):
	"""docstring for Matrix"""
	def __init__(self, matrix):
		self.row = len(matrix)
		self.isVector = isinstance(matrix[0], int)
		self.cols = 1 if self.isVector else len(matrix[0])
		self.matrix = [matrix] if self.isVector else matrix

	def is_vector(self):
		return self.isVector


	def transpose(self):
		return self

	def scale(self, scalar):
		self.matrix = [[num*scalar for num in row] for row in self.matrix]
		return self

	@classmethod
	def identity(cls, size):
		return cls([[int(i==j) for i in range(size)] for j in range(size)])

	@classmethod
	def zeros(cls, rows, cols):
		return cls([[0]*cols]*rows)
		