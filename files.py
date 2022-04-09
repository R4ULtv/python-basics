# FILES
# Files are a way to store data in a program.

# Open a file
# The open() function returns a file object, which has methods for reading and writing.
# The open() function takes two arguments:
# 1. The name of the file
# 2. The mode
# The mode can be “r” for reading (default), “w” for writing, “a” for appending, “r+” for reading and writing, “w+” for writing and reading, “a+” for appending and reading, “b” for binary mode, and “t” for text mode (default).

# write
file = open("file_name.txt", "w")
file.write("Hello World")

# read
file = open("file_name.txt", "r")
print(file.read())