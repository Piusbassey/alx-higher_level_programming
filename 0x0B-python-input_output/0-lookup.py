#!/usr/bin/python3
def lookup(obj):
	"""
		Function that returns the list of available attributes and methods of an object.

		Args:
obj: Any object.

Returns:
List of the attributes and methods.
	"""
	return [attr for attr in dir(obj) if not attr.startswith('__')]
