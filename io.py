file = open("/tmp/python.log","a")
file.seek(0)
file.write("hello world\n")
file.close()

file = open("/tmp/python.log","r+")
file.seek(0)
out=file.read()
print out

file.seek(0)
out=file.readline()
print out


file.seek(0)
out=file.readline()
while out:
	print out
	out = file.readline()

file.seek(0)
out=file.readlines()
for lines in out:
	print lines

file.close()




