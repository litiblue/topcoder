class GreaterGameDiv2(object):

	def calc(self, a, b):
		return sum(i > j for i, j in zip(a, b))
