#!/usr/bin/python3
def lookup(obj):
	"""
		Returns the list of available attributes and methods of an object.

		Args:
obj: The object whose attributes and methods need to be looked up.

Returns:
list: A list containing the names of attributes and methods of the object.
"""
return [attr for attr in dir(obj) if not attr.startswith('__')]
