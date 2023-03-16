class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
	# ... Your code here ...

	def __enter__(...):
	# ... Your code here ...

	def __exit__(...):
	# ... Your code here ...

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
			nested list (list(list, list, ...)) representing the data.
		"""
	# ... Your code here ...
	
	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
			list: representing the data (when self.header is True).
			None: (when self.header is False).
		"""
	# ... Your code here ...

from csvreader import CsvReader
if __name__ == "__main__":
	with CsvReader('bad.csv') as file:
		if file == None:
			print("File is corrupted")
	with CsvReader('good.csv') as file:
		data = file.getdata()
		header = file.getheader()