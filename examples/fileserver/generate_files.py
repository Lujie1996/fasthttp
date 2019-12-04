import os
import random
import string

def generate_big_random_letters(filename,size):
    """
    generate big random letters/alphabets to a file
    :param filename: the filename
    :param size: the size in bytes
    :return: void
    """
    chars = ''.join([random.choice(string.letters) for i in range(size)]) #1

    with open(filename, 'w') as f:
        f.write(chars)
    pass

if __name__ == '__main__':
	print 'start generating random files...'	

	# n = input('Number of files: ')
	# s = input('File size (MB): ')
	# n = int(n)
	# s = int(s)
	n = 10

	path = 'static/'
	os.mkdir(path, 0755);

	l = [1, 16, 128, 512, 1024]
	for s in l:
		size_in_byte = s * 1024

		

		filename_prefix = str(s) + 'kb_'
		for i in range(n):
			total_path = path + filename_prefix + str(i) + ".txt"
			generate_big_random_letters(total_path, size_in_byte)
			print str(i + 1) + ' / ' + str(n) + ' files created..' 
		print 'Random file generation finished.' + str(s) + "kb"
