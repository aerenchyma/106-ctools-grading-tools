import os, sys, subprocess
from os import walk, path
from subprocess import call

# checks
if "necessary_files" not in [f for f in os.walk(".")][0][1]:
	print "You don't have your folder of files in the directory. Copy it over!\n"
elif "test106.py" not in [f for f in os.walk("necessary_files")][0][2]:
	print "You probably need test106.py in the necessary files folder and it ain't there yet"

# Need to run this script from inside the bulk file, e.g. PS9
# Need to save all files necessary for running people's programs
filenames = ["test106.py"] # this will always be necessary

if len(sys.argv) > 1:
	for fl in sys.argv[1:]:
		filenames.append(fl)

dirs = [f for f in os.walk(".")][0][1] # all sub-directories
#print dirs

# copy all necessary files into each person's folder
for d in dirs: 
	dr = d.replace(" ","\ ").replace("(","\(").replace(")","\)").replace(",","\,") # handled all chars
	#print [f for f in os.walk("necessary_files")]
	try:
		for fp in [f for f in os.walk("necessary_files")][0][2]:
			os.system("cp necessary_files/{} {}/Submission\ attachment\(s\)/".format(fp,dr)) # assuming ctools format
	except:
		print "I think your file structure is wrong. Take a look at it."