import os, sys, subprocess
import rexec

if "Test_Results" not in os.listdir("."):
	os.system("mkdir Test_Results")

r = rexec.RExec()
# copies each of the files from the necessary_files folder into submissions folder
for f in os.listdir("necessary_files"):
	os.system("cp necessary_files/{} .".format(f))
# runs all the problem sets and saves them in Test_Results folder
student_psets = [f for f in os.listdir(".") if "--" in f and "ps" in f]
for ps in student_psets:
	 os.system("python r.r_execfile('{}') > Test_Results/{}.txt".format(ps,ps.split("_")[0]))