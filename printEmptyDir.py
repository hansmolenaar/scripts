import glob, os

p = os.path.dirname(os.path.realpath(__file__))
print("Path " + p)
for d in glob.glob(p + os.path.sep + "**" + os.path.sep, recursive=True):
	if len(os.listdir(d)) == 0:
		print(d + " is empty")
	#else:
		#print("Directory " + d + " is not empty")
input("ready");