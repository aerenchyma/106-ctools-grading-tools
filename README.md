## grading tools for SI 106

### you need
- python 2.7.6+
- to know why this repository exists, probably

### to use

Download the assignment files that you're grading from Canvas. A single assignment will be downloaded into a .zip folder called **submissions**. 

(Or **submissions (2)**, etc, if you've saved a folder full of assignments before in the same location, presumably you know how that stuff happens.) 

The ``` submissions ``` folder, unzipped, will contain a bunch of files -- it will contain every single file that students submitted. Each file is prepended with a student name, i.e. if Paul Resnick submits a file called ``` my-problem-set-9.py ```, in the **submissions** folder you'll see ```paul--resnick_my-problem-set-9.py```.

So,

1. Download assignment submissions folder from Canvas.

2. Clone or download this repository. 

3. Save any files required for running the problem set in the ``` necessary_files ``` folder. (In general, this will just be ```test106.py ``, and all will be fine, but for some problem sets, we use other text files, etc, that students may not have uploaded to Canvas.)

4. Copy this whole folder into the ``` submissions ``` folder. 

5. In your command line, run the following:

``` cd ``` into the submissions folder, whatever it's called/wherever it is

``` cd 106-ctools-grading-tools ```

``` python canvas_manage_files.py ``` -- run that Python script, which runs all of the Python submissions in the folder and saves the output in the ``` Test_Results ``` folder.

And then look in the ``` Test_Results ``` folder (submissions > 106-ctools-grading-tools (this folder) > Test_Results) for the files saved as each student's name in order to do the majority of the grading, referring to the files directly downloaded from Canvas if need be.



