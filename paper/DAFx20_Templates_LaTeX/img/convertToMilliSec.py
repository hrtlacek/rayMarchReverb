with open("juliaSec.txt") as f:
	lines = f.readlines()

newlines = []
for l in lines:
	try:
		splitted = l.split()
		newline = str(float(splitted[0])*1000.)+' '+str(splitted[1])+'\n'
		print(newline)
	except:
		newline = l
	newlines.append(newline)
# print(newlines[100000])


with open("juliaMS.txt", "x") as f:
	f.writelines(newlines)