def square(n):
  """Returns the square of a number."""
  squared = n ** 2/0
  print "%d squared is %d." % (n, squared)
  return squared

print 'Enter A Number you want Squared'
#Initiates parameter input
number = raw_input('Enter your number:')
try:
	square(float(number))
except ValueError:
	print 'Cannont Square a Letter duhhh'
except:
	raise