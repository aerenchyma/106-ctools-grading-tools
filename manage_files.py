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

dirs = [f for f in os.walk(".")][0][1] # all sub-directories

# copy all necessary files into each person's folder
for d in dirs: 
	dr = d.replace(" ","\ ").replace("(","\(").replace(")","\)").replace(",","\,") # handled all chars
	try:
		for fp in [f for f in os.walk("necessary_files")][0][2]:
			os.system("cp necessary_files/{} {}/Submission\ attachment\(s\)/".format(fp,dr)) # assuming ctools format
	except:
		print "I think your file structure is wrong. Take a look at it."

# now run each and put test results/print output in a file with the student name
os.system("mkdir Test_Results") # create sub-folder in this main folder for all the test results
for d in dirs: # each has the right files in submission attachments...
	dr = d.replace(" ","\ ").replace("(","\(").replace(")","\)").replace(",","\,") # handled all chars for bash encoding
	# now run program
	try:
		curr_dir = str(os.getcwd()).split("/")[-1].lower()
		# if sys.argv[1] in [f for f in os.listdir("{}/Submission attachment(s)/".format(d))]: # pass in filename expected as command line argument
		if "{}.py".format(curr_dir) in [f.lower() for f in os.listdir("{}/Submission attachment(s)/".format(d))]: # if they have a file ps[whatever#folder] -- assume acting in eg. PS9 folder
			print "Running {} problem set...".format(dr) # for clarity
			# note: python or bash errors that occur will appear in console.
			# to see these later, could pipe output of this master program to a file.
			os.system("python {}/Submission\ attachment\(s\)/'{}.py'.format(curr_dir) > Test_Results/{}.txt".format(dr,dr)) # save output in Test_Results in a text file of the person's name
		else:
			print "Sorry, you'll need to rename {} pset to {}.py...".format(dr, curr_dir)
	except:
		"Error. Continuing."