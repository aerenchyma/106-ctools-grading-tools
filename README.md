## grading tools for SI 106

### you need
- python
- to know why this repository exists, probably

### to use

You normally download all the assignments from CTools in a .zip file, I assume, which extracts to a file name e.g. ``` PS9 ``` or ``` PS7 ``` or whatever the assignment was called in the CTools post.

1. Download/clone this repository to somewhere central/easy on your computer, maybe the folder into which you often download the .zip files for the assignments. Also save the relevant assignments folder.

2. Copy the ``` necessary_files ``` folder from this repository into the main folder with all the students' folders.

3. That folder includes ``` test106.py ```. If this assignment requires any other files (like ``` train.txt ``` and ``` test.txt ``` or whatever), copy those files into the ``` necessary_files ``` folder.

4. Also copy the ``` manage_files.py ``` file into the assignment folder, at the root level.

5. So, for example for PS9, your file structure should look like this; you can check with ``` ls ``` and/or Finder or My Computer:

	SomeFolderOnYourComputer
		PS9
			manage_files.py
			necessary_files
				test106.py
				anyotherfileeveryonewillneed.txt
			Student1 (theiruniqname)
				Submission Attachments
			Student2 (theiruniqnameyay)
				Submission Attachments
			Etc (These are all sub-directories)
				Submission Attachments


6. ``` cd <assignment folder whatever it is> ```

7. ``` python manage_files.py ```

	Or, if you want to get all the console output from running these files into a text document, pipe it to a file by running something like this:

	``` python manage_files.py > console_output_assignments.txt ``` (Then you won't see any output in your command prompt, just in that text file.)

8. You should end up with a new directory inside your assignment folder, the ``` PS9 ``` or ``` PS7 ``` folder or whatever it is, called ``` Test_Results ```. In that file is a text file for each student. Inside each of those text files is the printed output from their program. 

	So if they passed all the tests and also printed out some stuff, you'll see all of that in the text file. You should be able to see all the "Pass" and "Failed test #"s in that file, though!

	This program assumes that each student saved their problem set as, e.g. ``` ps9.py ``` or whatever. If they saved it as something else, the text file will be blank. If they didn't do the assignment, the text file will also be blank. Then to see if they get a grade, you'll have to ``` cd ``` into their appropriate folder and run their problem set. A TODO -- this should still hopefully cut down on the work required.

9. Now your file structure should look like this:

		SomeFolderOnYourComputer
			PS9
				manage_files.py
				Test_Results
					student1results.txt
					student2results.txt
					etc.txt
				necessary_files
					test106.py
					anyotherfileeveryonewillneed.txt
				Student1 (theiruniqname)
					Submission Attachments
				Student2 (theiruniqnameyay)
					Submission Attachments
				Etc (These are all sub-directories)
					Submission Attachments

NOTES
----

**1:** this does not help with side-effects of programs -- e.g. running the programs like this does not seem to write .CSV files, even if the program is properly written. I'm workin' on it. Feel free to play around!

**2:** replacing ``` manage_files.py ``` with ``` just_copy_files.py ``` will copy each of the files in the ``` necessary_files ``` folder into each of the students' sub-directories, but will NOT run any of the programs.

**3:** Ctrl + C won't quit this, because multiple processes are running. If you want to stop in the middle for any reason you have to close your command prompt window. It'll stop right when you...do that, but other than it not going through everyone, it won't break anything. If you run the manage_files program again in the same folder it will begin rewriting (like if you forgot to copy a file into ``` necessary_files ``` or something), so that should all be good.

You know where to find me
