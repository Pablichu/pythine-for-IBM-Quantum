


class Account(object):
	ID_COUNT = 1
	
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
	
	def transfer(self, amount):
		self.value += amount

class Bank:
	"""The bank"""
	def __init__(self):
		self.accounts = []

	def add(self, new_account):
		""" Add new_account in the Bank
		    @new_account: Account() new account to append
	        @return   True if success, False if an error occured
	    """
		# test if new_account is an Account() instance and if
		# it can be appended to the attribute accounts
	
		if not isinstance(new_account, Account):
			print('Not an account object!!')
			return False

		self.accounts.append(new_account)
		return True

	def transfer(self, origin, dest, amount) -> bool:
#	    """ Perform the fund transfer
#	        @origin:  str(name) of the first account
#	        @dest:    str(name) of the destination account
#	        @amount:  float(amount) amount to transfer
#	        @return   True if success, False if an error occured"""
		ori = None
		des = None
		for acc in self.accounts:
			if ori == None and acc.name == origin:
				ori = acc
			if des == None and acc.name == dest:
				des = acc
		
		if not isinstance(ori, Account) or not isinstance(des, Account):
			print('Names not found')
			return False

		if ori.value < amount:
			print(ori.name + ' HAS NO MONEY TO TRANSFER ' + str(amount))
			return False
		ori.transfer(amount * -1)
		des.transfer(amount)
		return True

	def fix_account(self, name):
		""" fix account associated to name if corrupted
	        @name:   str(name) of the account
	        @return  True if success, False if an error occured
		"""
		# ... Your code ...