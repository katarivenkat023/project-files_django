from django import template

register=template.Library()

def slicing1(value):
	result=value[2]
	return result

def slicing2(value):
	result=value[2:5].upper()
	return result
def slicing3(value):
	result=value[::].title()
	return result

register.filter('slicing1',slicing1)
register.filter('slicing2',slicing2)
register.filter('slicing3',slicing3)