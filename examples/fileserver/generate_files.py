import os

if __name__ == '__main_':

	# n = input('Number of files: ')
	# s = input('File size (MB): ')
	# n = int(n)
	# s = int(s)
	n = 100
	s = 5

	path = 'static/'
	filename_prefix = str(s) + 'mb_'
	for i in range(n):
		total_path = path + filename_prefix + str(i)
		f = open(total_path, 'wb')
		f.seek(s * 1048576)
		f.write(b'\0')
		f.close()

	print 'created!'
