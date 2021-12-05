Step 1 :
Go to step 1 text extract from image folder and paste all the jpg files that you wanna extract

Step 2 :
open textExtractor.py and set the path_to_tesseract to where the tesseract.exe located. eg. path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

step 3 :
set image_path according to file name so that it loop through all the files and extract text data out of it.

step 4 :
There is a variable called "file" that open a file and if not present then create it. set name in open (by default its 'extraction' and loop and extension) to your choice.

This will generate .txt files based on your .xlxs files

step 5 :
Copy all the .txt file and paste it in step 2 makeExcelSheet folder.

step 6 :
Increase range according to file and set file name in dataManipulation function (It will loop through all of them).

step 7 :
Quick check all the excel files cause it doesn't gurantee accuracy.

#####################
Software by Aryan Agrawal
Start Date : 4-12-2021
End Date : 5-12-2021
Company : BalajiNPro
######################
