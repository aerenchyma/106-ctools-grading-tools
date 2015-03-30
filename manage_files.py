import os, sys, subprocess
from os import walk, path
#from subprocess import call

# checks for your setup
if "necessary_files" not in [f for f in os.walk(".")][0][1]:
	print "You don't have your folder of files in the directory. Copy it over!\n"
elif "test106.py" not in [f for f in os.walk("necessary_files")][0][2]:
	print "You probably need test106.py in the necessary files folder and it ain't there yet"

# Need to run this script from inside the bulk file, e.g. PS9
# Need to save all files necessary for running people's programs
filenames =[x for x in os.listdir("necessary_files")]
#filenames = ["test106.py"] # this will always be necessary

# pass other necessary files in as command line args
# if len(sys.argv) > 1:
# 	for fl in sys.argv[1:]:
# 		filenames.append(fl)

dirs = [f for f in os.walk(".")][0][1] # all sub-directories

# copy all necessary files into each person's folder
for d in dirs: 
	dr = d.replace(" ","\ ").replace("(","\(").replace(")","\)").replace(",","\,") # handled all chars
	#print [f for f in os.walk("necessary_files")]
	try:
		for fp in [f for f in os.walk("necessary_files")][0][2]:
			os.system("cp necessary_files/{} {}/Submission\ attachment\(s\)/".format(fp,dr)) # assuming ctools format
	except:
		print "I think your file structure is wrong. Take a look at it."
# now run each and put test results/print output in a file with the name

os.system("mkdir Test_Results") # create sub-folder in this main folder for all the test results
for d in dirs: # now each has the right files in submission attachments
	dr = d.replace(" ","\ ").replace("(","\(").replace(")","\)").replace(",","\,") # handled all chars
	# run program 
	#os.system("cd {}/Submission\ attachment\(s\)/".format(dr))
	try:
		if "ps9.py" in [f for f in os.listdir("{}/Submission attachment(s)/".format(d))]:
			print "Running {} problem set...".format(dr)
			## the following works
			os.system("python {}/Submission\ attachment\(s\)/ps9.py > Test_Results/{}.txt".format(dr,dr)) # save output in Test_Results in a text file of the person's name
		else:
			print "Sorry, you'll need to rename {} pset to ps9.py...".format(dr)
	except:
		"Error. Continuing."