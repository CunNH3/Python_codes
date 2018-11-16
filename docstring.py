def docstring(a,b):
	"""
	return a+b
	a : int 
	b : int
	"""
	return a+b
if  __name__=='__main__':
	print(docstring.__doc__)
	print(docstring(1,2))
