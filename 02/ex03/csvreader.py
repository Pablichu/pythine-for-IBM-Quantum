import csv
from os.path import isfile

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		
		self.filename = filename
		self.file = None
		self.csv = None

		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		if not isfile(self.filename):
			print('File not found')
			return

		self.file = open(self.filename, 'r')
		try:
			self.csv = csv.reader(self.file)
		except csv.Error:
			print('This shit cannot be parsed')
			self.csv = None
		return self

	def __exit__(self, type, value, traceback):
		if self.file:
			self.file.close()

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
			nested list (list(list, list, ...)) representing the data.
		"""
		csv_list = []
		for row in self.csv:
			csv_list.append(row)
		#csv_list = list(self.csv)[self.skip_top:self.skip_bottom]
		return csv_list


	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
			list: representing the data (when self.header is True).
			None: (when self.header is False).
		"""
		if self.header is False:
			return None
		return next(self.csv)

if __name__ == "__main__":
	#with CsvReader('bad.csv') as file:
	#	if file == None:
	#		print("File is corrupted")
	with CsvReader(filename='addresses.csv', header=True) as file:
		data = file.getdata()
		print(data)
		header = file.getheader()
		print(header)